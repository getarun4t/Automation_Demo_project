#This page is used to store the locator and actions for every page in the Clark Sales Funnel. Each class corresponds to each page in the
#Clark Sales Funnel

class Dashboard():
    dashboard = "//span[contains(.,'Verträge digitalisieren')]"
    angebote = "//a[contains(.,'Angebote')]"
    plan_name = "//div[@class='_subtitle_niboal']"

class Angebote():
    privathaftpflicht = "//p[@title='Privathaftpflicht']"

class Privathaftpflicht():
    einverstandnis = "//label[contains(@for,'consent-broker')]"
    angebot_anfordern = "//button[contains(.,'Angebot anfordern')]"

class Versichern():
    mich_alleine = "//h2[contains(.,'Mich alleine')]"

class Aufgeführten():
    beschaftigt = "//h2[contains(.,'Dienst beschäftigt')]"

class Schadensfall():
    bereit = "//h2[contains(.,'Gerne bin ich bereit bei einem Schaden bis zu 150,-EUR selbst zu zahlen, wenn dadurch meine Prämie sinkt')]"

class Anmerkungen():
    anfordern_textbox = "//input[@type='text']"
    anfordern_button = "//button[contains(.,'Angebot anfordern')]"

class Zum_angebote():
    angebote_button = "//a[contains(.,'Zum Angebot')]"

class Angebotes():
    jetzt_abschlieben = "/html/body/div[3]/div/div/div/main/div[2]/div/div/section/div/section[1]/div/div/div[2]/div[2]/button/span/span"
    selected_plan = "/html/body/div[3]/div/div/div/main/div[2]/div/div/section/div/section[1]/div/div/div[2]/div[2]/p[1]"

class Sichern():
    email_textbox = "//input[@type='email']"
    email_password = "//input[@type='password']"
    jetzt_registrieren = "//button[contains(.,'Jetzt registrieren')]"

class Personliche_Angaben():
    herr = "//span[contains(.,'Herr')]"
    vorname = "//input[@name='firstName']"
    nachname = "//input[@name='lastName']"
    geburtsdatum = "//input[@name='birthdate']"
    strabe = "//input[@name='street']"
    hausnr = "//input[@name='houseNumber']"
    plz = "//input[@name='zipcode']"
    ort = "//input[@name='city']"
    telefonnummer = "//input[@name='phoneNumber']"
    weiter = "//button[contains(.,'Weiter')]"

class Zahlungsdaten():
    IBAN = "//input[@type='text']"
    check = "//label[@for='ibanCheck']"
    tarif = "//button[contains(.,'Tarif bestellen')]"

class Angaben_Ubersicht():
    check = "//label[@for='termsCheck']"
    jetzt_verbindlich_kaufen = "//button[contains(.,'Jetzt verbindlich kaufen')]"

class Bestellung():
    zuruck_zur_ubersicht = "//button[contains(.,'Zurück zur Übersicht')]"

class Gefallt():
    nein = "//button[contains(.,'Nein')]"
    close = "//div[@tabindex='-1']"

class Weiter():
    weiter = "//button[contains(.,'Weiter')]"