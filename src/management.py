from dataManipulator import DataManipulator
from userProfile import UserProfile
from group import Group
from page import Page
from event import Event
from post import Post

#get the information from files
database = DataManipulator()

def create_new_user():
    """This function is used to create new users"""
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
    """This function is used to delete users"""
    confirm = input('Are you sure you want to delete this user account? (y/n)')
    if confirm.lower() == 'y' or confirm.lower() == 'yes':
        try:
            if database.delete_user(user_id):
                print('The user has been successfully deleted from the system.')
        except FileNotFoundError as e:
            print("User's file is not found")

def create_new_page(owner):
    """This function is used to create new pages"""
    name = input('Enter page name: ')
    confirm = input('Create the page? (y/n)')
    if confirm.lower() == 'y' or confirm.lower() == 'yes':
        page = Page(name, None, owner, None)
        database.add_new_page(page)

        user = database.users[owner]
        user.add_my_page(page.get_id())
        database.add_new_user(user)

def follow_page(user_id, page_id):
    """This function is used to enable user to follow pages"""
    page = database.pages[page_id]
    page.add_follower(user_id)
    database.add_new_page(page)

    user = database.users[user_id]
    user.follow_page(page_id)
    database.add_new_user(user)

def delete_page(page_id):
    """This function is used to delete pages"""
    confirm = input('Are you sure you want to delete this page? (y/n)')
    
    if confirm.lower() == 'y' or confirm.lower() == 'yes':
        try:
            if database.delete_page(page_id):
                print('The page was successfully deleted!!')
        except FileNotFoundError as e:
            print("Page's file was not found")
    

def create_new_group(owner):
    """This function is used to ceate new groups"""
    name = input('Enter group name: ')
    confirm = input('Create the group? (y/n)')
    if confirm.lower() == 'y' or confirm.lower() == 'yes':
        group = Group(name, None, owner, None)
        database.add_new_group(group)

        user = database.users[owner]
        user.add_my_group(group.get_id())
        database.add_new_user(user) 


def join_group(user_id, group_id):
    """This function is used to enable a user to join groups"""
    group = database.groups[group_id]
    group.add_follower(user_id)
    database.add_new_page(group)

    user = database.users[user_id]
    user.join_group(group_id)
    database.add_new_user(user)

def delete_group(group_id):
    """This function is used to delete groups"""

    confirm = input('Are you sure you want to delete this group? (y/n)')
    
    if confirm.lower() == 'y' or confirm.lower() == 'yes':
        try:
            if database.delete_group(group_id):
                print('The group was successfully deleted!!') 
        except FileNotFoundError as e:
            print("Group's file was not found")

def create_new_event(owner):
    """This function is used to create new events"""

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

        user = database.users[owner]
        user.add_event(event.get_id())
        database.add_new_user(user)

def delete_event(event_id):
    """This functin is used to delete an event"""

    confirm = input('Are you sure you want to delete this event? (y/n)')
    
    if confirm.lower() == 'y' or confirm.lower() == 'yes':
        try:
            if database.delete_event(event_id):
                print('The event was successfully deleted!!')
        except FileNotFoundError as e:
            print("Event's file was not found!!") 

def create_new_post(owner):
    """This function is used to create new posts"""

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

    user = database.users[owner]
    user.add_post(post.get_id())
    database.add_new_user(user)


def edit_post(post_id:str):
    """This function is used to edit an existing post"""

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
    """This function is used to delete a post"""

    confirm = input('Are you sure you want to delete this post? (y/n)')
    if confirm.lower() == 'y' or confirm.lower() == 'yes':
        try:
            if database.delete_post(post_id):
                print('The post was successfully deleted!!')
        except FileNotFoundError as e:
            print("Post's file was not found!!") 

def login():
    """This function is used to manage login to the system"""
    raise NotImplementedError

def add_friend(user_id,friend_id):
    """This function is used to add friends for the user"""
    user = database.users[user_id]
    user.add_friend(friend_id)
    database.users[user_id] = user 
    database.write_users_to_file(user.to_json()) 

def remove_friend(user_id,friend_id):
    """This function is used to remove a friend from the user friends list"""
    user = database.users[user_id]
    user.remove_friend(friend_id)
    database.users[user_id] = user 
    database.write_users_to_file(user.to_json())
    



