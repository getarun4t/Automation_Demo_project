# Created by arunsasi at 2020-05-18
Feature: Clark Sales - Privathaftpflicht feature
  Clark sales funnel is offering many options. One among them is "Privathaftpflicht". This feature file aims to test the entire feature.

  Scenario: New customer going through the "Privathaftpflicht" flow in "Angebote" channel
    Given Clarks Sales channel is opened
    When I am clicking on Angebote
    And select "Privathaftpflicht" option
    And select "Einverständnis" checkbox
    And select a choice in "Versichern" Page
    And select a choice in "aufgeführten" Page
    And select a choice in "bei einem Schadensfall" Page
    And enter information in ""Angebot anfordern" textbox
    And click on Zum Angebote button
    And click on ""Jetzt abschließen" button
    And create a username and password and reguster
    And fill mandatory details in the Persönliche Angaben Page
    And enter IBAN details in Zahlungsdaten Page
    And proceed from the Angaben-Übersicht Page
    And proceed fromm the Bestellung abgeschlossen Page
    And close the pop-ups in dashboard
    Then Sales Order is created