import pytest
import selenium
from selenium import webdriver
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

driver = None


@pytest.fixture(scope='module')
def setUP():
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.delete_all_cookies()
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    yield
    driver.close()


def test_login():
    a = 10
    b = 20
    assert a + 10 == b, "both are same "
    print("the value after sum is -->:"
          "" + str(a + 10))


def test_rahul():
    a = "selenium"
    assert a.upper() == "SELENIUM"


def test_value():
    a = 20
    assert a == 10


@pytest.mark.login.usefixtures("setUP")
def test_run():
    list = []

    listexp = ['Select', 'Option1', 'Option2', 'Option3']

    sel = Select(driver.find_element_by_id("dropdown-class-example")).options
    for items in sel:
        list.append(items.text)

    assert list == listexp
    ## assert list in listexp
    print(list)


@pytest.mark.usefixtures("setUP")
def test_run2():
    driver.find_element_by_id("openwindow").click()

    handles = driver.window_handles
    size = len(handles)
    parent_handle = driver.current_window_handle
    for x in range(size):
        if handles[x] != parent_handle:
            driver.switch_to.window(handles[x])
            print(driver.title)
            driver.close()
            break

    driver.switch_to.window(parent_handle)
