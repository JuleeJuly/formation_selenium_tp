Feature: Verifier les frames,les alertes et les fenetres
    En tant qu'utilisateur
    Je veux utiliser les frames, les alertes et les fenetres du site

    Scenario: Ouverture d'un nouvel onglet
        Given je suis sur la page browser-windows
        When j ouvre un nouvel onglet
        And le nouvel onglet est ouvert
        Then je peux le fermer

    Scenario: Ouverture d'une fenetre modale
        Given je suis sur la page modal-dialogs
        When je choisis une grande popup
        And la popup est ouverte
        Then le texte attendu est affiche