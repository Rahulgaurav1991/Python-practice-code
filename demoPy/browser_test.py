import pytest
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="class")
def browserSetup(request):
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    request.cls.driver = driver

    yield
    driver.close()


@pytest.mark.usefixtures("browserSetup")
class Test_Browser:
    pass


class Test_verifyTitle(Test_Browser):
    value = ""

    def test_verify_title(self):
        self.driver.get("https://www.google.co.in/")
        value = self.driver.title
        assert value == "Google"
        value = self.driver.find_element(By.NAME, "btnK").get_attribute("aria-label")
        print(value)
