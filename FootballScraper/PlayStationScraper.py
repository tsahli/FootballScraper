from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

desktop = os.path.join(os.path.join(os.path.expanduser('~'), 'Desktop'))
driver = webdriver.Firefox(executable_path=desktop + '\\geckodriver.exe')
add_to_cart_xpath = '/html/body/div/div[1]/div/div[2]/div/div[1]/div[1]/div[1]/div/div/div/div/div[3]/div[5]/div/div[3]/div/div[2]/div[2]/div[1]/section/div[1]/div[3]/button/span/span'
print('Starting...')
count = 0
sign_in_url = 'https://www.walmart.com/account/login?tid=0&returnUrl=%2Fip%2FPlayStation-5-Console%2F363472942'
username = ''
password = ''
username_xpath = 'email'
password_xpath = 'password'
sign_in_xpath = '/html/body/div/div/div[2]/form[1]/button[1]'

driver.get(sign_in_url)
driver.implicitly_wait(5)
username_field = driver.find_element_by_id(username_xpath)
password_field = driver.find_element_by_id(password_xpath)
sign_in_button = driver.find_element_by_xpath(sign_in_xpath)
print('Sending keys...')
username_field.send_keys(username)
password_field.send_keys(password)
sign_in_button.click()
driver.implicitly_wait(5)
print('Signing in...')
while True:
    try:
        driver.implicitly_wait(3)
        add_to_cart_button = driver.find_element_by_xpath(add_to_cart_xpath)
        add_to_cart_button.click()
        driver.maximize_window()
        break
    except:
        count += 1
        driver.implicitly_wait(3)
        print('\nRefreshing for the ' + str(count) + ' time...')
        driver.refresh()

driver.find_element_by_xpath('/html/body/div/div/div/div/div/div/div[1]/div/div[1]/div/div[2]/div/div/div/div/div[3]/div/div/div[2]/div[1]/div[2]/div/button[1]').click()
print('\n----------- DONE, CHECKOUT QUICKLY -----------')
