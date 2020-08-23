import pytest

from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(params=["Chrome", "Firefox"], scope="class")
def browserSetup(request):
    if request.param == "Chrome":
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://google.com")
        driver.set_page_load_timeout(120)
        driver.delete_all_cookies()
    if request.param == "Firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        driver.maximize_window()
        driver.get("https://google.com")
        driver.set_page_load_timeout(120)
        driver.delete_all_cookies()
    request.cls.driver = driver
    yield
    driver.close()
