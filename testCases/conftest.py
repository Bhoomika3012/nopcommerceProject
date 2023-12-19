from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):

    if browser == 'Edge':
        driver = webdriver.Edge()
        print("Launching Edge browser.........")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching firefox browser.........")
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")