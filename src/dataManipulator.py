import os
from userProfile import UserProfile
from group import Group
from page import Page
from event import Event
from post import Post
import json 
from itertools import count
from counter_values import CounterValues
from newsFeed import NewsFeed
class DataManipulator():
    """This class is used to write and read the system infromation 
    into/from files which are considered the database of the system
    """
    
    cwd = os.getcwd()
    cwd = os.path.join(cwd,'..')  if cwd.split('/')[-1] == 'src' else cwd
    last_counter = CounterValues() 
    
    def __init__(self):
        self.users = {}
        self.events = {}
        self.groups = {}
        self.posts = {}
        self.pages = {}
        
        self.__read_counters()
        self.__read_users()
        self.__read_pages()
        self.__read_groups()
        self.__read_events()
        self.__read_posts()
        


        
    def __read_users(self):
        """This function is used to read the information of all users
        stored in the directory /data/users. Every file is named using the 
        ID of the user and contains his/her name,email, password,list of friends,
        list of owned pages, list of followed pages, list of owned groups, list of joined groups
        and list of events in a json format. """

        path = os.path.join(self.cwd,'data/users')
        available_users = os.listdir(path)
        if len(available_users)>0:
            for  user_id in available_users:
                if user_id == 'README.md':
                    continue
                #assuming the user data was stored in JSON format
                with open(os.path.join(path,user_id),'r') as file:
                    user_data = json.load(file)
                    user = UserProfile(user_data['id'],user_data['name'], user_data['email'], 
                                        user_data['password'], user_data['timeline'])
                    user.init_friends(user_data['friends'])
                    user.init_my_groups(user_data['my_groups'])
                    user.init_joined_groups(user_data['joined_groups'])
                    user.init_my_pages(user_data['my_pages'])
                    user.init_followed_pages(user_data['followed_pages'])
                    user.init_events(user_data['my_events'])
                    self.users[user_id.split('.')[0]]=user 

    def __read_groups(self):
        """This group is used to read the groups info from the files into the system
        """
        path = os.path.join(self.cwd,'data/groups')
        available_groups = os.listdir(path)
        if len(available_groups)>0:
            for group_id in available_groups:
                if group_id == 'README.md':
                    continue
                with open(os.path.join(path,group_id),'r') as file:
                    group_data = json.load(file)
                    group = Group(name = group_data['name'],icon = None, owner = group_data['owner'], id = group_data['id'])
                    group.init_admins(group_data['admins'])
                    group.init_members(group_data['members'])
                    group.init_posts(group_data['posts'])
                    self.groups[group_id.split('.')[0]]=group

    def __read_pages(self):
        """This function is used to read the pages info from the files into the system
        """
        path = os.path.join(self.cwd,'data/pages')
        available_pages = os.listdir(path)
        if len(available_pages)>0:
            for page_id in available_pages:
                if page_id == 'README.md':
                    continue
                with open(os.path.join(path,page_id),'r') as file:
                    page_data = json.load(file)
                    page = Page(name = page_data['name'], icon= None,owner = page_data['owner'],id =page_data['id'])
                    page.init_admins(page_data['admins'])
                    page.init_followers(page_data['followers'])
                    page.init_posts(page_data['posts'])
                    self.pages[page_id.split('.')[0]]=page

    def __read_events(self):
        """This function is used to read the pages info from the files into the system
        """
        path = os.path.join(self.cwd,'data/events')
        available_pages = os.listdir(path)
        if len(available_pages)>0:
            for event_id in available_pages:
                if event_id == 'README.md':
                    continue
                with open(os.path.join(path,event_id),'r') as file:
                    event_data = json.load(file)
                    event = Event(name = event_data['name'],icon = None, owner = event_data['owner'], id = event_data['id'])
                    event.set_place(event_data['place'])
                    event.set_time(event_data['time'])
                    event.set_date(event_data['date'])
                    event.set_about(event_data['about'])
                    event.init_posts(event_data['posts'])
                    self.events[event_id.split('.')[0]]=event

    def __read_counters(self):
        """This funciton is used to read the counter values info from the files into the system
        """
        path = os.path.join(self.cwd,'data/others/counters.txt')
        with open(path,'r') as file:
            self.last_counter.init_counters(json.load(file)) 
            
    
    def __read_posts(self):
        """ This function is used to read posts from post folders"""
        path = os.path.join(self.cwd,'data/posts')
        available_posts = os.listdir(path)
        if len(available_posts)>0:
            for post_id in available_posts :
                if post_id == 'README.md':
                    continue
                with open(os.path.join(path,post_id)) as file:
                    post_data = json.load(file)
                    post = Post(owner = post_data['owner'],content = post_data['content'],id = post_data['id'])
                    post.set_date_time(post_data['date'],post_data['time'])
                    self.posts[post_id.split('.')[0]] = post

            
    def write_users_to_file(self,user:dict):
        """This function is used to write/update user info in the users folder"""
        with open(os.path.join(self.cwd,'data/users',user['id']+'.txt'),'w') as outputfile:
            json.dump(user,outputfile)
        

    def write_groups_to_file(self, group:dict):
        """This function is used to write/update group info in the groups folder"""
        with open(os.path.join(self.cwd,'data/groups',group['id']+'.txt'),'w') as outputfile:
            json.dump(group,outputfile)
    
    def write_pages_to_file(self,page:dict):
        """This function is used to write/update page info in the pages folder"""
        with open(os.path.join(self.cwd,'data/pages',page['id']+'.txt'),'w') as outputfile:
            json.dump(page,outputfile)
        
    def write_events_to_file(self,event:dict):
        """This function is used to write/update event info in the events folder"""
        with open(os.path.join(self.cwd,'data/events',event['id']+'.txt'),'w') as outputfile:
            json.dump(event,outputfile)

    def write_counters_to_file(self):
        """This function is used to write/update counter info in the others folder"""
        with open(os.path.join(self.cwd,'data/others/counters.txt'),'w') as outputfile:
            json.dump(CounterValues().last_counter,outputfile)

    def write_post(self,post):
        """This function is used to write new posts to a given path which can be to a
        group, event or page"""
        with open(os.path.join(self.cwd,'data/posts',post['id']+'.txt'),'w') as outputfile:
            json.dump(post,outputfile)
    
    def add_new_user(self, user: UserProfile):
        self.users[user.get_id()] =user
        self.write_users_to_file(user.to_json())
        self.write_pages_to_file(user.timeLine.to_json()) 

    def delete_user(self, user_id: str):
        path = os.path.join(self.cwd,'data/users',user_id+'.txt')
        if os.path.exists(path):
            os.remove(path) 
            
            if not os.path.exists(path) and \
                self.delete_page(self.users[user_id]['timeline']):
                self.users.pop(user_id)
                return True
            else: 
                return False 
        raise FileNotFoundError 

    def add_new_page(self, page:Page):
        self.pages[page.get_id()] = page
        self.write_pages_to_file(page.to_json())

    def delete_page(self, page_id: str):
        path = os.path.join(self.cwd,'data/pages',page_id+'.txt')
        if self.__delete_file_from_database(path):
            self.pages.pop(page_id)
            return True
        else: return False 
              

    def add_new_group(self, group: Group):
        self.groups[group.get_id()] = group
        self.write_groups_to_file(group.to_json)

    def delete_group(self,group_id):
        path = os.path.join(self.cwd,'data/groups',group_id+'.txt')
        if self.__delete_file_from_database(path):
            self.groups.pop(group_id)
            return True
        else: return False  
    
    def add_new_event(self, event:Event):
        self.events[event.get_id()] = event
        self.write_events_to_file(event.to_json)

    def delete_event(self, event_id):
        path = os.path.join(self.cwd,'data/events',event_id+'.txt')
        if self.__delete_file_from_database(path):
            self.groups.pop(event_id)
            return True
        else: return False
              
    def create_new_post(self,post:Post):
        self.posts[str(post.get_id())] = post 
        self.write_post(post.to_json())

    def delete_post(self,post_id:str):
        path = os.path.join(self.cwd,'data/posts',post_id+'.txt')
        if self.__delete_file_from_database(path):
            self.posts.pop(post_id)
            return True
        else: return False

    

    def __delete_file_from_database(self, path:str):
        if os.path.exists(path):
            os.remove(path) 
            
            if not os.path.exists(path):
                return True
            else: 
                return False 
        raise FileNotFoundError



