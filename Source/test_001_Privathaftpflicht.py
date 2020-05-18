#This file is used to specify the pytest implentation of the feature file.
#All the Gherkin line definitions is done in this file
#This file cane be used while reusing Gherkin implementations

from pytest_bdd import scenario, given, when, then
from Drivers.chromedriver import driver
from Environment.QA_challenge import credentials
from Pages.Clark_Sales import Dashboard, Angebote, Privathaftpflicht, Versichern, Aufgeführten, Weiter, Schadensfall, Anmerkungen, \
    Zum_angebote, Angebotes, Sichern, Personliche_Angaben, Zahlungsdaten, Angaben_Ubersicht, Bestellung, Gefallt
from Synchronization.custom_wait import wait_for, wait_if_displayed, wait_till_element_disappears
from selenium.webdriver.common.by import By


@scenario('../Features/test_001_Privathaftpflicht.feature','New customer going through the "Privathaftpflicht" flow in "Angebote" channel')
def test_new_customer():
    pass


@given("Clarks Sales channel is opened")
def dashboard_verify():
    pass                                                                                # Covered in conftest.py


@when("I am clicking on Angebote")
def click_angebote():
    wait_and_click(By.XPATH, Dashboard.angebote)
    wait_if_displayed(Angebote.privathaftpflicht, Dashboard.angebote, 5)
    wait_till_element_disappears(Dashboard.dashboard)


@when('select "Privathaftpflicht" option')
def click_privathaftpflicht():
    wait_and_click(By.XPATH, Angebote.privathaftpflicht)
    wait_if_displayed(Privathaftpflicht.einverstandnis, Angebote.privathaftpflicht, 3)
    wait_till_element_disappears(Angebote.privathaftpflicht)


@when('select "Einverständnis" checkbox')
def click_einverstandnis():
    wait_and_click(By.XPATH, Privathaftpflicht.einverstandnis)
    wait_and_click(By.XPATH, Privathaftpflicht.angebot_anfordern)


@when('select a choice in "Versichern" Page')
def select_versichern():
    wait_and_click(By.XPATH, Versichern.mich_alleine)                                   #randint method may be used to select random choices here during each execution
    wait_if_displayed(Aufgeführten.beschaftigt, Weiter.weiter, 2)


@when('select a choice in "aufgeführten" Page')
def select_versichern():
    wait_and_click(By.XPATH, Aufgeführten.beschaftigt)
    wait_if_displayed(Schadensfall.bereit, Weiter.weiter, 2)


@when('select a choice in "bei einem Schadensfall" Page')
def select_schadensfall():
    wait_and_click(By.XPATH, Schadensfall.bereit)
    wait_if_displayed(Anmerkungen.anfordern_textbox, Weiter.weiter, 2)


@when('enter information in ""Angebot anfordern" textbox')
def select_aufgefuhrten():
    wait_and_click(By.XPATH, Anmerkungen.anfordern_textbox)
    driver.find_element_by_xpath(Anmerkungen.anfordern_textbox).send_keys("Automation test request")
    wait_and_click(By.XPATH, Anmerkungen.anfordern_button)
    wait_if_displayed(Zum_angebote.angebote_button, Anmerkungen.anfordern_button, 2)
    wait_till_element_disappears(Anmerkungen.anfordern_button)


@when("click on Zum Angebote button")
def zum_angebote():
    wait_and_click(By.XPATH, Zum_angebote.angebote_button)
    wait_if_displayed(Angebotes.jetzt_abschlieben, Zum_angebote.angebote_button, 2)


@when('click on ""Jetzt abschließen" button')
def angebote():
    wait_for(By.XPATH, Angebotes.selected_plan)
    global plan                                                                                 #copying the selected plan to verify in the dashboard
    plan = driver.find_element_by_xpath(Angebotes.selected_plan).text
    wait_and_click(By.XPATH, Angebotes.jetzt_abschlieben)
    wait_if_displayed(Sichern.email_password, Angebotes.jetzt_abschlieben, 2)


