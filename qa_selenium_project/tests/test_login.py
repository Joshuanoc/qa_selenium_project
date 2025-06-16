from selenium import webdriver
from pages.login_page import LoginPage
import time

def test_login():
    driver = webdriver.Chrome()
    driver.get("https://example.com/login")

    login = LoginPage(driver)
    login.enter_username("user123")
    login.enter_password("pass123")
    login.click_login()

    time.sleep(2)
    assert "Dashboard" in driver.title
    driver.quit()