if __name__ == "__main__":
    #this code is used to test the functionality of the class dataManipulator
    database = DataManipulator()
    print('testing usrs')
    user = UserProfile(None,'Munaib Alhelali', 'moneebalhelaly@gmail.com', 'munaib1234')
    database.write_users_to_file(user.to_json())
    user = UserProfile(None,'Munaib Alhelali', 'moneebalhelaly@gmail.com', 'munaib1234')
    database.write_users_to_file(user.to_json())
   
    print('testing pages')
    page = Page('mypage',None,user.get_id())
    database.write_pages_to_file(page.to_json())
    
    print('testing groups')
    group = Group('mygroup',None,user.get_id())
    database.write_groups_to_file(group.to_json()) 
    
    print('testing events')
    event = Event('testing code',None,user.get_id())
    event.set_place('at home')
    event.set_date('01/01/2020')
    event.set_time('00:00')
    event.set_about('testing the functionality of dataManipulator class')
    database.write_events_to_file(event.to_json())

    print('testing posts')
    post_content = 'this is a sample post to test the functionality of the function'
    post = Post(id=None, owner =user.get_id(),content=post_content)
    database.write_post(post.to_json())

    database.write_counters_to_file()
    print(database.users)
    print(database.pages)
    print(database.groups)
    print(database.events)
    print(database.posts)
    print(database.last_counter)

    


    
                






                    
                           
                           