@when("create a username and password and reguster")
def sichern():
    wait_and_click(By.XPATH, Sichern.email_password)
    driver.find_element_by_xpath(Sichern.email_textbox).send_keys(credentials.email_id)
    driver.find_element_by_xpath(Sichern.email_password).send_keys(credentials.password)
    wait_and_click(By.XPATH, Sichern.jetzt_registrieren)
    wait_if_displayed(Personliche_Angaben.herr, Sichern.jetzt_registrieren, 2)


@when("fill mandatory details in the Persönliche Angaben Page")
def personliche():
    wait_and_click(By.XPATH, Personliche_Angaben.herr)
    driver.find_element_by_xpath(Personliche_Angaben.vorname).send_keys(credentials.first_name)
    driver.find_element_by_xpath(Personliche_Angaben.nachname).send_keys(credentials.last_name)
    driver.find_element_by_xpath(Personliche_Angaben.geburtsdatum).send_keys(credentials.birth_date)
    driver.find_element_by_xpath(Personliche_Angaben.strabe).send_keys(credentials.street)
    driver.find_element_by_xpath(Personliche_Angaben.hausnr).send_keys(credentials.house_number)
    driver.find_element_by_xpath(Personliche_Angaben.plz).send_keys(credentials.ZIP)
    driver.find_element_by_xpath(Personliche_Angaben.ort).send_keys(credentials.city)
    driver.find_element_by_xpath(Personliche_Angaben.telefonnummer).send_keys(credentials.phone_number)
    wait_and_click(By.XPATH, Personliche_Angaben.weiter)
    wait_if_displayed(Zahlungsdaten.check, Personliche_Angaben, 2)


@when("enter IBAN details in Zahlungsdaten Page")
def zahlungsdaten():
    wait_and_click(By.XPATH, Zahlungsdaten.check)
    driver.find_element_by_xpath(Zahlungsdaten.IBAN).send_keys(credentials.bank_account)
    wait_and_click(By.XPATH, Zahlungsdaten.tarif)
    wait_if_displayed(Angaben_Ubersicht.jetzt_verbindlich_kaufen, Zahlungsdaten.tarif, 2)
    wait_till_element_disappears(Zahlungsdaten.tarif)


@when("proceed from the Angaben-Übersicht Page")
def Angaben():
    wait_for(By.XPATH, Angaben_Ubersicht.check)
    driver.find_element_by_xpath(Angaben_Ubersicht.check).location_once_scrolled_into_view              #to scroll the checkbox into view
    driver.find_element_by_xpath(Angaben_Ubersicht.check).click()
    wait_and_click(By.XPATH, Angaben_Ubersicht.jetzt_verbindlich_kaufen)
    wait_if_displayed(Bestellung.zuruck_zur_ubersicht, Angaben_Ubersicht.jetzt_verbindlich_kaufen, 5)
    wait_till_element_disappears(Angaben_Ubersicht.jetzt_verbindlich_kaufen)


@when("proceed fromm the Bestellung abgeschlossen Page")
def Bestelung():
    wait_and_click(By.XPATH, Bestellung.zuruck_zur_ubersicht)
    wait_if_displayed(Gefallt.nein, Bestellung.zuruck_zur_ubersicht, 2)


@when("close the pop-ups in dashboard")
def gefallt():
    wait_and_click(By.XPATH, Gefallt.nein)
    wait_and_click(By.XPATH, Gefallt.close)


@then("Sales Order is created")
def plan_check():
    wait_for(By.XPATH, Dashboard.plan_name)
    plan_dashboard = driver.find_element_by_xpath(Dashboard.plan_name).text
    assert plan == plan_dashboard                                                           #asserting the selected plan

def wait_and_click(type, locator):
    wait_for(type, locator)                                                                 #custom method to wait for an element and click
    driver.find_element_by_xpath(locator).click()                                           #the method can be implemented in the conftest.py file as well