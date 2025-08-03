import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/math.html")

    x = browser.find_element(By.CSS_SELECTOR, "#input_value")
    y = calc(x.text)

    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(y)

    chek = browser.find_element(By.ID, "robotCheckbox")
    chek.click()

    radio = browser.find_element(By.ID, "robotsRule")
    radio.click()

    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()

finally:
   time.sleep(10)
   browser.quit()