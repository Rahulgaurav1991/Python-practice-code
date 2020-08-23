import time

from selenium import webdriver
##from webdriver_manager.firefox import FirefoxDrivermanger
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class RunTest:

    def FindMutiple(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        driver.implicitly_wait(time_to_wait=120)
        driver.set_page_load_timeout(120)
        driver.find_element(By.ID, "checkBoxOption1").click()
        time.sleep(5)
        allelements = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
        print("the size fo allemenets are --->" + str(len(allelements)))
        print(len(allelements))
        for items in allelements:
            if not items.is_selected():
                items.click()

    def dropdown(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        driver.implicitly_wait(120)
        sel = Select(driver.find_element(By.NAME, "dropdown-class-example")).options
        for value in sel:
            print(value.text)
            if value.text == "Option1":
                break

    def element_Visblity(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://qaclickacademy.github.io/protocommerce/")
        driver.implicitly_wait(120)
        ## display = driver.find_element(By.XPATH, "//legend[.='Checkbox Example']")
        try:
            if (driver.find_element(By.XPATH, "//legend[.='Checkbox Example']")).is_displayed():
                print("displayed")

        except:
            print("value not found")
            

        print("hello")


r = RunTest()
##r.dropdown()
r.element_Visblity()
