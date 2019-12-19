import os
from userProfile import UserProfile
import csv
class DataManipulator():
    """This class is used to write and read the system infromation 
    into/from files which are considered the database of the system
    """

    def __init__(self):
        self.users = []
        self.events = []
        self.groups = []
        self.posts = []
        self.pages = []
        self.last_counter = {'user':0, 'event':0, 
                            'group':0, 'post':0, 'page':0}
        
    def __read_users(self):
        """This function is used to read the information of all users
        stored in the directory /data/users. Every file is named using the 
        ID of the user and contains his/her name,email, password,list of friends,
        list of owned pages, list of followed pages, list of owned groups, list of joined groups
        and list of events. """

        cwd = os.getcwd()
        cwd = '/'.join(cwd.split('/')[:-1]) if cwd.split('/') == 'src' else cwd
        path = os.join(cwd,'data/users')
        available_users = os.listdir(path)

        for  user_name in available_users:
           with open(path+user_name,'r') as file:
               csv_reader = csv.reader(file, delimiter=',')
               
               user = UserProfile()
        