import os
from userProfile import UserProfile
from group import Group
from page import Page
from event import Event
import json 

class DataManipulator():
    """This class is used to write and read the system infromation 
    into/from files which are considered the database of the system
    """
    cwd = os.getcwd()
    cwd = os.path.join(cwd,'..')  if cwd.split('/')[-1] == 'src' else cwd
    def __init__(self):
        self.users = {}
        self.events = {}
        self.groups = {}
        self.posts = {}
        self.pages = {}
        self.last_counter = {'user':0, 'event':0, 
                            'group':0, 'post':0, 'page':0}
        self.__read_users()
        self.__read_pages()
        self.__read_groups()
        self.__read_events()

        
    def __read_users(self):
        """This function is used to read the information of all users
        stored in the directory /data/users. Every file is named using the 
        ID of the user and contains his/her name,email, password,list of friends,
        list of owned pages, list of followed pages, list of owned groups, list of joined groups
        and list of events in a json format. """

        path = os.path.join(cwd,'data/users')
        available_users = os.listdir(path)

        for  user_id in available_users:
            #assuming the user data was stored in JSON format
            with open(os.path.join(path,user_id),'r') as file:
                user_data = json.load(file)
                user = UserProfile(user_data['name'], user_data['email'], user_data['password'])
                user.init_friends(user_data['friends'])
                user.init_my_groups(user_data['my_groups'])
                user.init_joined_groups(user_data['joined_groups'])
                user.init_my_pages(user_data['my_pages'])
                user.init_followed_pages(user_data['followed_pages'])
                user.init_events(user_data['my_events'])
                self.users[user_id](user)

    def __read_groups(self):
        """This group is used to read the groups info from the files into the system
        """
        path = os.path.join(cwd,'data/groups')
        available_groups = os.listdir(path)
        for group_id in available_groups:
            with open(os.path.join(path,group_id),'r') as file:
                group_data = json.load(file)
                group = Group(group_data['uid'], group_data['name'], group_data['owner'])
                group.init_admins(group_data['admins'])
                group.init_members(group_data['members'])
                group.init_posts(group_data['posts'])
                self.groups[group_id](group)

    def __read_pages(self):
        """This function is used to read the pages info from the files into the system
        """
        path = os.path.join(cwd,'data/pages')
        available_pages = os.listdir(path)
        for page_id in available_pages:
            with open(os.path.join(path,page_id),'r') as file:
                page_data = json.load(file)
                page = Page(page_data['uid'], page_data['name'], page_data['owner'])
                page.init_admins(page_data['admins'])
                page.init_followers(page_data['followers'])
                page.init_posts(page_data['posts'])
                self.pages[page_id](page)

    def __read_events(self):
        """This function is used to read the pages info from the files into the system
        """
        path = os.path.join(cwd,'data/events')
        available_pages = os.listdir(path)
        for event_id in available_pages:
            with open(os.path.join(path,event_id),'r') as file:
                event_data = json.load(file)
                event = Event(event_data['uid'], event_data['name'], event_data['owner'])
                event.set_place(event_data['place'])
                event.set_time(event_data['time'])
                event.set_date(event_data['date'])
                event.set_about(event_data['about'])
                event.init_posts(event_data['posts'])
                self.pages[event_id](event)

    def __read_counters(self):
        """This funciton is used to read the counter values info from the files into the system
        """
        path = os.path.join(cwd,'data/others/counters.txt')
        with open(path,'r') as file:
            self.last_counter= json.load(file)
            
    def write_users_to_file(self,user:dict):
        with open(os.path.join(cwd,'data/users',user.get_id(),'.txt'),'w') as outputfile:
            json.dump(user,outputfile)
        

    def write_groups_to_file(self, group:dict):
        with open(os.path.join(cwd,'data/groups',group.get_id(),'.txt'),'w') as outputfile:
            json.dump(group,outputfile)
    
    def write_pages_to_file(self,page:dict):
        with open(os.path.join(cwd,'data/pages',page.get_id(),'.txt'),'w') as outputfile:
            json.dump(page,outputfile)
        
    def write_events_to_file(self,event:dict):
        with open(os.path.join(cwd,'data/events',event.get_id(),'.txt'),'w') as outputfile:
            json.dump(event,outputfile)

    def write_counters_to_files(self,counters:dict):
        with open(os.path.join(cwd,'data/others/counters.txt','w')) as outputfile:
            json.dump(counters,outputfile)


    


    
                






                    
                           
                           