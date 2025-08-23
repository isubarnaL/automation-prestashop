from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)


    def wait_for(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))


    def click(self, locator):
        self.wait_for(locator).click()


    def fill(self, locator, text):
        el = self.wait_for(locator)
        el.clear()
        el.send_keys(text)


    def get_text(self, locator):
        return self.wait_for(locator).text