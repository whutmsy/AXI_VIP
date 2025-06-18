#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("user-agent=Mozilla/5.0...")
driver = webdriver.Chrome(options=options)

try:
    driver.get("https://ddys.pro/category/movie/western-movie/page/0")
    print("页面标题:", driver.title)
finally:
    driver.quit()