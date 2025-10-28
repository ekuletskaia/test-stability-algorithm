# Appium Configuration

This document describes how to configure and run Appium for reproducing the stability optimization experiment.

1. Install Appium version 2.x: npm install -g appium
2. Check the installation:
   appium -v
   appium doctor
3. For local runs — use `capabilities-local.json`
4. For cloud runs (BrowserStack) — use `capabilities-browserstack.json`
5. Default Appium endpoint: http://127.0.0.1:4723/wd/hub

## 1. Capabilities files
Two example configuration files are provided in this repository:
- `capabilities-local.json` — for local emulator or physical device.
- `capabilities-browserstack.json` — for running tests in the BrowserStack cloud.

Use these files as templates and replace placeholder values (`appPackage`, `appActivity`, or `app-id`) with your own.

## 2. Local run example
Example command for local Appium session:
```python
from appium import webdriver

with open("env/capabilities-local.json") as f:
    caps = json.load(f)

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
```

## 3. BrowserStack run
Replace YOUR_USERNAME and YOUR_ACCESS_KEY with your BrowserStack credentials.
```python
from appium import webdriver

with open("env/capabilities-browserstack.json") as f:
    caps = json.load(f)

BROWSERSTACK_URL = "https://YOUR_USERNAME:YOUR_ACCESS_KEY@hub-cloud.browserstack.com/wd/hub"

driver = webdriver.Remote(BROWSERSTACK_URL, caps)
```
