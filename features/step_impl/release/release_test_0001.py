from getgauge.python import step, before_scenario
import os
import json

from kylin_utils import util


@before_scenario()
def before_scenario_hooks():
    global client
    global data
    client = util.setup_instance('kylin_instance.yml')
    with open(os.path.join('data/release_test_0001', 'release_test_0001.json'),
              'r') as f:
        data = json.load(f)


@step("Create project <project_name> and load table <tables>")
def prepare_project_step(project_name, tables):
    client.create_project(project_name=project_name)
    tables = data.get(tables)
    resp = client.load_table(project_name=project_name, tables=tables)
    assert ",".join(resp["result.loaded"]) == tables


@step("Create model with <model_desc> in <project>")
def create_model_step(model_desc, project):
    model_name = data.get(model_desc).get('name')
    model_desc_data = data.get(model_desc)

    resp = client.create_model(project_name=project,
                               model_name=model_name,
                               model_desc_data=model_desc_data)
    assert json.loads(resp['modelDescData'])['name'] == model_name


@step("Create cube with <cube_desc> in <prpject>, cube name is <cube_name>")
def create_cube_step(cube_desc, project, cube_name):
    resp = client.create_cube(project_name=project,
                              cube_name=cube_name,
                              cube_desc_data=data.get(cube_desc))
    assert json.loads(resp['cubeDescData'])['name'] == cube_name


@step("Build segment from <start_time> to <end_time> in <cube_name>")
def build_first_segment_step(start_time, end_time, cube_name):
    resp = client.build_segment(start_time=start_time,
                                end_time=end_time,
                                cube_name=cube_name)
    assert client.await_job_finished(job_id=resp['uuid'], waiting_time=20)


@step("Merge cube <cube_name> segment from <start_name> to <end_time>")
def merge_segment_step(cube_name, start_time, end_time):
    resp = client.merge_segment(cube_name=cube_name,
                                start_time=start_time,
                                end_time=end_time)
    assert client.await_job_finished(job_id=resp['uuid'], waiting_time=20)


@step("Clone cube <old_cube_name> and name it <new_cube_name> in <project>, modify build engine to <engine>")
def clone_cube_step(old_cube_name, new_cube_name, project, build_engine):
    resp = client.clone_cube(cube_name=old_cube_name,
                             new_cube_name=new_cube_name,
                             project_name=project)
    assert resp.get('name') == new_cube_name
    client.update_cube_engine(cube_name=new_cube_name,
                              engine_type=build_engine)


@step("Query SQL <SQL> and specify <cube_name> cube to query in <project>, compare result with <result>")
def query_cube_step(sql, cube_name, project, result):
    resp = client.execute_query(cube_name=cube_name,
                                project_name=project,
                                sql=sql)
    assert resp.get('isException') is False
    assert resp.get('results')[0][0] == result
    assert resp.get('cube') == 'CUBE[name=' + cube_name + ']'
    assert resp.get('pushDown') is False


@step("Disable cube <cube_name>")
def disable_cube_step(cube_name):
    resp = client.disable_cube(cube_name=cube_name)
    assert resp.get('status') == 'DISABLED'


@step("Query SQL <SQL> in <project> and pushdown, compare result with <result>")
def query_pushdown_step(sql, project, result):
    resp = client.execute_query(project_name=project, sql=sql)
    assert resp.get('isException') is False
    assert resp.get('results')[0][0] == result
    assert resp.get('cube') == ''
    assert resp.get('pushDown') is True
