import pytest
from selenium import webdriver
import undetected_chromedriver as uc

@pytest.fixture
def setup(browser):
    if browser == 'chrome':
        options = uc.ChromeOptions()
        options.add_argument("--start-maximized")  # optional
        driver = uc.Chrome(options=options)
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Ie()
    yield driver
    driver.quit()
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")

# conftest.py

def pytest_configure(config):
    metadata = config.pluginmanager.getplugin("metadata")
    if metadata:
        from pytest_metadata.plugin import metadata_key
        config.stash[metadata_key]['Project Name'] = 'nop Commerce'
        config.stash[metadata_key]['Module Name'] = 'Customers'
        config.stash[metadata_key]['Tester'] = 'Ree'

@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)