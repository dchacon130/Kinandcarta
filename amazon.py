from cmath import log
from lib2to3.pgen2 import driver
import time
import unittest
import HtmlTestRunner

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


class Login(unittest.TestCase):

    @classmethod
    def setUp(cls) -> None:
        
        cls.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        cls.driver.get('https://www.amazon.com/')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
    
    def test_search_by_Alexa(self):
        
        self.driver.find_element(By.ID, "twotabsearchtextbox").send_keys('Alexa')
        self.driver.find_element(By.ID, "nav-search-submit-button").click()

        time.sleep(5)
        self.driver.find_element(By.XPATH, "//a[@class='s-pagination-item s-pagination-button'][contains(text(),'2')]").click() 

        time.sleep(10)

        entries = self.driver.find_elements(By.XPATH, "//span[@class = 'a-size-medium a-color-base a-text-normal']")

        print(len(entries))
        entries[2].click()


        if self.driver.find_element(By.ID, "add-to-cart-button").is_displayed():
            self.driver.find_element(By.ID, "add-to-cart-button").click()
            time.sleep(3)
            carNumber = self.driver.find_element(By.ID, "nav-cart-count").text
            print(carNumber)
        else:
            noProduct = self.driver.find_element(By.XPATH, '//*[@id="outOfStock"]/div/div[1]/span[1]').text
            print(noProduct)
            self.assertEqual('No disponible por el momento.', noProduct, 'No hay cantidades de este producto por el momento.')
            print('No hay cantidades de este producto por el momento.')
        

        
    @classmethod
    def tearDown(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
        print('Test Completed')
  
    

if __name__ == '__main__':
	unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='Results'))