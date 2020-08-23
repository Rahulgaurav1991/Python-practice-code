from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chromehrome(executable_path=ChromeDriverManager().install())
wait = WebDriverWait(driver, 120).until(expected_conditions.element_to_be_clickable(By.XPATH, ""))
