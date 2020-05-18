#This file is used to list down the setup and teardown functions in the framework. The same file can be used to implement
#common steps implementation as well

import pytest
from Drivers.chromedriver import driver
from Environment.QA_challenge import credentials


@pytest.fixture(scope="session", autouse=True)
def setup_and_teardown():
    driver.get(credentials.url)
    yield
    driver.close()