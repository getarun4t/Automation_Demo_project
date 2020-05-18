import pytest
from Drivers.chromedriver import driver
from Environment.QA_challenge import credentials


@pytest.fixture(scope="session", autouse=True)
def setup_and_teardown():
    driver.get(credentials.url)
    yield
    driver.close()