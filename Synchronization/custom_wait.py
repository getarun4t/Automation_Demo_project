# This file is used as a single point of storage for all Synchronization statements used in the entire framework
# Custom waits has been implemented since webdriver waits were not successful in Synchronizing the UI and the code

from Drivers.chromedriver import driver
import time


def wait_for(type, locator):
    while (len(driver.find_elements_by_xpath(locator)) == 0):
        time.sleep(0.1)


def wait_if_displayed(element1, element2, wait_time):
    count = 0
    interval = 0.1
    total_wait = wait_time / interval
    while (len(driver.find_elements_by_xpath(element1)) == 0):
        time.sleep(interval)
        count = count + 1
        if (count == total_wait):
            driver.find_element_by_xpath(element2).click()
            break


def wait_till_element_disappears(element):
    while (len(driver.find_elements_by_xpath(element)) > 0):
        time.sleep(0.1)
