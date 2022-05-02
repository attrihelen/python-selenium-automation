# Created by lenaa at 5/2/2022
Feature: Amazon Sign In page verification

  Scenario: Verify Sign In page opens once Returns & Orders clicked
    Given Open Amazon page
    When Click on Returns&Orders icon
    Then Verify Sign-In text is present