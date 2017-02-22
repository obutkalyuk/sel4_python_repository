import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd

def wait(driver):
    wait = WebDriverWait(driver, 10)
    return wait

def test_example(driver):
    driver.get("http://localhost/litecart/admin/login.php")
    CorrectLogin(driver, "admin", "admin")


def CorrectLogin(driver, user, password):
    usernameInput = driver.find_element_by_name("username")
    passwordInput = driver.find_element_by_name("password")
    loginButton = driver.find_element_by_name("login")
    usernameInput.send_keys(user)
    passwordInput.send_keys(password)
    loginButton.click()
    address = driver.current_url
    address == "http://localhost/litecart/admin/"

