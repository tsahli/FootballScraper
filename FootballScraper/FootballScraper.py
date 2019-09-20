#!python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import bs4
import yagmail
import csv

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

currentPage = driver.page_source
soup = bs4.BeautifulSoup(currentPage, "lxml")
rows = soup.findAll("tr", {'class' : ["bg2","bgFan"]})

picks = []
for row in rows:
    thisPick = []
    cells = row.findChildren("td")
    for cell in cells:
        thisPick.append(cell.get_text())
    picks.append(thisPick)

with open('picks.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(picks)

emailAttachment = ".\\picks.csv"
yag = yagmail.SMTP('tspythonprojects@gmail.com')
contents = ["Attached are this weeks picks.", emailAttachment]
yag.send(to=emailList, subject='This Weeks NFL Picks', contents=contents)

driver.quit()

