"""
Пример 1. Работа со стабильными идентификаторами
Использование content-desc и data-testid вместо текстовых локаторов.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def find_stable_element(driver, timeout=10):
    """
    Демонстрация поиска динамического элемента через стабильные атрибуты.
    """
    # предпочтительно использовать resource-id или content-desc
    locator = (By.ACCESSIBILITY_ID, "menu_profile")  # content-desc="menu_profile"
    element = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located(locator),
        message="Элемент с content-desc='menu_profile' не найден"
    )
    return element
