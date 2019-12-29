#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec. 28 12:25:00 2019

@author: munaib al-helali

"""
import os 
from management import Management

class View():
    """This class is used to serve as the interface of the system.
    It prints out the content to the screen"""
    def __init__(self, manager):
        self.manager = manager 

    def view_page(self,page):
        os.system('clear')
        print('Title: ', page.get_name()) 
        print('Owner: ', self.manager.database.users[str(page.get_owner())].get_name())
        print('==============================')
        print('Available Posts: ')
        posts = page.get_posts()
        for post in posts:
            self.view_post(self.manager.database.posts[post])
            print('+'*10,'\n')
        while not page.is_timeline:
            print('\n'*3)
            print('Control commands: ')
            option = input ('Choose one of the following commands: \
                \n[1] View the list of followers.\
                \n[2] View the list of admins.\
                \n[3] Go back\
                \nEnter your choice: ')
            
            if option == '1':
                print('\n'*2)
                print('List of followers of the current page: ')
                for i, follower in enumerate(page.get_followers()):
                    print(f'[{i}] ',self.manager.database.users[follower].get_name())
                
            elif option == '2':
                print('\n'*2)
                print('List of Admins of the current page: ')
                for i, admin in enumerate(page.get_admins()):
                    print(f'[{i}] ',self.manager.database.users[admin].get_name())
                                
            elif option == '3':
                break        

    def view_group(self, group):
        os.system('clear')
        print('Title: ', group.get_name()) 
        print('Owner: ', self.manager.database.users[str(group.get_owner())])
        print('==============================')
        print('Available Posts: ')
        posts = group.get_posts()
        for post in posts:
            self.view_post(self.manager.database.posts[post])
            print('+'*10,'\n')
        while True:
            print('\n'*3)
            print('Control commands: ')
            option = input ('Choose one of the following commands: \
                \n[1] View the list of members.\
                \n[2] View the list of admins.\
                \n[3] Go back\
                \nEnter your choice: ')
            
            if option == '1':
                print('\n'*2)
                print('List of followers of the current page: ')
                for i, member in enumerate(group.get_members()):
                    print(f'[{i}] ',self.manager.database.users[member].get_name())
                
            elif option == '2':
                print('\n'*2)
                print('List of Admins of the current page: ')
                for i, admin in enumerate(group.get_admins()):
                    print(f'[{i}] ',self.manager.database.users[admin].get_name())
                                
            elif option == '3':
                break

    def view_event(self, event):
        os.system('clear')
        print('Title: ', event.get_name()) 
        print('Owner: ', event.get_owner())
        print('Place: ', event.get_place()) 
        print('Time and Date: {}, {}'.format(event.get_time(), event.get_date()))
        print('about: ', event.get_description()) 
        
        print('\nAvailable Posts: ')
        posts = event.get_posts()
        for post in posts:
            self.view_post(self.manager.database.posts[post])
        while True:
            print('\n'*3)
            print('Control commands: ')
            option = input ('Choose one of the following commands: \
                \n[1] Go back\
                \nEnter your choice: ')
            
            if option == '1':
                break


    def view_post(self,post):
        print(f'Owner: {self.manager.database.users[str(post.get_owner())].get_name()}')
        print(f'Time and Date: {post.get_time()}, {post.get_date()}')
        print('='*10)
        print(f'Content: \n{post.get_content()}')



