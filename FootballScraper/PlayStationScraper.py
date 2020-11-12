from selenium import webdriver
import os

desktop = os.path.join(os.path.join(os.path.expanduser('~'), 'Desktop'))
driver = webdriver.Firefox(executable_path=desktop + '\\geckodriver.exe')
add_to_cart_xpath = '/html/body/div/div[1]/div/div[2]/div/div[1]/div[1]/div[1]/div/div/div/div/div[3]/div[5]/div/div[3]/div/div[2]/div[2]/div[1]/section/div[1]/div[3]/button/span/span'
print('Starting...')
count = 0
while True:
   #driver.get('https://www.walmart.com/ip/PlayStation-5-Console/363472942')
    driver.get('https://www.walmart.com/ip/Live-500BT-On-Ear-Wireless-Headphones-with-Voice-Assistant-White/872889758')
    try:
        add_to_cart_button = driver.find_element_by_xpath(add_to_cart_xpath)
        add_to_cart_button.click()
        driver.implicitly_wait(2)
        driver.maximize_window()
        driver.find_element_by_xpath('/html/body/div/div/div/div/div/div/div[1]/div/div[1]/div/div[2]/div/div/div/div/div[3]/div/div/div[2]/div[1]/div[2]/div/button[1]').click()
        driver.implicitly_wait(2)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[1]/div/div/div/div/div[3]/div/div[1]/div/section/section/div/button').click()
        print('\n\n----------- ADDED TO CART, CHECKOUT QUICKLY -----------')
        break
    except:
        count += 1
        driver.implicitly_wait(3)
        print('\nRefreshing for the ' + str(count) + ' time...')