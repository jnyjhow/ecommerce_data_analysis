from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

import sys

python_version = sys.version
print(f"Versão do Python: {python_version}")

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# options.add_argument("--start-maximized")
# options.add_argument("--enable-automation")
# options.add_argument("--disable-infobars")
# options.add_argument("--disable-browser-side-navigation")
# options.add_argument("--remote-debugging-port=9230")
# options.add_argument("--disable-gpu")
# options.add_argument("--log-level=3")

chromedriver_path = "drivers/chromedriver"
service = Service(executable_path=chromedriver_path)
driver = webdriver.Chrome(service=service, options=options)
# driver = webdriver.Chrome(options=options)

driver.get("https://www.google.com")
print(f"Título da página: {driver.title}")
driver.save_screenshot("google_screenshot.png")

driver.quit()
