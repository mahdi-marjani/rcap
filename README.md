# rcap

reCAPTCHA v2 Image Solver using YOLO with Selenium and Playwright

https://github.com/user-attachments/assets/22308be7-3a90-4757-8799-b47008b32bf0

## How it works
- Uses Selenium or Playwright from [rcap-client](https://github.com/mahdi-marjani/rcap-client) for browser interaction.
- Uses YOLO-based models from [rcap-core](https://github.com/mahdi-marjani/rcap-core) for image detection.

## Installation

Install via pip:

```
pip install rcap
```

## Usage

Selenium example:

```python
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from rcap.solver import SeleniumRecaptchaSolver

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.get("https://www.google.com/recaptcha/api2/demo")

solver = SeleniumRecaptchaSolver(driver)
solver.solve()  # Done!

print("reCAPTCHA solved!")
input("Press Enter to quit...")
driver.quit()
```

Playwright example:

```python
from playwright.sync_api import sync_playwright
from rcap.solver import PlaywrightRecaptchaSolver

playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=False)
page = browser.new_page()
page.goto("https://www.google.com/recaptcha/api2/demo")

solver = PlaywrightRecaptchaSolver(page)
solver.solve()  # Done!

print("reCAPTCHA solved!")
input("Press Enter to quit...")
page.close()
```

## Recommendation: Use Camoufox for stealthier automation

For better stealth and human-like interactions, I recommend using **Camoufox** — an anti-detect browser that simulates human cursor movement and other behaviors to help avoid bot detection.

https://github.com/user-attachments/assets/85dfcbbd-316d-4841-b20b-df5d0efea863

### Install

```bash
pip install -U camoufox
# optional but recommended if using proxies:
# pip install -U "camoufox[geoip]"
```

Download the Camoufox browser:

```bash
python -m camoufox fetch
```

### Usage with `rcap`

```python
from rcap.solver import PlaywrightRecaptchaSolver
from camoufox.sync_api import Camoufox

camoufox = Camoufox(headless=False, humanize=True)
browser = camoufox.start()
page = browser.new_page()
page.goto("https://www.google.com/recaptcha/api2/demo")

solver = PlaywrightRecaptchaSolver(page)
solver.solve()  # Done!

print("reCAPTCHA solved!")
input("Press Enter to quit...")
page.close()
```

`humanize=True` enables Camoufox's human-like cursor movement, which can significantly reduce the chance of triggering reCAPTCHA in the first place.
