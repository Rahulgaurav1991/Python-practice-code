import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from demoPy.conftest import setUP, driver
import pytest


@pytest.mark.usefixtures("setUP")
class Test_Demo:

    def test_runner(self):
        self.ActionChains(driver).move_to_element(
            driver.find_element(By.XPATH, "//legend[contains(.,'Mouse Hover Example')]")).perform()

        self.ActionChains(driver).move_to_element(driver.find_element(By.ID, "mousehover")).perform()

        self.ActionChains(driver).context_click().perform()

        time.sleep(3)
        all = driver.find_elements(By.XPATH, "//div[@class='mouse-hover-content']//a")

        for items in all:
            print(items.text)
