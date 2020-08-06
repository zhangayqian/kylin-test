from getgauge.python import step

from utils import kylin


class ReleaseTest:

    client = kylin.setup_instance()

    @step("Create model with <model_desc_data> in data file <release_test_0001.json>")
    def create_model_step(self):

