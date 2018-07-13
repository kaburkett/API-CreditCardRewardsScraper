from selenium import webdriver
from selenium.webdriver.firefox import options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re, json
import sqlite3
from datetime import datetime

def updateCategories(bank, category):
    print("grabbing and attempting to write to db")
    print(bank + " | "+ category)
    sqlite_file = 'database.db'
    # Connecting to the database file
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    # C) Updates the newly inserted or pre-existing entry            
    c.execute('UPDATE "categories" SET category= ? WHERE "bank"= ?', (category, bank))
    try:
        conn.commit()
    except:
        print("error occurred when trying to update")
    conn.close()

data = {}

class GetCreditCardRewards(unittest.TestCase):
    #boot webdriver
    Options = options.Options()
    Options.add_argument("--headless")
    driver = webdriver.Firefox(firefox_options=Options)
    #find current rewards categories
    driver.get("https://www.discover.com/credit-cards/cashback-bonus/cashback-calendar.html")
    discoverItRewards = driver.find_element_by_css_selector(".offer-enroll .offer-name").text
    driver.get("https://www.citi.com/credit-cards/credit-cards-citi/citi.action?ID=dividend-quarterly-offer")
    citiRewardsList = driver.find_elements_by_css_selector(".selectedProductRow .descriptions")
    citi = ""
    for citiRewards in citiRewardsList:
        if citi == "":
            citi = citiRewards.text
        else: citi = citi + " and " + citiRewards.text
    #chase is harder because they are all images so it has to be done by quarter and alt text
    currentMonth = datetime.now().month
    currentQuarter = (currentMonth-1)//3
    driver.get("https://creditcards.chase.com/freedom/calendar")
    chaseRewardsList = driver.find_elements_by_css_selector(".quarter-box-wrapper .quarter-box")
    chase = chaseRewardsList[currentQuarter].find_element_by_css_selector("img")
    chase = chase.get_attribute("alt")

    #write to sqllite
    updateCategories('Discover', discoverItRewards)
    updateCategories('Citi', citi)
    updateCategories('Chase', chase)

    
if __name__ == "__main__":
    unittest.main()