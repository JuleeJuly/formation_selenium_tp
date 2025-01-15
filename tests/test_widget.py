import pytest
import pytest_bdd
import time

from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pytest_bdd import parsers
from selenium import webdriver
from selenium.webdriver.common.by import By
from pytest_bdd import scenario, given,when,then
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@scenario('features/widget.feature',"Utiliser une barre de progression")
def test_progress_bar():
    pass

@given('je suis sur la page progress-bar')
def ouvrir_page_progress_bar(browser):
    browser.get('https://demoqa.com/progress-bar')
    browser.fullscreen_window()
    time.sleep(1)

@when('je lance le chargement')
def start(browser):
    # lancer le chargement
    browser.find_element(By.ID, 'startStopButton').click()
    
@then('le chargement se termine sans erreurs')
def isoke(browser):
    #on attend que le bouton reset soit visible afin de verifier que le chargement soit terminé
    try:
        element = WebDriverWait(browser, 15).until(
            EC.visibility_of_element_located((By.ID, 'resetButton'))
        )
    except NoSuchElementException:
        print("L'élément n'existe pas.")

@scenario('features/widget.feature',"Utiliser un menu")
def test_menu():
    pass

@given('je suis sur la page menu')
def ouvrir_page_menu(browser):
    browser.get('https://demoqa.com/menu')
    browser.fullscreen_window()
    time.sleep(1)

@when('je veux ouvrir le menu')
def open_menu(browser):
    # scroller afin de voir le menu
    btn = browser.find_element(By.XPATH, '//a[.="Main Item 2"]')
    browser.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", btn)
    # survoler les différents éléments du menu
    ActionChains(browser).move_to_element(browser.find_element(By.XPATH, '//a[.="Main Item 2"]')).perform()
    time.sleep(1)
    ActionChains(browser).move_to_element(browser.find_element(By.XPATH, '//a[.="SUB SUB LIST »"]')).perform()
    time.sleep(1)
    ActionChains(browser).move_to_element(browser.find_element(By.XPATH, '//a[.="Sub Sub Item 2"]')).perform()
    time.sleep(1)

@then('je peux acceder à un sous menu')
def isoke(browser):
    # verifier que le bouton Sub Sub Item 2 est visible
    assert browser.find_element(By.XPATH, '//a[.="Sub Sub Item 2"]').is_displayed()

@scenario('features/widget.feature',"Utiliser des listes deroulantes")
def test_select():
    pass

@given('je suis sur la page select-menu')
def ouvrir_page_select(browser):
    browser.get('https://demoqa.com/select-menu')
    browser.fullscreen_window()
    time.sleep(1)
    
@when('je choisis differentes options')
def choisir_options(browser):
    # on selectionne "Another root option" dans le premier select 
    browser.find_element(By.ID, 'withOptGroup').click()
    browser.find_element(By.ID, 'react-select-2-option-3').click()
    # scroll
    btn = browser.find_element(By.ID, 'cars')
    browser.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", btn)
    time.sleep(1)
    # on selectionne "Other" dans le deuxieme select
    browser.find_element(By.XPATH, '//div[@id="selectOne"]/div/div').click()
    browser.find_element(By.XPATH, '//div[@id="selectOne"]/div[2]/div/div/div[2]/div[6]').click()
    time.sleep(1)
    # on selectionne "Aqua" dans le troisieme select
    select = Select(browser.find_element(By.ID, 'oldSelectMenu'))
    select.select_by_visible_text('Aqua')
    # on selectionne "Black" et "Red" dans le quatrieme select
    browser.find_element(By.XPATH, '//div[@id="selectMenuContainer"]/div[7]/div/div/div/div').click()
    browser.find_element(By.ID, 'react-select-4-option-2').click()
    time.sleep(1)
    browser.find_element(By.ID, 'react-select-4-option-3').click()
    time.sleep(1)

@then('les options sont selectionnees')
def isoke(browser):
    # verifier que le premier select contient "Another root option"
    assert browser.find_element(By.ID, 'withOptGroup').text == 'Another root option'
    # verifier que le deuxieme select contient "Other"
    assert browser.find_element(By.XPATH, '//div[@id="selectOne"]/div/div').text == 'Other'
    # verifier que le troisieme select contient "Aqua" dont la valeur est "10"
    assert browser.find_element(By.ID, 'oldSelectMenu').get_attribute('value') == '10'
    # verifier que le quatrieme select contient "Black" et "Red"
    selectMenuContainer = browser.find_element(By.XPATH, '//div[@id="selectMenuContainer"]/div[7]/div/div/div/div')
    assert selectMenuContainer.text == 'Black\nRed',f"La valeur attendue est Black\nRed mais la valeur recue est : '{selectMenuContainer.text}'"