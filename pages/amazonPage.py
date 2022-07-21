import unittest
import configparser
import HtmlTestRunner

from selenium import webdriver
from locators.locators import *
from selenium.webdriver.common.by import By



class AmazonPage:
    def __init__(self, driver) -> None:
        self.driver = driver

        self.SearchBoxBy_Id = Locators.SearchBoxBy_Id
        self.ButtonSearch_Id = Locators.ButtonSearch_Id
        self.PageLink_LinkText = Locators.PageLink_LinkText
        self.RowProduct_Xpath = Locators.RowProduct_Xpath
        self.ButtonAddCart_Id = Locators.ButtonAddCart_Id
        self.LabelCarQuantity_Id = Locators.LabelCarQuantity_Id
        self.LabelStock_Xpath = Locators.LabelStock_Xpath
    
    def insert_text_to_search_bar(self, text):
        config = configparser.ConfigParser()
        config.read('configuracion.ini')
        self.browser = config['Browser']['Chrome']
        self.website = config['Website']['Page']
        self.driver = webdriver.Chrome(executable_path= self.browser)
        self.driver.get(self.website)
        self.driver.maximize_window()

        self.driver.find_element(By.ID, self.SearchBoxBy_Id).clear()
        self.driver.find_element(By.ID, self.SearchBoxBy_Id).send_keys(text)

    def click_button_search(self):
        self.driver.find_element(By.ID, self.ButtonSearch_Id).click()

    def click_on_the_page_number(self):
        self.driver.find_element(By.LINK_TEXT, self.PageLink_LinkText).click()

    def select_the_product(self, entry):
        entries = self.driver.find_elements(By.XPATH, self.RowProduct_Xpath)
        entries[entry].click()
        return entries

    def add_cart_button_exist(self):
        if self.driver.find_element(By.ID, self.ButtonAddCart_Id).is_displayed():
            self.driver.find_element(By.ID, self.ButtonAddCart_Id).click()
            carNumber = self.driver.find_element(By.ID, self.LabelCarQuantity_Id).text
            return carNumber
        else:
            noProduct = self.driver.find_element(By.XPATH, self.LabelCarQuantity_Id).text
            return noProduct

if __name__ == '__main__':
	unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='Results'))