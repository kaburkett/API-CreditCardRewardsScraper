# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re, json

class GetCreditCardRewards(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.kyleburkett.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_get_credit_card_rewards(self):
        driver = self.driver
        driver.get("https://www.discover.com/credit-cards/cashback-bonus/cashback-calendar.html")
        discoverItRewards = driver.find_element_by_xpath("//*[@id=\"tab_31463\"]/a/p").text
        driver.get("https://www.citi.com/credit-cards/credit-cards-citi/citi.action?ID=dividend-quarterly-offer")
        citiRewards = driver.find_element_by_xpath("//*[@id=\"contentFirst\"]/div[1]/ul/li[2]/span[2]").text
        data = {}
        data['Discover'] = discoverItRewards
        data['Citi'] = citiRewards
        json_data = json.dumps(data)
        print(json_data)
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
