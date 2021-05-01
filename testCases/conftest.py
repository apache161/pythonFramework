from selenium import webdriver
import pytest
import pytest_html
import os
import sys
import pkg_resources

@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver=webdriver.Chrome(executable_path="C:\\Users\\syede\\Downloads\\Learning\\Drivers\\chromedriver.exe")
        print("Launching Chrome browser")
    else:
        driver = webdriver.Edge(executable_path="C:\\Users\\syede\\Downloads\\Learning\\Drivers\\msedgedriver.exe")
        print("launching Edge browser")
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


##HTML Reporting
def pytest_configure(config):
    config._metadata['Project Name'] = 'Sample Demo'
    config._metadata['Module Name'] = 'Sample Module'
    config._metadata['Tester'] = 'Imran'


@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)


