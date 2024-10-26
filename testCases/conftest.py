import pytest
from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options

@pytest.fixture()  #fixture
def setup(browser):
    if browser == 'chrome':
        chrome_options = Options()
        chrome_options.add_argument("--incognito")
        #driver = webdriver.Chrome(options =chrome_options)
        driver = uc.Chrome(options=chrome_options)
        print("Launching chrome browser...")
    return driver


def pytest_addoption(parser):  #This will get the browser from command line/CLI/Hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request): # this will return the Browser value to setup method above
    return request.config.getoption("--browser")


######## PyTest HTML Report #########

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    metadata = config.pluginmanager.getplugin("metadata")
    if metadata:
        from pytest_metadata.plugin import metadata_key
        config.stash[metadata_key]['Project Name'] = 'nop Commerce'
        config.stash[metadata_key]['Module Name'] = 'Customers'
        config.stash[metadata_key]['Tester'] = 'Devarsh Patel'


# It is hook for delete/Modify Environment info to HTML Report
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)