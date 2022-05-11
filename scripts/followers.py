from dataclasses import dataclass
from multiprocessing.connection import wait
import time
import os
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def followers(username, password, target):
    driver = webdriver.Chrome()
    # define agent as iphone 11
    opt = webdriver.ChromeOptions() 
    opt.add_argument('--headless')
    opt.add_argument('--disable-gpu') 
    opt.add_argument('user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A356 Safari/604.1')
    driver = webdriver.Chrome(chrome_options=opt)
    # set size to iphone 11
    driver.set_window_size(375, 812)
    #set window position to second screen
    driver.set_window_position(2000, 150)
    # open url
    driver.get('https://www.instagram.com/')
    # wait for page to load
    time.sleep(2)
    # click link to login
    driver.find_element_by_xpath('//button[contains(text(), "Log In")]').click()
    # wait for page to load
    time.sleep(2)
    # find element name 'username' and send username
    username_input = driver.find_element(By.NAME, 'username')
    # enter username
    username_input.send_keys(username)
    # find password
    password_input = driver.find_element(By.NAME, 'password')
    # enter password
    password_input.send_keys(password)
    # wait for page to load
    time.sleep(2)
    # find login button
    login_button = driver.find_element_by_css_selector('button[type="submit"]')
    # click login button
    login_button.click()
    # wait for page to load
    time.sleep(10)
    # find go to target user profie    
    driver.get('https://www.instagram.com/' + target )
    # wait for page to load
    time.sleep(10)
    # find followers button
    followers_button = driver.find_element_by_css_selector('a[href="/' + target + '/followers/"]')
    # click followers button
    followers_button.click()
    # wait for page to load
    time.sleep(10)


    count = 0

    # find all followers
    while True:
        file = open(os.path.join( os.path.dirname( __file__ ), '..' ) + '\\database\\raw\\followers\\' + target + '.txt', 'a+')
        ul = driver.find_element_by_css_selector('ul')
        driver.execute_script("arguments[0].scrollIntoView(true);", ul)
        time.sleep(6)
        li_elements = ul.find_elements_by_tag_name('li')
        for li in li_elements:
            main_div = li.find_element_by_css_selector('div')
            left_div = main_div.find_elements_by_css_selector('div')[0]
            right_div = main_div.find_elements_by_css_selector('div')[1]
            name_div = left_div.find_elements_by_css_selector('div')[1]
            name = name_div.find_element_by_css_selector('span').text

            ##remove the current main div
            driver.execute_script("arguments[0].remove();", li)
            time.sleep(0.5)

            file.write(name + '\n') 
            count += 1
            # scroll down
            print(count, name)
            #if for loop reaches end, scroll to down 
            driver.execute_script("arguments[0].scrollIntoView(true);", ul)

        time.sleep(3)
        file.close()



    
