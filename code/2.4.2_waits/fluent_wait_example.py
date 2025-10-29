"""
Пример 2. Гибкое ожидание (Fluent Wait)
Позволяет задать частоту опроса и игнорируемые исключения.
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

def fluent_wait_example(driver, locator, timeout=15, poll_frequency=1):
    """Ожидание с периодическим опросом (polling)."""
    wait = WebDriverWait(driver, timeout, poll_frequency, ignored_exceptions=[NoSuchElementException])
    element = wait.until(lambda d: d.find_element(*locator))
    return element
