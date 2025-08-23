from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AuthPage:
    def __init__(self, driver):
        self.driver = driver

    def register(self, customer):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "firstname"))
        ).send_keys(customer["first"])
        self.driver.find_element(By.NAME, "lastname").send_keys(customer["last"])
        self.driver.find_element(By.NAME, "email").send_keys(customer["email"])
        self.driver.find_element(By.NAME, "password").send_keys(customer["password"])
        self.driver.find_element(By.NAME, "customer_privacy").click()
        self.driver.find_element(By.NAME, "psgdpr").click()
        self.driver.find_element(By.CLASS_NAME, "form-control-submit").click()

    def login(self, email, password):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "field-email"))
        ).send_keys(email)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.ID, "submit-login").click()

    def goto_registration(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".no-account a"))
        ).click()

