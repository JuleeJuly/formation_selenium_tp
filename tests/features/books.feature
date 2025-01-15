Feature: Bibliotheque
    En tant qu'utilisateur
    Je veux parcourir la Bibliotheque

    Scenario: Rechercher un livre par auteur
        Given je suis sur la page books
        When je recherche un livre par auteur
        Then la liste des livres de l auteur est affichee
