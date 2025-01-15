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

@scenario('features/check.feature',"Modifier les donnees dans les tableaux")
def test_modif():
    pass

@given('je suis sur la page webtables')
def ouvrir_page_table(browser):
    browser.get('https://demoqa.com/webtables')
    browser.fullscreen_window()
    time.sleep(1)

@when('je supprime et modifie des utilisateurs')
def modification(browser):
    #suppression des deux derniers utilisateurs
    browser.find_element(By.ID, 'delete-record-2').click()
    browser.find_element(By.ID, 'delete-record-3').click()
    time.sleep(1)
    #modification du salaire du premier utilisateur
    browser.find_element(By.ID, 'edit-record-1').click()
    time.sleep(1)
    browser.find_element(By.ID, 'salary').clear()
    browser.find_element(By.ID, 'salary').send_keys('4300')
    browser.find_element(By.ID, 'submit').click()
    time.sleep(1)

@then('les informations sont à jour')
def isoke(browser):
    salaire = browser.find_element(By.CSS_SELECTOR, '.rt-tbody > div:nth-of-type(1) div:nth-of-type(5)')
    #Verifier que le salaire vaut bien 4300
    assert salaire.text == '4300'
    #Verifier que la deuxieme ligne du tableau est vide
    assert browser.find_element(By.XPATH, '//div[@class="rt-tbody"]/div[2]/div[@class="rt-tr -padRow -even"]/div[1]').text == ' '
    time.sleep(1)