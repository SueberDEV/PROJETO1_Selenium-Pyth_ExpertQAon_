import pytest
from selenium import webdriver

@pytest.fixture()
def swag():
    swag = webdriver.Chrome()
    swag.get("https://www.saucedemo.com/")
    swag.maximize_window()
    yield swag   
    swag.quit()
