import pytest
import pytest_bdd
import time

from selenium.webdriver.support.ui import Select
from pytest_bdd import parsers
from selenium import webdriver
from selenium.webdriver.common.by import By
from pytest_bdd import scenario, given,when,then

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@scenario('features/check.feature',"Selectionner des elements")
def test_checkbox():
    pass

@given('je suis sur la page checkbox')
def ouvrir_page_checkbox(browser):
    browser.get('https://demoqa.com/checkbox')
    browser.fullscreen_window()

@when('je choisis tous les documents sauf office et excel file')
def coche_decoche(browser):
    assert browser.find_element(By.XPATH, '//span[text()="Home"]').is_displayed()
    browser.find_element(By.XPATH, '//span[text()="Home"]').click()
    assert browser.find_element(By.XPATH, '//button[@class="rct-option rct-option-expand-all"]').is_displayed()
    browser.find_element(By.XPATH, '//button[@class="rct-option rct-option-expand-all"]').click()
    office = browser.find_element(By.XPATH, '//span[text()="Office"]')
    browser.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", office)
    time.sleep(1)
    assert browser.find_element(By.XPATH, '//span[text()="Office"]').is_displayed()
    browser.find_element(By.XPATH, '//span[text()="Office"]').click()
    excel = browser.find_element(By.XPATH, '//span[text()="Excel File.doc"]')
    browser.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", excel)
    time.sleep(1)
    assert browser.find_element(By.XPATH, '//span[text()="Excel File.doc"]').is_displayed()
    browser.find_element(By.XPATH, '//span[text()="Excel File.doc"]').click()

@then('les documents choisis sont selectionne')
def isoke(browser):
    time.sleep(1)
    assert browser.find_element(By.XPATH, '//span[text()="desktop"]').is_displayed()
    assert browser.find_element(By.XPATH, '//span[text()="notes"]').is_displayed()
    assert browser.find_element(By.XPATH, '//span[text()="commands"]').is_displayed()
    assert browser.find_element(By.XPATH, '//span[text()="workspace"]').is_displayed()
    assert browser.find_element(By.XPATH, '//span[text()="react"]').is_displayed()
    assert browser.find_element(By.XPATH, '//span[text()="angular"]').is_displayed()
    assert browser.find_element(By.XPATH, '//span[text()="veu"]').is_displayed()
    assert browser.find_element(By.XPATH, '//span[text()="wordFile"]').is_displayed()
    time.sleep(1)