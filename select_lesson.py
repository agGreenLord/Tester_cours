from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time



link = "https://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

try:

    num1_chek = browser.find_element(By.ID, 'num1')
    num1 = num1_chek.text
    num2_chek = browser.find_element(By.ID, 'num2')
    num2 = num2_chek.text
   
    answer = int(num1) + int(num2)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    seletion = select.select_by_value(str(answer))

    browser.find_element(By.CLASS_NAME, 'btn').click()

finally:
    time.sleep(10)
    browser.quit()


