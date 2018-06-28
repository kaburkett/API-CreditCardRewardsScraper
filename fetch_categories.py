from selenium import webdriver
from selenium.webdriver.firefox import options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re, json
import sqlite3

def updateCategories(bank, category):
    print("grabbing and attempting to write to db")
    print(bank + " | "+ category)
    sqlite_file = 'database.db'
    # Connecting to the database file
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    # C) Updates the newly inserted or pre-existing entry            
    c.execute("UPDATE 'categories' SET 'category'=category WHERE 'bank'=bank")
    try:
        conn.commit()
    except:
        print("error occurred when trying to update")
    conn.close()

data = {}

class GetCreditCardRewards(unittest.TestCase):
    Options = options.Options()
    Options.add_argument("--headless")
    driver = webdriver.Firefox(firefox_options=Options)
    print("web driver actually is set")
    driver.get("https://www.discover.com/credit-cards/cashback-bonus/cashback-calendar.html")
    discoverItRewards = driver.find_element_by_xpath("//*[@id=\"tab_31463\"]/a/p").text
    driver.get("https://www.citi.com/credit-cards/credit-cards-citi/citi.action?ID=dividend-quarterly-offer")
    citiRewards = driver.find_element_by_xpath("//*[@id=\"contentFirst\"]/div[1]/ul/li[2]/span[2]").text
    #data['Discover'] = discoverItRewards
    updateCategories('Discover', discoverItRewards)
    updateCategories('Citi', citiRewards)
    #data['Citi'] = citiRewards

    
if __name__ == "__main__":
    unittest.main()