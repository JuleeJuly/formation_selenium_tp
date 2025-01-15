Feature: Verifier les widgets
    En tant qu'utilisateur
    Je veux utiliser les différents widgets du site

    Scenario: Utiliser une barre de progression
        Given je suis sur la page progress-bar
        When je lance le chargement
        Then le chargement se termine sans erreurs

    Scenario: Utiliser un menu
        Given je suis sur la page menu
        When je veux ouvrir le menu
        Then je peux acceder à un sous menu
    
    Scenario: Utiliser des listes deroulantes
        Given je suis sur la page select-menu
        When je choisis differentes options
        Then les options sont selectionnees