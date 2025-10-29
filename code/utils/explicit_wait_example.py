"""
Пример 1. Явное ожидание (Explicit Wait)
Наиболее надёжный способ дождаться появления элемента на странице.
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def explicit_wait_example(driver, locator, timeout=10):
    """Ожидание появления элемента."""
    element = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located(locator),
        message=f"Элемент {locator} не найден"
    )
    return element
