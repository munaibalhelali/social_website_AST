from dataManipulator import DataManipulator
from userProfile import UserProfile
from group import Group
from page import Page
from event import Event
from post import Post

class Management():
    def __init__(self):
        #get the information from files
        self.database = DataManipulator()

    def create_new_user(self):
        """This function is used to create new users"""
        name = input('Enter user name: ')
        used_emails = [user.get_email() for user in self.database.users.values()]
        while True:
            email = input('Enter user email: ')
            if email in used_emails:
                print('email is already available in the system')
            else:
                break
        while True:
            password = input('Enter user password: ')
            password1 = input('Re-enter user password: ')

            if password == password1:
                break 
        confirm = input('Create user? (y/n)')
        if confirm.lower() == 'y' or confirm.lower() == 'yes':
            user = UserProfile(None, name, email, password)
            self.database.add_new_user(user)
        
    def delete_user(self,user_id):
        """This function is used to delete users"""
        confirm = input('Are you sure you want to delete this user account? (y/n)')
        if confirm.lower() == 'y' or confirm.lower() == 'yes':
            try:
                if self.database.delete_user(user_id):
                    print('The user has been successfully deleted from the system.')
            except FileNotFoundError as e:
                print("User's file is not found")

    def create_new_page(self, owner):
        """This function is used to create new pages"""
        name = input('Enter page name: ')
        confirm = input('Create the page? (y/n)')
        if confirm.lower() == 'y' or confirm.lower() == 'yes':
            page = Page(name, None, owner, None)
            self.database.add_new_page(page)

            user = self.database.users[owner]
            user.add_my_page(page.get_id())
            self.database.add_new_user(user)

    def follow_page(self, user_id, page_id):
        """This function is used to enable user to follow pages"""
        page = self.database.pages[page_id]
        page.add_follower(user_id)
        self.database.add_new_page(page)

        user = self.database.users[user_id]
        user.follow_page(page_id)
        self.database.add_new_user(user)

    def delete_page(self, page_id):
        """This function is used to delete pages"""
        confirm = input('Are you sure you want to delete this page? (y/n)')
        
        if confirm.lower() == 'y' or confirm.lower() == 'yes':
            try:
                if self.database.delete_page(page_id):
                    print('The page was successfully deleted!!')
            except FileNotFoundError as e:
                print("Page's file was not found")
        

    def create_new_group(self, owner):
        """This function is used to ceate new groups"""
        name = input('Enter group name: ')
        confirm = input('Create the group? (y/n)')
        if confirm.lower() == 'y' or confirm.lower() == 'yes':
            group = Group(name, None, owner, None)
            self.database.add_new_group(group)

            user = self.database.users[owner]
            user.add_my_group(group.get_id())
            self.database.add_new_user(user) 


    def join_group(self, user_id, group_id):
        """This function is used to enable a user to join groups"""
        group = self.database.groups[group_id]
        group.add_member(user_id)
        self.database.add_new_page(group)

        user = self.database.users[user_id]
        user.join_group(group_id)
        self.database.add_new_user(user)

    def delete_group(self, group_id):
        """This function is used to delete groups"""

        confirm = input('Are you sure you want to delete this group? (y/n)')
        
        if confirm.lower() == 'y' or confirm.lower() == 'yes':
            try:
                if self.database.delete_group(group_id):
                    print('The group was successfully deleted!!') 
            except FileNotFoundError as e:
                print("Group's file was not found")

    def create_new_event(self, owner):
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

            self.database.add_new_event(event)

            user = self.database.users[owner]
            user.add_event(event.get_id())
            self.database.add_new_user(user)

    def delete_event(self, event_id):
        """This functin is used to delete an event"""

        confirm = input('Are you sure you want to delete this event? (y/n)')
        
        if confirm.lower() == 'y' or confirm.lower() == 'yes':
            try:
                if self.database.delete_event(event_id):
                    print('The event was successfully deleted!!')
            except FileNotFoundError as e:
                print("Event's file was not found!!") 

    def create_new_post(self, owner):
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
        self.database.create_new_post(post)

        user = self.database.users[owner]
        user.add_post(post.get_id())
        self.database.add_new_user(user)
        return str(post.get_id())


    def edit_post(self, post_id:str):
        """This function is used to edit an existing post"""

        post = self.database.posts[post_id]
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

        self.database.create_new_post(post)

    def delete_post(self, post_id:str):
        """This function is used to delete a post"""

        confirm = input('Are you sure you want to delete this post? (y/n)')
        if confirm.lower() == 'y' or confirm.lower() == 'yes':
            try:
                if self.database.delete_post(post_id):
                    print('The post was successfully deleted!!')
            except FileNotFoundError as e:
                print("Post's file was not found!!") 

    def add_friend(self, user_id,friend_id):
        """This function is used to add friends for the user"""
        user = self.database.users[user_id]
        user.add_friend(friend_id)
        self.database.users[user_id] = user 
        self.database.write_user_to_file(user.to_json()) 

    def remove_friend(self, user_id,friend_id):
        """This function is used to remove a friend from the user friends list"""
        print(user_id)
        user = self.database.users[str(user_id)]
        user.remove_friend(friend_id)
        self.database.users[str(user_id)] = user 
        self.database.write_user_to_file(user.to_json())

    def login(self):
        """This function is used to manage login to the system.
        Return:
        boolean,UserProfile
            It returns True and the user profile if the entered information are correct
            other wise it returns False and -1 to indicate unsuccessful login.
        """
        log_option = input('Choose one of the following:\n\
                            [1] Have an account\n\
                            [2] Create a new account\
                                \n\nEnter your choice: ')
        if int(log_option) == 1:
            user_email = input('Enter user email: ')
            available_emails = [(user,user.get_email()) for user in self.database.users.values()]
            for user, email in available_emails:
                if user_email == email: 
                    password = input('Enter password: ')
                    counter =3
                    while counter >0:
                        if password == user.get_password():
                            return True, user
                        counter -=1
                        print(f'Password does not match, you have {counter} attempts left.')
                        password = input('Re-enter password: ')
            else: 
                print('Email is not in the system!!! ')
                return False, -1 
        elif int(log_option) == 2:
            self.create_new_user()
            return False, -1 
        else:
            return False, -1 

            
            


if __name__ == "__main__":
    #this code is used to test the functionality of the class dataManipulator
    manager = Management()
    print('testing usrs')
    manager.create_new_user()