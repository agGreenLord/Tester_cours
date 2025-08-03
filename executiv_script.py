from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link = "https://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
  value = browser.find_element(By.ID, "input_value")
  answer = calc(int(value.text))

  form = browser.find_element(By.CLASS_NAME, 'form-control')
  #browser.execute_script('return argument[0].scrollIntoView(true)', form)
  form.send_keys(answer)

  checkbox = browser.find_element(By.ID, 'robotCheckbox')
  #browser.execute_script('return argument[0].scrollIntoView(true)', checkbox)
  checkbox.click()

  radio = browser.find_element(By.ID, 'robotsRule')
  browser.execute_script('return arguments[0].scrollIntoView(true)', radio)
  radio.click()

  button = browser.find_element(By.CLASS_NAME, 'btn')
  browser.execute_script('return arguments[0].scrollIntoView(true)', button)
  button.click()

finally:
  time.sleep(5)
  browser.quit()
