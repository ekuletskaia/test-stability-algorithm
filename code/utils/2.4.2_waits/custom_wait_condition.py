"""
Пример 3. Кастомное ожидание
Создание собственного условия ожидания, например, когда элемент становится видимым и содержит текст.
"""

from selenium.webdriver.support.ui import WebDriverWait

def custom_wait_condition(driver, locator, expected_text, timeout=10):
    """Ожидание, пока элемент станет видимым и его текст совпадёт с ожидаемым."""
    WebDriverWait(driver, timeout).until(
        lambda d: (el := d.find_element(*locator)) and el.is_displayed() and el.text == expected_text,
        message=f"Элемент {locator} не содержит ожидаемый текст: {expected_text}"
    )
