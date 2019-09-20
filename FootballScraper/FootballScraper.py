#!python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import bs4

file = open("C:\\Users\\tsahli\\Documents\\selenium\\cbspass.txt", "r")
lines = file.readlines()
username = lines[0]
password = lines[1]

driver = webdriver.Firefox()
driver.get("https://www.cbssports.com/login?product_abbrev=opm&xurl=http%3A%2F%2Ftaylorelectricoffice.football.cbssports.com%2Foffice-pool%2Fstandings%2Flive&master_product=26040")
usernameField = driver.find_element_by_id("userid")
passwordField = driver.find_element_by_id("password")
usernameField.send_keys(username)
passwordField.send_keys(password)
driver.find_element_by_name("_submit").click()

currentPage = driver.page_source()
print(currentPage)






driver.quit()

