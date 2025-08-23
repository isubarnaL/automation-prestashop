from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def goto_signin(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".user-info a"))
        ).click()

    def signout(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Sign out"))
        ).click()

    def is_logged_in(self):
        return "Sign out" in self.driver.page_source

    def is_logged_out(self):
        return "Sign in" in self.driver.page_source

    def open_first_product(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "article.product-miniature a"))
        ).click()
