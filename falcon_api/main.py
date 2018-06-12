import falcon
import json
from selenium import webdriver
from selenium.webdriver.firefox import options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re, json

data = {}

class GetCreditCardRewards(unittest.TestCase):
    def fetchData():
        Options = options.Options()
        Options.add_argument("--headless")
        driver = webdriver.Firefox(firefox_options=Options)
        print("web driver actually is set")
        driver.get("https://www.discover.com/credit-cards/cashback-bonus/cashback-calendar.html")
        discoverItRewards = driver.find_element_by_xpath("//*[@id=\"tab_31463\"]/a/p").text
        driver.get("https://www.citi.com/credit-cards/credit-cards-citi/citi.action?ID=dividend-quarterly-offer")
        citiRewards = driver.find_element_by_xpath("//*[@id=\"contentFirst\"]/div[1]/ul/li[2]/span[2]").text
        data['Discover'] = discoverItRewards
        data['Citi'] = citiRewards

class TestResource(object):
    def on_get(self, req, res):
        """Handles all GET requests."""
        res.status = falcon.HTTP_200  # This is the default status
        print("----------------------------")
        instance_of_class = GetCreditCardRewards.fetchData.__call__()
        json_output = data
        print(json.dumps(json_output))
        print("----------------------------")
        res.body = (json.dumps(json_output))

# Create the Falcon application object
app = falcon.API()

# Instantiate the TestResource class
test_resource = TestResource()
print("just instantiating")

# Add a route to serve the resource
app.add_route('/', test_resource)
