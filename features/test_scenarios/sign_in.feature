Feature: Sign in 
    Scenario: Sign in after new account creation
        Given i created account successfully
        When i press login button
        Then i logged in successfully
