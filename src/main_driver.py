#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec. 28 12:25:00 2019

@author: munaib al-helali

This is the main driver of the system. It is reponsible for controlling
and cooredinating  the tasks throughout the operation of the system """

from management import Management
from view import View
import os 
current_user = None
if __name__ == "__main__":
    manager = Management()
    viewer = View(manager) 
    while True:
        os.system('clear')
        #ask the user to login or create a new account
        success, user = manager.login()
        #check if the user successfully loged-in 
        if success:
            current_user = user 
            if user.is_system_admin():
                pass 
            #first thing to be displayed is the user's timeline
            viewer.view_page(manager.database.pages[current_user.get_timeline()])
            while True:
                #give the user the option to brows availalble pages/groups
                option = input('Choose one of the following options:\n\
                                [1] Pages I follow.\n\
                                [2] Groups I am in.\n\
                                [3] View other pages.\n\
                                [4] View other groups.\n\
                                [5] View my events.\n\
                                [6] Create a new page.\n\
                                [7] Create a new group.\n\
                                [8] Create a new event.\n\
                                [9] List Friends.\n\
                                [10] Find Friends.\n\
                                [11] Logout\n\
                                    Enter your choice: ')

                if option == '1':
                    my_pages_list =[]
                    print('List of yours pages:')
                    for i, page_id in enumerate(current_user.get_pages()):
                        print(f'[{i+1}] {manager.database.pages[str(page_id)].get_name()}')
                    while True:
                        sub_option = input('Choose one of the following options:\n\
                                            [1] View page.\n\
                                            [2] Delete page.\n\
                                            [3] Go back\n\
                                                Enter your choice: ')
                        if sub_option == '1':
                            chosen_page = input('Enter the page number: ')
                            viewer.view_page(manager.database.pages[current_user.get_pages()[int(chosen_page)-1]])
                        elif sub_option == '2':
                            page_to_remove = input('Enter the group number: ')
                            page = my_pages_list[int(page_to_remove)]
                            if page.get_owner() == current_user.get_id():
                                if not page.is_timeline :
                                    manager.delete_group(page.get_id())
                                else:
                                    print('A timeline cannot be deleted!!!')
                            else: 
                                print('You are not the owner of this page!!!') 
                                
                        elif sub_option == '3':
                            break 

                elif option == '2':
                    my_groups_list =[]
                    print('List of yours groups:')
                    for i, group_id in enumerate(current_user.get_groups()):
                        group = manager.database.groups[str(group_id)]
                        print(f'[{i+1}] {group.get_name()}')
                        my_groups_list.append(group)
                    while True:
                        sub_option = input('Choose one of the following options:\n\
                                            [1] View group.\n\
                                            [2] Delete group.\n\
                                            [3] Go back\n\
                                                Enter your choice: ')
                        if sub_option == '1':
                            chosen_group = input('Enter the group number: ')
                            viewer.view_group(manager.database.groups[current_user.get_groups()[int(chosen_group)-1]])
                        elif sub_option == '2':
                            group_to_remove = input('Enter the group number: ')
                            group = my_groups_list[int(group_to_remove)]
                            if group.get_owner() == current_user.get_id():
                                manager.delete_group(group.get_id())
                            else: 
                                print('You are not the owner of this page!!!') 

                        elif sub_option == '3':
                            break  

                elif option == '3':
                    print('List of other pages:')
                    pages_list = []
                    for i, page in enumerate(manager.database.pages.values()):
                        print(f'[{i+1}] {page.get_name()}')
                        pages_list.append(page)
                    while True:
                        sub_option = input('Choose one of the following options:\n\
                                            [1] View page.\n\
                                            [2] Follow page\n\
                                            [3] Make a post.\n\
                                            [4] Go back\n\
                                                Enter your choice: ')
                        if sub_option == '1':
                            chosen_page = input('Enter the page number: ')
                            viewer.view_page(pages_list[int(chosen_page)-1]) 
                        elif sub_option == '2':
                            page_no = input('Enter the page number: ')
                            manager.follow_page(current_user.get_id(),
                                                    pages_list[int(page_no)].get_id())
                        elif sub_option == '3':
                            page_no = input('Enter the page number you want to post on: ')
                            post_id = manager.create_new_post(current_user.get_id())
                            page = pages_list[int(page_no)-1]
                            page.add_post(post_id)
                            manager.database.write_page_to_file(page.to_json())
                            
                        elif sub_option == '4':
                            break 

                elif option == '4':
                    print('List of other groups:')
                    groups_list =[]
                    for i, group in enumerate(manager.database.groups.values()):
                        print(f'[{i+1}] {group.get_name()}')
                        groups_list.append(group)
                    while True:
                        sub_option = input('Choose one of the following options:\n\
                                            [1] View group.\n\
                                            [2] Join group.\n\
                                            [3] Make post.\n\
                                            [4] Go back\n\
                                                Enter your choice: ')
                        if sub_option == '1':
                            chosen_group = input('Enter the group number: ')
                            viewer.view_group(groups_list[int(chosen_group)-1]) 
                        elif sub_option == '2':
                            group_no = input('Enter the group number: ')
                            manager.join_group(current_user.get_id(),
                                                groups_list[int(group_no)-1].get_id())
                        elif sub_option == '3':
                            group_no = input('Enter the page number you want to post on: ')
                            post_id = manager.create_new_post(current_user.get_id())
                            group = groups_list[int(group_no)-1]
                            group.add_post(post_id)
                            manager.database.write_group_to_file(group.to_json())
                        
                        elif sub_option == '4':
                            break 
                elif option == '5':
                    print('List of availabel events:')
                    events_list =[]
                    for i, event in enumerate(manager.database.events.values()):
                        print(f'[{i+1}] {event.get_name()}')
                        events_list.append(event) 
                    while True:
                        sub_option = input('Choose one of the following options:\n\
                                            [1] View event.\n\
                                            [2] Make post.\n\
                                            [3] Go back\n\
                                                Enter your choice: ')
                        if sub_option == '1':
                            chosen_event = input('Enter the event number: ')
                            viewer.view_event(events_list[int(chosen_event)-1]) 
                        
                        elif sub_option == '2':
                            event_no = input('Enter the event number you want to post on: ')
                            post_id = manager.create_new_post(current_user.get_id())
                            event = events_list[int(event_no)-1]
                            event.add_post(post_id)
                            manager.database.write_event_to_file(event.to_json())
                        
                        elif sub_option == '3':
                            break 
                elif option == '6':
                    manager.create_new_page(current_user.get_id())

                elif option == '7':
                    manager.create_new_group(current_user.get_id())

                elif option == '8':
                    manager.create_new_event(current_user.get_id())

                elif option == '9':
                    friends = []
                    for friend in current_user.get_friends():
                        friends.append(manager.database.users[str(friend)])
                    for i, friend in enumerate(friends):
                        print(f'[{i+1}] {friend.get_name()}')
                    while True:
                        sub_option = input('Choose one of the following options:\n\
                                            [1] Delete a friend.\n\
                                            [2] Go back.\n\
                                                Enter your choice: ')
                        if sub_option == '1':
                            friend_to_remove = input('Enter friend number: ')
                            print(friends[int(friend_to_remove)-1])
                            manager.remove_friend(current_user.get_id(), 
                                                friends[int(friend_to_remove)-1].get_id())
                        elif sub_option == '2':
                            break 



                elif option == '10':
                    print('List of available users:\n','='*10)
                    users_list = []
                    for i, user in enumerate(manager.database.users.values()):
                        print(f'[{i+1}] {user.get_name()}')
                        users_list.append(user)
                    while True:
                        sub_option = input('Choose one of the following opitons:\n\
                                            [1] Add a new friend.\n\
                                            [2] Go back.\n\
                                                Enter your choice: ')
                        if sub_option == '1':
                            friend_id = input('Enter the user number: ')
                            manager.add_friend(current_user.get_id(), 
                                                    users_list[int(friend_id)-1].get_id())
                        elif sub_option == '2':
                            break 

                elif option == '11':
                    break 
            
            




            
        

        




