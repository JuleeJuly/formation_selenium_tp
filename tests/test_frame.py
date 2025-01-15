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

@scenario('features/frame.feature',"Ouverture d'un nouvel onglet")
def test_open_tab():
    pass

@given('je suis sur la page browser-windows')
def ouvrir_page_windows(browser):
    browser.get('https://demoqa.com/browser-windows')

@when('j ouvre un nouvel onglet')
def open(browser):
    # Ouverture d'un nouvel onglet
    browser.find_element(By.ID, 'tabButton').click()
    

@when('le nouvel onglet est ouvert')
def open(browser):
    # se positionner sur le nouvel onglet
    browser.switch_to.window(browser.window_handles[1])
    # verifier que le titre du nouvel onglet existe
    assert browser.find_element(By.ID, 'sampleHeading').is_displayed()
    time.sleep(1)

@then('je peux le fermer')
def isoke(browser):
    # fermer le nouvel onglet
    browser.close()
    # se positionner sur la premiere fenetre
    browser.switch_to.window(browser.window_handles[0])
    # verifier que le titre de la premiere fenetre existe
    assert browser.find_element(By.XPATH, '//h1[text()="Browser Windows"]').is_displayed()
    time.sleep(1)


@scenario('features/frame.feature',"Ouverture d'une fenetre modale")
def test_open_modale():
    pass

@given('je suis sur la page modal-dialogs')
def ouvrir_fenetre_modale(browser):
    browser.get('https://demoqa.com/modal-dialogs')
    browser.fullscreen_window()

@when('je choisis une grande popup')
def open(browser):
    # ouverture de la fenetre modale
    browser.find_element(By.ID, 'showLargeModal').click()
    time.sleep(1)

@when('la popup est ouverte')
def verif(browser):
    # verifier la presence du texte de la modale
    assert browser.find_element(By.XPATH, '//div[@class="modal-body"]/p').is_displayed()

@then('le texte attendu est affiche')
def isoke(browser):
    # recuperer le texte
    texte = browser.find_element(By.XPATH, '//div[@class="modal-body"]/p').text
    # le mot a chercher
    mot = "Lorem Ipsum"
    # verifier le nombre d'occurence du mot
    nombre_occurence = texte.count(mot)
    assert nombre_occurence == 4
    # fermer la modale
    browser.find_element(By.ID, 'closeLargeModal').click()
    time.sleep(1)