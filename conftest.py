import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="function")
def driver():
    # Setup Chrome options
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")  # Start maximized

    # Suppress ChromeDriver logs (like DEPRECATED_ENDPOINT)
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    # Initialize WebDriver
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    yield driver   # Provide the driver to the test

    driver.quit()  # Teardown
