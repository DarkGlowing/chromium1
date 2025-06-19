from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()

# ОБНОВЛЁННЫЙ путь — важно!
chrome_options.add_argument("user-data-dir=/root/.config/chromium")
chrome_options.add_argument("profile-directory=Default")

# Необязательные настройки
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--no-first-run")
chrome_options.add_argument("--no-default-browser-check")

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://idx.google.com/host-61180269")

input("Нажми Enter, чтобы закрыть браузер...")

