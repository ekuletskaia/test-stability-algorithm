"""
Переиспользуемые обёртки ожиданий для поиска и взаимодействия с элементами.
Относятся к разделу 2.4.1 статьи:
«Стабилизация локаторов и переиспользуемые методы поиска».
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_find_element(driver, locator, timeout=10):
    """Waits until a single element is present in the DOM."""
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located(locator),
        message=f"Element {locator} not found"
    )

def wait_and_click(driver, locator, timeout=10):
    """Waits until the element is clickable and performs a click."""
    element = WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(locator),
        message=f"Element {locator} not clickable"
    )
    element.click()
    return element

def wait_find_all_elements(driver, locator, timeout=10):
    """Waits until at least one matching element appears and returns all found."""
    WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located(locator),
        message=f"No elements found for {locator}"
    )
    return driver.find_elements(*locator)
