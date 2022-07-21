# Createad by Diego Chacón 07/21/2022

Feature: As a Customer when I search for Alexa, I want to see if the third option on the second page is available for purchase and can be added to the cart

    Scenario: Search the product Alexa in the Amazon webpage
        GIVEN the user navigates to www.amazon.com
        AND Searches for "<SearchBy>"
        AND navigates to the second page
        AND selects the third item
        THEN assert that the item would be available for purchase, the user would be able to add it to the cart
    
    Example: 
        | SearchBy |
        | Alexa    |