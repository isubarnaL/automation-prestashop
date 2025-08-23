import pytest
import logging
import time
from pages.home_page import HomePage
from pages.auth_page import AuthPage
from pages.checkout_page import *
from utils.storefront import open_storefront
from utils.test_data import make_customer


@pytest.mark.usefixtures("driver")
def test_purchase_flow(driver):
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

    # Product selection & cart
    checkout.select_first_product()
    time.sleep(1)
    checkout.add_product_to_cart()
    time.sleep(3)
    checkout.go_to_checkout_from_modal()
    time.sleep(3)
    checkout.proceed_from_cart_page()
    time.sleep(2)

    # Address & shipping
    checkout.fill_address(customer["address"])
    checkout.confirm_address()
    checkout.confirm_shipping()

    # Payment & place order
    checkout.choose_payment_check()
    checkout.agree_to_terms()
    checkout.place_order()
