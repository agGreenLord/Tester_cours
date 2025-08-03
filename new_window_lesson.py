from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link = "https://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
  browser.find_element(By.CLASS_NAME, 'trollface').click()
  new_window = browser.window_handles[1]
  browser.switch_to.window(new_window)
  
  x = browser.find_element(By.CSS_SELECTOR, "#input_value")
  y = calc(x.text)

  answer = browser.find_element(By.ID, 'answer')
  answer.send_keys(y)

  button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
  button.click()


finally:
  time.sleep(5)
  browser.quit()