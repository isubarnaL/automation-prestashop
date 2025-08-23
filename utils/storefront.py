from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def open_storefront(driver, base_url="https://demo.prestashop.com/#/en/front"):
    driver.get(base_url)

    # Wait for the iframe to appear
    iframe = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "framelive"))
    )

    # Switch into the iframe
    driver.switch_to.frame(iframe)

    # Wait for a known element in the storefront to ensure it’s loaded
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "header#header"))
    )

    return driver.current_url
