import pytest
from pages.home_page import HomePage
from pages.auth_page import AuthPage
from utils.storefront import open_storefront
from utils.test_data import make_customer
import time
import logging

@pytest.mark.usefixtures("driver")
def test_registration_login(driver):
    # Open ephemeral PrestaShop storefront
    open_storefront(driver)

    # Initialize home page
    home = HomePage(driver)
    home.goto_signin()

    # Initialize auth page and create a new customer
    auth = AuthPage(driver)
    auth.goto_registration()
    customer = make_customer()
    auth.register(customer)
    time.sleep(5)
    # Verify user is logged in
    assert home.is_logged_in(), "User should be logged in after registration"
    logging.info("Logged In automatically after registration")

    # Log out and verify logged out
    home.signout()
    assert home.is_logged_out(), "User should be logged out after sign out"
    logging.info("User signed out to prepare for login and registration test")
    time.sleep(2)
    # Login with the same user and verify logged in
    home.goto_signin()
    auth.login(customer["email"], customer["password"])
    time.sleep(2)
    assert home.is_logged_in(), "User should be logged in after login"
    logging.info("Successfully logged in with existing customer")
