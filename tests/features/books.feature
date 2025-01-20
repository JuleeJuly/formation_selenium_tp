Feature: Library
    As a user
    I want to browse the library

    Scenario: Search for a book by author
        Given I am on the books page
        When I search for a book by author
        Then the list of books by the author is displayed
