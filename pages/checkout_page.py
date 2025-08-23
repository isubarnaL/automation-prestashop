from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import logging

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    # ---------------- LOCATORS ----------------
    product_locator = (By.CSS_SELECTOR, ".product-miniature a")
    add_to_cart_locator = (By.CSS_SELECTOR, ".btn.btn-primary.add-to-cart")
    modal_checkout_btn = (By.CSS_SELECTOR, "#blockcart-modal .btn.btn-primary")
    cart_checkout_btn = (By.CSS_SELECTOR, ".cart-detailed-actions a.btn.btn-primary")

    address1_locator = (By.NAME, "address1")
    city_locator = (By.NAME, "city")
    state_locator = (By.NAME, "id_state")
    postcode_locator = (By.NAME, "postcode")
    confirm_address_locator = (By.NAME, "confirm-addresses")

    confirm_shipping_locator = (By.NAME, "confirmDeliveryOption")
    pay_by_check_locator = (By.CSS_SELECTOR, "#payment-option-1")
    terms_checkbox_locator = (By.CSS_SELECTOR, ".js-terms")
    place_order_btn_locator = (By.CSS_SELECTOR, "#payment-confirmation button")

    # ---------------- METHODS ----------------
    def set_quantity(self, qty):
        try:
            qty_elem = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.NAME, "qty"))
            )
            # Clear existing value
            qty_elem.clear()
            qty_elem.send_keys(str(qty))
            logging.info(f"Quantity set to {qty}")
        except TimeoutException:
            logging.error("Quantity input field not found on the page")
            assert False, "Quantity input not available"

    def is_stock_warning_displayed(self):
        try:
            self.driver.find_element(By.CSS_SELECTOR, ".js-product-availability")
            logging.info("Stock warning is displayed")
            return True
        except:
            logging.info("No stock warning displayed")
            return False

    def select_first_product(self):
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.product_locator)
        ).click()
        logging.info("Opened first product details page")

    def add_product_to_cart(self):
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.add_to_cart_locator)
        ).click()
        logging.info("Product added to cart")

    def go_to_checkout_from_modal(self):
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.modal_checkout_btn)
        ).click()
        logging.info("Navigated to checkout page from modal")

    def proceed_from_cart_page(self):
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.cart_checkout_btn)
        ).click()
        logging.info("Navigated to Addresses section")

    def fill_address(self, address):
        try:
            address1 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.address1_locator)
            )
            address1.clear()
            address1.send_keys(address["address1"])

            city = self.driver.find_element(*self.city_locator)
            city.clear()
            city.send_keys(address["city"])

            state_dropdown = Select(self.driver.find_element(*self.state_locator))
            state_dropdown.select_by_index(1)  # pick first valid state

            postcode = self.driver.find_element(*self.postcode_locator)
            postcode.clear()
            postcode.send_keys(address["postcode"])

            logging.info("Address filled successfully")
        except Exception:
            logging.info("Address already exists, skipping")

    def confirm_address(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.confirm_address_locator)
        ).click()
        logging.info("Confirmed address")

    def confirm_shipping(self):
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.confirm_shipping_locator)
        ).click()
        logging.info("Confirmed shipping method")

    def choose_payment_check(self):
        try:
            payment_option = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='payment-option'][value='payment_check']"))
            )
            payment_option.click()
            logging.info("Selected payment by check")
        except TimeoutException:
            logging.error("Payment option not available on checkout page")

    def agree_to_terms(self):
        checkbox = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.terms_checkbox_locator)
        )
        checkbox.click()
        logging.info("Agreed to terms and conditions")

    def place_order(self):
            btn = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.place_order_btn_locator)
            )
            if not btn.is_enabled():
                logging.error("Place Order button is disabled")
                assert False, "Place Order button is disabled "
            btn.click()
    
