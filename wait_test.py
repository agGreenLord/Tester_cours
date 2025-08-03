from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui  import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
  browser.implicitly_wait(5)
  
  button = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "$100")
  )
  browser.find_element(By.ID, 'book').click()

  #x = WebDriverWait(browser, 10).until(EC.visibility_of_element_located(By.ID, "input_value"))
  x = browser.find_element(By.ID, 'input_value')

  answer = calc(x.text)
  text = browser.find_element(By.ID, 'answer')
  text.send_keys(answer)

  sub_button = browser.find_element(By.CSS_SELECTOR, '[type = "submit"]')
  sub_button.click()

finally:
  time.sleep(5)
  browser.quit()
