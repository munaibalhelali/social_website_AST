from dataManipulator import DataManipulator
from userProfile import UserProfile
from group import Group
from page import Page
from event import Event
from post import Post

#get the information from files
database = DataManipulator()

def create_new_user():
    name = input('Enter user name: ')
    email = input('Enter user email: ')

    while True:
        password = input('Enter user password: ')
        password1 = input('Re-enter user password: ')

        if password == password1:
            break 
    confirm = input('Create user? (y/n)')
    if confirm.lower() == 'y' or confirm.lower() == 'yes':
        user = UserProfile(None, name, email, password)
        database.add_new_user(user)
    
def delete_user(user_id):
    confirm = input('Are you sure you want to delete this user account? (y/n)')
    if confirm.lower() == 'y' or confirm.lower() == 'yes':
        try:
            if database.delete_user(user_id):
                print('The user has been successfully deleted from the system.')
        except FileNotFoundError as e:
            print("User's file is not found")

def create_new_page(owner):
    name = input('Enter page name: ')
    confirm = input('Create the page? (y/n)')
    if confirm.lower() == 'y' or confirm.lower() == 'yes':
        page = Page(name, None, owner, None)
        database.add_new_page(page)


def delete_page(page_id):
    confirm = input('Are you sure you want to delete this page? (y/n)')
    
    if confirm.lower() == 'y' or confirm.lower() == 'yes':
        try:
            if database.delete_page(page_id):
                print('The page was successfully deleted!!')
        except FileNotFoundError as e:
            print("Page's file was not found")
    

def create_new_group(owner):
    name = input('Enter group name: ')
    confirm = input('Create the group? (y/n)')
    if confirm.lower() == 'y' or confirm.lower() == 'yes':
        page = Page(name, None, owner, None)
        database.add_new_group(page)

def delete_group(group_id):
    confirm = input('Are you sure you want to delete this group? (y/n)')
    
    if confirm.lower() == 'y' or confirm.lower() == 'yes':
        try:
            if database.delete_group(group_id):
                print('The group was successfully deleted!!') 
        except FileNotFoundError as e:
            print("Group's file was not found")

def create_new_event(owner):
    name = input('Enter event the name of the event: ')
    place = input('Enter the place of the event: ')
    time = input('Enter the time of the event: ' )
    date = input('Enter the date of the event: ')
    about = input('Enter event describtion: ')
    confirm = input('Create the event? (y/n)')
    if confirm.lower() == 'y' or confirm.lower() == 'yes':
        event = Event(name,None , owner, None)
        event.set_about(about)
        event.set_date(date)
        event.set_place(place) 
        event.set_time(time)

        database.add_new_event(event)

def delete_event(event_id):
    confirm = input('Are you sure you want to delete this event? (y/n)')
    
    if confirm.lower() == 'y' or confirm.lower() == 'yes':
        try:
            if database.delete_event(event_id):
                print('The event was successfully deleted!!')
        except FileNotFoundError as e:
            print("Event's file was not found!!") 

def create_new_post(owner):
    print('Enter post content: ')
    MultiLine = []
    while True:
        line = input()
        if line:
            MultiLine.append(line)
        else:
            break
    post_content = '\n'.join(MultiLine)

    post = Post(owner, post_content, None)
    database.create_new_post(post)


def edit_post(post_id:str):
    post = database.posts[post_id]
    print(f"Current post content:\n{post['content']}")
    print('Enter post editted content: ')
    MultiLine = []
    while True:
        line = input()
        if line:
            MultiLine.append(line)
        else:
            break
    new_content = '\n'.join(MultiLine)
    post['content'] = new_content

    database.create_new_post(post)


def delete_post(post_id:str):
    confirm = input('Are you sure you want to delete this post? (y/n)')
    if confirm.lower() == 'y' or confirm.lower() == 'yes':
        try:
            if database.delete_post(post_id):
                print('The post was successfully deleted!!')
        except FileNotFoundError as e:
            print("Post's file was not found!!") 

def login():
    raise NotImplementedError




