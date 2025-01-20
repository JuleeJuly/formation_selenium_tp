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

@scenario('features/books.feature', "Search for a book by author")
def test_book():
    pass

@given('I am on the books page')
def open_books_page(browser):
    browser.get('https://demoqa.com/books')
    browser.fullscreen_window()

@when('I search for a book by author')
def search_by_author(browser):
    # Verify that the search field is displayed
    assert browser.find_element(By.ID, 'searchBox').is_displayed()
    browser.find_element(By.ID, 'searchBox').send_keys('Marijn Haverbeke')
    browser.find_element(By.ID, 'searchBox').send_keys('\uE007')  # Press "Enter"
    time.sleep(1)

@then("the list of books by the author is displayed")
def verify_books_list(browser):
    # Verify that the searched book is displayed
    assert browser.find_element(By.XPATH, '//div[.="Marijn Haverbeke"]').is_displayed()
    time.sleep(2)
