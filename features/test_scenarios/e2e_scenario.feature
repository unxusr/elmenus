Feature: Find a resturant and make an order
    Scenario: End to End scenario Find a restaurant and create user and make an order
        Given i visit elmenus.com as a guest user
        When i type a "McDonald's" in the search field
        And i press "go" button
        And i click on "McDonald's"
        Then i can see all "McDonald's" menu items
        And i can select item from McDonald' menu
        And i stopped by the login modal
        And i create new account
        And i select my location
        And i fill in my address information
        And i placed the order sucessfully
