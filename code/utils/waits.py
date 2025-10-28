from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_find_element(driver, locator, timeout=10):
    WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located(locator),
        message=f"Element {locator} not found"
    )
