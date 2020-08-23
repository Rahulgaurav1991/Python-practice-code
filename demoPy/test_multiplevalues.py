import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("browserSetup")
class BaseTest:
    pass


class TestLogin(BaseTest):

    def test_verifyTitle(self):

        print(self.driver.title)

    @pytest.mark.parametrize("username, password", [("rahul", 123), ("gaurav", 23455)])
    def test_login(self, username, password):
        """
        this method is used to login to Application
        :param username:
        :param password:
        :return:
        """

        self.driver.get("https://www.facebook.com/")
        self.driver.find_element(By.ID, "email").send_keys(username)
        self.driver.find_element(By.ID, "pass").send_keys(password)
