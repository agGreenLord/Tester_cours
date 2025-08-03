import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class TastAbs(unittest.TestCase):
    def test_registration1(self):
        self.link = "https://suninjuly.github.io/registration1.html"
        self.browser = webdriver.Chrome()
        self.browser.get(self.link)
        input1 = self.browser.find_element(By.CLASS_NAME, "first")
        input1.send_keys("Ivan")
        input2 = self.browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your last name']")
        input2.send_keys("Petrov")
        input3 = self.browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your email']")
        input3.send_keys("dad@gmail.ru")
        button = self.browser.find_element(By.CSS_SELECTOR, "[type='submit']")
        button.click()
        
        self.browser.implicitly_wait(2)
        self.ver_str = self.browser.find_element(By.TAG_NAME, "h1")

        self.assertEqual(self.ver_str, "Congratulations! You have successfully registered!", "NON REGISTRATION FINISH")

    def test_registration2(self):
        self.link = "https://suninjuly.github.io/registration2.html"
        self.browser = webdriver.Chrome()
        self.browser.get(self.link)
        input1 = self.browser.find_element(By.CLASS_NAME, "first")
        input1.send_keys("Ivan")
        input2 = self.browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your last name']")
        input2.send_keys("Petrov")
        input3 = self.browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your email']")
        input3.send_keys("dad@gmail.ru")
        button = self.browser.find_element(By.CSS_SELECTOR, "[type='submit']")
        button.click()
        self.assertEqual()
    


if __name__ == "__main__":
    unittest.main()