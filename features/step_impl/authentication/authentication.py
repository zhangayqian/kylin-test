from getgauge.python import step, before_scenario, Messages
from utils import kylin


class LoginTest:

    client = kylin.setup_instance("kylin_instance.yml")

    @step("Authentication with user <user> and password <password>.")
    def assert_authentication_failed(self, user, password):
        resp = self.client.login(username=user, password=password)
        assert len(resp) == 0

    @step("Authentication with built-in user <table>")
    def assert_authentication_success(self, table):
        for i in range(1, 3):
            user = table.get_row(i)
            resp = self.client.login(username=user[0], password=user[1])
            assert resp.get('userDetails').get('username') == user[0]
