import time

import pytest

from traceback import print_stack

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager





def test_Value():
    try:
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.jntua.ac.in/")
        driver.implicitly_wait(120)
        value = driver.find_element(By.XPATH, "//marquee//li[5]//a").text
        driver.save_screenshot("C:\\Users\\win10\\Desktop\\RahulPhyton\\demoPy.png")
        print("the text is:---->>" + value)
        # element = driver.find_element_by_xpath("//strong[.='Our Mission']")
        driver.execute_script("arguments[0].scrollIntoView();",
                              driver.find_element_by_xpath("//strong[.='Our Mission']"))
        time.sleep(5)
        # assert value in "Information to the Constituent "
    except:

        print_stack()









    else:
        print("hello")


    finally:
        print("Rahul")


def test_swith_window():
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    driver.implicitly_wait(120)
    driver.find_element(By.ID, "openwindow").click()
    Parent = driver.current_window_handle
    print("the parent title is--->" + driver.title)
    childWindows = driver.window_handles

    for window in childWindows:
        if window != Parent:
            driver.switch_to.window(window)
            driver.maximize_window()
            print("The title of window is:-->" + driver.title)
            driver.close()
            break

    driver.switch_to.window(Parent)
    print("the parent title is--->" + driver.title)
    driver.close()


def test_rahul_Window():
    list = []
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    driver.implicitly_wait(120)
    driver.find_element(By.ID, "openwindow").click()
    parent = driver.current_window_handle
    child = driver.window_handles
    for allwindows in child:
        if allwindows not in parent:
            driver.switch_to.window(allwindows)
            driver.maximize_window()
            print("The title of web pages is:--->" + driver.title)
            driver.close()

    driver.switch_to.window(parent)
    print("the title of web page is:--->" + driver.title)
    driver.close()


def test_Frames():
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.maximize_window()
    driver.delete_all_cookies()
    driver.get("https://letskodeit.teachable.com/p/practice")
    driver.implicitly_wait(120)
    driver.execute_script("arguments[0].scrollIntoView();",
                          driver.find_element_by_id("courses-iframe"))

    WebDriverWait(driver, 120).until(expected_conditions.frame_to_be_available_and_switch_to_it(
        driver.find_element(By.XPATH, "//iframe[contains(@id,'courses')]")))

    # driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[contains(@id,'courses')]"))
    driver.find_element(By.ID, "search-courses").send_keys("Rahul")
    driver.switch_to.default_content()


def test_Action(setUP):
    try:
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.maximize_window()
        driver.delete_all_cookies()
        driver.get("https://letskodeit.teachable.com/p/practice")
        driver.implicitly_wait(120)

        ActionChains(driver).move_to_element(
            driver.find_element(By.XPATH, "//legend[contains(.,'Mouse Hover Example')]")).perform()

        ActionChains(driver).move_to_element(driver.find_element(By.ID, "mousehover")).perform()

        ActionChains(driver).context_click().perform()

        time.sleep(3)
        all = driver.find_elements(By.XPATH, "//div[@class='mouse-hover-content']//a")

        for items in all:
            print(items.text)


    except(Exception):
        print_stack()

    else:
        print("Rahul")
    finally:
        driver.close()


@pytest.fixture()
def setup():
    print("I am first to runn")
    yield
    print("i am last to run")


def test_name(setup):
    print("this is my test case ")
