Feature: Verifier les frames,les alertes et les fenetres
    En tant qu'utilisateur
    Je veux utiliser les frames, les alertes et les fenetres du site

    Scenario: Ouverture d'un nouvel onglet
        Given je suis sur la page browser-windows
        When j ouvre un nouvel onglet
        Then le nouvel onglet est ouvert et je peux le fermer

    Scenario: Ouverture d'une fenetre modale
        Given je suis sur la page modal-dialogs
        When je choisis une grande popup
        Then la popup s ouvre et affiche le texte attendu