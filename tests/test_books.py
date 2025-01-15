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

@scenario('features/books.feature',"Rechercher un livre par auteur")
def test_livre():
    pass

@given('je suis sur la page books')
def ouvrir_page_livre(browser):
    browser.get('https://demoqa.com/books')
    browser.fullscreen_window()

@when('je recherche un livre par auteur')
def recherche_par_auteur(browser):
    # Verifie que le champ de recherche est affiche
    assert browser.find_element(By.ID, 'searchBox').is_displayed()
    browser.find_element(By.ID, 'searchBox').send_keys('Marijn Haverbeke')
    browser.find_element(By.ID, 'searchBox').send_keys('\uE007')
    time.sleep(1)

@then('la liste des livres de l auteur est affichee')
def isoke(browser):
    # Verifie que le livre recherche est affiche
    assert browser.find_element(By.XPATH, '//div[.="Marijn Haverbeke"]').is_displayed()
    time.sleep(2)
