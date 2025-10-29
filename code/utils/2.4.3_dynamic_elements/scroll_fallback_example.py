"""
Пример 2. Подход scroll-to-click как fallback-решение
Когда элемент не найден на экране, выполняется прокрутка до него.
"""

from appium.webdriver.common.appiumby import AppiumBy

def scroll_and_click(driver, text: str):
    """
    Прокрутка до элемента с указанным текстом и клик.
    """
    ui_selector = (
        'new UiScrollable(new UiSelector().scrollable(true))'
        f'.scrollIntoView(new UiSelector().text("{text}"))'
    )
    element = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, ui_selector)
    element.click()
    return element
