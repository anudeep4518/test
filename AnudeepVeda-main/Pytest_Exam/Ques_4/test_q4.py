import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest
import pytest_html
from time import sleep

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com")
    #sleep(5)
    return driver

def login(setup,uname,psd):
    un = setup.find_element(By.ID,"user-name")
   # uname = "standard_user"
    un.send_keys(uname)
    pwd = setup.find_element(By.ID,"password")
    #psd = "secret_sauce"
    pwd.send_keys(psd)
    setup.find_element(By.ID,"login-button").click()
    sleep(5)
    try:
        res = setup.find_element(By.XPATH,"/html/body/div/div/div/div[1]/div[2]/span").text
        if res == 'Products':
            return True
    except(Exception):
        log = logging.getLogger()
        log.info("NO such element exception")
        return False



def test_login(setup):
    log = logging.getLogger()
    log.info("testing for login")
    res = login(setup,"standard_user","secret_sauce")
    assert res == True
    log.info("login successful")

def test_login2(setup):
    log = logging.getLogger()
    log.info("testing for login")
    res = login(setup,"std_user","seceeretsauce")
    assert res == True
    log.info("login failed")

def add_to_cart_page(setup):
    login(setup,"standard_user", "secret_sauce")
    setup.find_element(By.ID,"add-to-cart-sauce-labs-bike-light").click()
    c = setup.find_element(By.CLASS_NAME,"shopping_cart_link").text
    if int(c) > 0:
        return True
    else:
        return False
def test_cart(setup):
    res = add_to_cart_page(setup)
    assert res == True
#def remove(setup):
    #setup.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
    setup.find_element(By.ID,"remove-sauce-labs-bike-light").click()
    c = setup.find_element(By.CLASS_NAME, "shopping_cart_link").text
    assert int(c) == 0

def pytest_html_report_title(report):
    report.title="q4.html"