import pytest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import config as cfg

driver = webdriver.Chrome(ChromeDriverManager().install())


def test_login_enter_main_building():
    driver.maximize_window()
    driver.get(cfg.globalConfig["URL"])
    WebDriverWait(driver, 30).until(ec.presence_of_element_located((By.ID, 'ding-register-view__login'))).click()
    phoneElement = WebDriverWait(driver, 30).until(ec.presence_of_element_located((By.XPATH, '//*[@id="ding-login'
                                                                                             '-view__phone"]/input')))
    phoneElement.send_keys(cfg.mainTenant["phoneNumber"])
    WebDriverWait(driver, 30).until(ec.presence_of_element_located((By.ID, 'ding-login-view__submit'))).click()
    # element = WebDriverWait(driver, 30).until(ec.presence_of_element_located((By.CLASS_NAME, 'ap-otp-input')))
    # here i need to create a function for receiving otp from api
    time.sleep(40)
    buildings = WebDriverWait(driver, 30).until(ec.presence_of_all_elements_located((By.CLASS_NAME, 'box')))
    buildings[1].click()
