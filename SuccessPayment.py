import sys,os
import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from subprocess import CREATE_NO_WINDOW
 
options = Options()
options = webdriver.ChromeOptions()

BTN_Buy_Now = '//*[@id="container"]/div/div/div[1]/div[2]/div/div/a'
title_shop = '//*[@id="container"]/div/div/div[2]/div[1]/div[1]/span[1]'
BTN_checkout = '//*[@id="container"]/div/div/div[2]/div[2]/div[1]'
BTN_Pengaturan = '//*[@id="container"]/div/div/div[2]/div[2]/div[2]/img'
Title_COCOSTORE = '//*[@id="header"]/div/h1'
BTN_CONTINUE = '//*[@id="application"]/div[1]/a'
Title_Credit_debit_card = '//*[@id="payment-list"]/div[1]/a/div[2]/div[1]'
BTN_Credit_debit_card = '//*[@id="payment-list"]/div[1]/a'
Field_card_number = '//*[@id="application"]/div[3]/div/div/div/form/div[2]/div[1]/input'
Field_expire_date = '//*[@id="application"]/div[3]/div/div/div/form/div[2]/div[2]/input'
Field_CVV = '//*[@id="application"]/div[3]/div/div/div/form/div[2]/div[3]/input'
BTN_Pay_Now = '//*[@id="application"]/div[1]/a'
Field_password = 'PaRes'
BTN_OK = 'ok'
Title_success = '//*[@id="container"]/div/div/div[1]/div[2]/div/div[2]/div/span[1]'

class SuccessTest(unittest.TestCase):
  
    def setUp(self):
        self.s = Service("C:\webdriver\chromedriver")
        self.s.creationflags = CREATE_NO_WINDOW
        self.driver = webdriver.Chrome(service=self.s, options=options)
  
  #TEST SUCCESS 
    def test_success_payment(self):
        url = 'https://demo.midtrans.com/'
        self.driver.get(url)
        driver = self.driver
        self.assertEqual('Sample Store', driver.title)
        element = driver.find_element(By.XPATH,BTN_Buy_Now)
        element.click()
        element = driver.find_element(By.XPATH,title_shop)
        self.assertEqual('Shopping Cart  ', element.text)
        element = driver.find_element(By.XPATH,BTN_checkout)
        element.click()
        time.sleep(3)
        element = driver.find_element(By.ID,'snap-midtrans')
        driver.switch_to.frame(element)
        element = driver.find_element(By.XPATH,Title_COCOSTORE)
        self.assertEqual('COCO STORE', element.text)
        element = driver.find_element(By.XPATH,BTN_CONTINUE)
        element.click()
        time.sleep(1)
        element = driver.find_element(By.XPATH,BTN_Credit_debit_card)
        element.click()
        time.sleep(1)
        element = driver.find_element(By.XPATH,Field_card_number)
        element.send_keys("4811111111111114")
        element = driver.find_element(By.XPATH,Field_expire_date)
        element.send_keys("04/22")
        element = driver.find_element(By.XPATH,Field_CVV)
        element.send_keys("123")
        element = driver.find_element(By.XPATH,BTN_Pay_Now)
        element.click()
        time.sleep(4)
        driver.switch_to.frame(0)
        element = driver.find_element(By.XPATH,'//*[@id="PaRes"]')
        element.send_keys("112233")
        element = driver.find_element(By.NAME,BTN_OK)
        element.click()
        time.sleep(8)
        driver.switch_to.default_content()
        element = driver.find_element(By.XPATH,Title_success)
        self.assertEqual('Thank you for your purchase.', element.text)
        

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
  unittest.main()