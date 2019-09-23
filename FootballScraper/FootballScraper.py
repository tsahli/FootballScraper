#!python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import yagmail

passFile = open("C:\\Users\\tsahli\\Documents\\selenium\\cbspass.txt", "r")
lines = passFile.readlines()
username = lines[0]
password = lines[1]

emailList = []
emailFile = open("C:\\Users\\tsahli\\Documents\\selenium\\emails.txt", "r")
emailLines = emailFile.readlines()
for line in emailLines:
    if not None:
        emailList.append(line)

driver = webdriver.Firefox()
driver.get("https://www.cbssports.com/login?product_abbrev=opm&xurl=http%3A%2F%2Ftaylorelectricoffice.football.cbssports.com%2Foffice-pool%2Fstandings%2Flive&master_product=26040")
usernameField = driver.find_element_by_id("userid")
passwordField = driver.find_element_by_id("password")
usernameField.send_keys(username)
passwordField.send_keys(password)
driver.find_element_by_name("_submit").click()

driver.maximize_window()
element = driver.find_element_by_id("nflheader")
driver.execute_script("arguments[0].scrollIntoView();", element)
driver.save_screenshot("picks.png")

driver.get("http://taylorelectricoffice.football.cbssports.com/office-pool/standings")
driver.find_element_by_id("btnPrint").click()
driver.save_screenshot("standings.png")

picksScreenshot = ".\\picks.png"
standingsScreenshot = ".\\standings.png"
yag = yagmail.SMTP('tspythonprojects@gmail.com')
contents = ["Attached are this weeks picks and standings.", picksScreenshot, standingsScreenshot]
yag.send(to=emailList, subject='This Weeks NFL Picks', contents=contents)

driver.quit()

