#This file is used to store all information related to Chromedriver


from selenium import webdriver

#To execute the code in a dockerized environment, please use the below code

options = webdriver.ChromeOptions()
URL = 'http://localhost:4444/wd/hub'
options.add_argument("start-maximized")
options.add_argument("enable-automation")
options.add_argument("--no-sandbox")
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-browser-side-navigation")
options.add_argument("--disable-gpu")
driver = webdriver.Remote(command_executor=URL,
                          desired_capabilities=options.to_capabilities())

#To execute the code in the local environment, please use the below code

# chromedriver = '/usr/local/bin/chromedriver'
# driver = webdriver.Chrome(chromedriver)
# driver.maximize_window()