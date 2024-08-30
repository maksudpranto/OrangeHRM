import pytest
from pytest_metadata.plugin import metadata_key
from selenium import webdriver

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver


def pytest_configure(config):
    config.stash[metadata_key] ['Project Name'] = "nop Ecommerce"
    config.stash[metadata_key]['Test Performed By'] = "Md Maksud Hossain"

@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop('JAVA HOME',None)
    metadata.pop('Plugins',None)
    metadata.pop('Packages',None)