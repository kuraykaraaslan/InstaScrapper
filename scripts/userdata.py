import json
import os
from multiprocessing.connection import wait
from pickle import TRUE
from re import T
import time
from turtle import update
from webbrowser import get

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def userdata(username, password, target, action):

    #action = 'followers'
    action = 'followers'

    driver = webdriver.Chrome()

    driver.get('https://www.instagram.com/')
    # wait for page to load
    time.sleep(2)
    # click link to login
    # driver.find_element_by_xpath('//button[contains(text(), "Log In")]').click()
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
    time.sleep(7)

    if action == 'followers':

        json_followers_file = os.path.join(os.path.dirname(
            __file__), '..') + '\\database\\' 'users.json'
        with open(json_followers_file, 'r') as f:
            json_followers = json.load(f)
        f.close()

        json_target_followers_file = open(os.path.join(os.path.dirname(
            __file__), '..') + '\\database\\raw\\followers\\' + target + '.txt', 'r')
        json_target_followers = json_target_followers_file.readlines()

        # this is the file that will be used to store the followers by count
        temp_count = 0
        temp_count_all = 0
        for follower in json_target_followers:

            driver.get('https://www.instagram.com/' + follower + '/?__a=1')
            time.sleep(3)
            json_response = driver.find_element_by_tag_name("body").text
            json_response = json.loads(json_response)

            while json_response == '{"message":"","spam":true,"status":"fail"}':
                print('Instagram dedected spam, gonna wait for 5 minutes')
                time.sleep(300)
                driver.get('https://www.instagram.com/' + follower + '/?__a=1')
                time.sleep(3)
                json_response = driver.find_element_by_tag_name("body").text
                json_response = json.loads(json_response)
                if not json_response == '{"message":"","spam":true,"status":"fail"}':
                    break                    
                    

            temp_count_all += 1
            temp_count += 1

            if json_response == {}:
                print('[' + str(temp_count_all) + ']: [' +
                      follower + '] is not a valid user')
                continue
            else:
                print('[' + str(temp_count_all) + ']: [' +
                      follower + '] is a valid user', end=' ')

                if not follower in json_followers.values():
                    print('and not in the database, adding to database')
                    json_user = {
                        "id": json_response['graphql']['user']['id'],
                        "username": json_response['graphql']['user']['username'],
                        "biography": json_response['graphql']['user']['biography'],
                        "full_name": json_response['graphql']['user']['full_name'],
                        "profile_pic_url": json_response['graphql']['user']['profile_pic_url'],
                        "is_business_account": json_response['graphql']['user']['is_business_account'],
                        "is_professional_account": json_response['graphql']['user']['is_professional_account'],
                        "is_private": json_response['graphql']['user']['is_private'],
                        "is_verified": json_response['graphql']['user']['is_verified'],
                        "edge_followed_by": json_response['graphql']['user']['edge_followed_by']['count'],
                        "edge_follow": json_response['graphql']['user']['edge_follow']['count'],
                        "edge_owner_to_timeline_media": json_response['graphql']['user']['edge_owner_to_timeline_media']['count'],
                        "external_url": json_response['graphql']['user']['external_url'],
                        "business_address_json": json_response['graphql']['user']['business_address_json'],
                        "business_contact_method": json_response['graphql']['user']['business_contact_method'],
                        "business_email": json_response['graphql']['user']['business_email'],
                        "business_phone_number": json_response['graphql']['user']['business_phone_number'],
                        "category_name": json_response['graphql']['user']['category_name'],
                        "media_count": json_response['graphql']['user']['edge_owner_to_timeline_media']['count'],
                        "highlight_reel_count": json_response['graphql']['user']['highlight_reel_count'],
                        "date_registered": int(time.time()),
                        "date_updated": '',
                        "date_last_activity": '',
                        "date_last_activity_description": '',
                        "follow": {},
                        "status": 'active'
                    }

                    json_user['follow'][target] = True

                    json_followers[follower] = json_user

                else:
                    print('and in the database, updating database')

                    json_user = json_followers[follower]

                    json_user_new = {
                        "id": json_response['graphql']['user']['id'],
                        "username": json_response['graphql']['user']['username'],
                        "biography": json_response['graphql']['user']['biography'],
                        "full_name": json_response['graphql']['user']['full_name'],
                        "profile_pic_url": json_response['graphql']['user']['profile_pic_url'],
                        "is_business_account": json_response['graphql']['user']['is_business_account'],
                        "is_professional_account": json_response['graphql']['user']['is_professional_account'],
                        "is_private": json_response['graphql']['user']['is_private'],
                        "is_verified": json_response['graphql']['user']['is_verified'],
                        "edge_followed_by": json_response['graphql']['user']['edge_followed_by']['count'],
                        "edge_follow": json_response['graphql']['user']['edge_follow']['count'],
                        "edge_owner_to_timeline_media": json_response['graphql']['user']['edge_owner_to_timeline_media']['count'],
                        "external_url": json_response['graphql']['user']['external_url'],
                        "business_address_json": json_response['graphql']['user']['business_address_json'],
                        "business_contact_method": json_response['graphql']['user']['business_contact_method'],
                        "business_email": json_response['graphql']['user']['business_email'],
                        "business_phone_number": json_response['graphql']['user']['business_phone_number'],
                        "category_name": json_response['graphql']['user']['category_name'],
                        "media_count": json_response['graphql']['user']['edge_owner_to_timeline_media']['count'],
                        "highlight_reel_count": json_response['graphql']['user']['highlight_reel_count'],
                        "date_registered": int(time.time()),
                        "date_updated": '',
                        "date_last_activity": '',
                        "date_last_activity_description": '',
                        "follow": {},
                        "status": 'active'
                    }

                    json_followers[follower] = json_user

                    for key in json_user:
                        updateable_keys = ['edge_followed_by', 'edge_follow',
                                        'edge_owner_to_timeline_media', 'media_count', 'highlight_reel_count']
                        if key in updateable_keys:
                            if json_user_new[key] != json_user[key]:
                                json_user[key] = json_user[key]
                                json_user['date_updated'] = int(time.time())
                                json_user['date_last_activity'] = int(time.time())
                                json_user['date_last_activity_description'] += ' key ' + key + ' changed from ' + str(
                                    json_user[key]) + ' to ' + str(json_response[key]) + '\n'
                            else:
                                json_user['date_updated'] = int(time.time())

                if temp_count == 5:
                    json_object = json.dumps(json_followers, indent=4)
                    with open(json_followers_file, 'w') as outfile:
                        outfile.write(json_object)
                    temp_count = 0
