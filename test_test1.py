import login as login
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import time


def test_building_settings():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    login.test_login_enter_main_building()
    WebDriverWait(driver, 30).until(ec.presence_of_element_located((By.ID, "ding-menu-properties"))).click()
    element = WebDriverWait(driver, 30).until(
        ec.presence_of_element_located((By.ID, "ding-property-list-view__add-property")))
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    WebDriverWait(driver, 30).until(
        ec.presence_of_element_located((By.ID, "ding-property-list-view__add-property"))).click()
    driver.find_element(By.CSS_SELECTOR, ".ding-tab-bar__li:nth-child(2)").click()
    driver.find_element(By.ID, "ding-property-add-view__alias-name").click()
    driver.find_element(By.ID, "ding-property-add-view__alias-name").send_keys("dira 5")
    driver.find_element(By.CSS_SELECTOR, "#vs-ding-property-add-view__floor__combobox .vs__search").click()
    driver.find_element(By.ID, "vs-ding-property-add-view__floor__option-1").click()
    driver.find_element(By.CSS_SELECTOR, "#vs-ding-property-add-view__rooms__combobox .vs__search").click()
    driver.find_element(By.ID, "vs-ding-property-add-view__rooms__option-1").click()
    driver.find_element(By.ID, "ding-property-add-view__size").click()
    driver.find_element(By.ID, "ding-property-add-view__size").send_keys("100")
    driver.find_element(By.ID, "ding-property-add-view__comment").click()
    driver.find_element(By.ID, "ding-property-add-view__comment").send_keys(
        "this apartment created by automation testing")
    driver.find_element(By.CSS_SELECTOR,
                        "#vs-ding-property-add-view__specification-dropdown-61d21c909af439590905a9bb__combobox .vs__search").click()
    driver.find_element(By.ID,
                        "vs-ding-property-add-view__specification-dropdown-61d21c909af439590905a9bb__option-1").click()
    driver.find_element(By.CSS_SELECTOR, ".vs__selected-options > .vs__search:nth-child(1)").click()
    driver.find_element(By.ID,
                        "vs-ding-property-add-view__specification-dropdown-61cd7947e63388ecfb2f4c63__option-1").click()
    driver.find_element(By.ID, "ding-property-add-view__specification-input-61d21c909af439590905a9bb").click()
    driver.find_element(By.ID,
                        "ding-property-add-view__specification-input-61d21c909af439590905a9bb").send_keys(
        "parking")
    driver.find_element(By.ID, "ding-property-add-view__specification-input-61cd7947e63388ecfb2f4c63").click()
    driver.find_element(By.ID,
                        "ding-property-add-view__specification-input-61cd7947e63388ecfb2f4c63").send_keys(
        "warehouse")
    driver.find_element(By.ID, "ding-property-add-view__submit").click()
