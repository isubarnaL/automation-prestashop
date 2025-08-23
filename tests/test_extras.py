import pytest
import time
import logging
from pages.home_page import HomePage
from pages.auth_page import AuthPage
from pages.checkout_page import CheckoutPage
from utils.storefront import open_storefront
from utils.test_data import make_customer
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("driver")
def test_max_quantity_out_of_stock(driver):
    """Verify if setting an excessive quantity triggers out-of-stock message."""
    # Open ephemeral PrestaShop storefront
    open_storefront(driver)
    logging.info("Opened PrestaShop storefront")

    # Initialize home page
    home = HomePage(driver)
    home.goto_signin()
    logging.info("Navigated to Sign In page")

    # Initialize auth page and register a customer
    auth = AuthPage(driver)
    customer = make_customer()
    auth.goto_registration()
    auth.register(customer)
    time.sleep(2)
    assert home.is_logged_in(), "User should be logged in after registration"
    logging.info("Customer registered and logged in")

    checkout = CheckoutPage(driver)
    checkout.select_first_product()

    # Set quantity to 1000
    checkout.set_quantity(1000)
    # Try adding to cart
    checkout.add_product_to_cart()

     # Verify the stock warning is displayed
    assert checkout.is_stock_warning_displayed(), "Expected stock warning not shown"