import os
import sys
import time
from scripts.userdata import *
from scripts.followers import *
from scripts.following import *
from scripts.userdata import *
from logindata import *

from zoneinfo import available_timezones

# test json import

print('\n')
print('Instagram Target Followers Scraper')
print('----------------------------------')
print('version 1.0')
print('----------------------------------')
print('developed by: Kuray Karaaslan')

print('----------------------------------')
print('\n')
print('available chooices:')
print('[1] - update followers of a target user')
print('[2] - update following of a target user // not working yet')
print('[3] - update database of users')
print('[4] - instagram credentials')
print('[5] - install dependencies')
print('[6] - exit')


while True:
    choice = input('\n\nchoice: ')
    if choice == '1':
        target = input('target username: ')
        followers(username, password, target)
    elif choice == '2':
        target = input('target username: ')
        following(username, password, target)
    elif choice == '3':
        target = input('target username: ')
        while True:
            choice = input(
                '\n\n[1] - update followers of a target user\n[2] - update following of a target user\nchoice: ')
            if choice == '1':
                action = 'followers'
                break
            elif choice == '2':
                action = 'following'
                break
            else:
                print('invalid choice')
        userdata(username, password, target, action)
    elif choice == '4':
        print('edit your credentials in logindata.py')
        print('----------------------------------')
    elif choice == '5':
        #make folder
        if not os.path.exists(os.path.join(os.path.dirname(
                __file__), '..') + '\\database\\'):
            os.mkdir(os.path.join(os.path.dirname(
                __file__), '..') + '\\database\\')
        if not os.path.exists(os.path.join(os.path.dirname(
            __file__), '..') + '\\database\\raw\\'):
            os.mkdir(os.path.join(os.path.dirname(
                __file__), '..') + '\\database\\raw\\')
        if not os.path.exists(os.path.join(os.path.dirname(
            __file__), '..') + '\\database\\raw\\followers\\'):
            os.mkdir(os.path.join(os.path.dirname(
                __file__), '..') + '\\database\\raw\\followers\\')
    elif choice == '6':
        sys.exit()
    else:
        print('\n')
        print('invalid choice')
        print('----------------------------------')
        print('\n')
        print('available chooices:')
        print('[1] - update followers of a target user')
        print('[2] - update following of a target user // not working yet')
        print('[3] - update database of users')
        print('[4] - instagram credentials')
        print('[5] - exit')
        continue
    print('\n')
