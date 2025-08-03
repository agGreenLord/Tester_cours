import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    box = browser.find_element(By.ID, 'treasure')
    box_value = box.get_attribute('valuex')

    x = calc(box_value)

    string = browser.find_element(By.ID, 'answer')
    string.send_keys(x)

    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    radio = browser.find_element(By.ID, "robotsRule")
    radio.click()

    button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]' )
    button.click()

finally:
    time.sleep(10)
    browser.quit()