# pytest-style demo test (template)
# run with: pytest -q

from appium import webdriver
import json
from code.utils.waits import wait_find_element, wait_and_click
from code.utils.scroll import scroll_to_text
from code.utils.retry_strategy import flaky_retry

def create_driver(caps_path="env/capabilities-local.json", endpoint="http://127.0.0.1:4723/wd/hub"):
    with open(caps_path) as f:
        caps = json.load(f)
    return webdriver.Remote(endpoint, caps)

@flaky_retry(max_retries=2, delay_sec=1.0)
def test_example_template():
    driver = create_driver()
    try:
        # пример: дождаться и кликнуть по элементу
        el = wait_find_element(driver, by="id", value="login_button")
        wait_and_click(driver, by="id", value="login_button")

        # пример: прокрутить до текста и кликнуть
        scroll_to_text(driver, "Login")
    finally:
        driver.quit()
