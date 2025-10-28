from appium.webdriver.common.appiumby import AppiumBy

def scroll_to_text(driver, text: str):
    """
    Scrolls until element with visible text is found (Android).
    """
    ui_selector = (
        'new UiScrollable(new UiSelector().scrollable(true))'
        f'.scrollIntoView(new UiSelector().text("{text}"))'
    )
    return driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, ui_selector)

def scroll_and_click_text(driver, text: str):
    el = scroll_to_text(driver, text)
    el.click()
    return el
