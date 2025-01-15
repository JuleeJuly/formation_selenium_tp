Feature: Verifier les elements
    En tant qu'utilisateur
    Je veux utiliser les differents elements du site

    Scenario: Selectionner des elements
        Given je suis sur la page checkbox
        When je choisis tous les documents sauf office et excel file
        Then les documents choisis sont selectionne

    Scenario: Modifier les donnees dans les tableaux
        Given je suis sur la page webtables
        When je supprime et modifie des utilisateurs
        Then les informations sont à jour