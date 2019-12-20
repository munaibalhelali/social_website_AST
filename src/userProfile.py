from itertools import count
from timeLine import TimeLine
import copy
class UserProfile : 
    counter = count(0)
    def __init__(self, name=None, email=None, password=None):
        self.uid = next(self.counter)
        self.name = name
        self.email = email
        self.password=password
        self.picture=[]
        self.friends=[]
        self.timeLine= TimeLine(self.name, self.picture, self.uid)
        self.my_pages = []
        self.followed_pages = []
        self.my_groups = []
        self.joined_groups = []
        self.my_events = []
        self.my_posts = []
    


    def set_name(self, in_name):
        self.name = in_name

    def set_email(self, in_email):
        self.email = in_email

    def set_password(self, in_password):
        self.password = in_password
        
    def set_picture(self, in_pic):
        self.picture = in_pic

    def add_friend(self, in_friend):
        self.friends.append(in_friend)
    def init_friends(self, in_friends):
        self.friends= copy.deepcopy(in_friends)

    def add_my_group(self,group):
        self.my_groups.append(group)
    def init_my_groups(self,group):
        self.my_groups= copy.deepcopy(group)

    def join_group(self,group):
        self.joined_groups.append(group)
    def init_joined_groups(self,group):
        self.joined_groups= copy.deepcopy(group)

    def add_my_page(self, page):
        self.my_pages.append(page)
    def init_my_pages(self, pages):
        self.my_pages= copy.deepcopy(pages)

    def follow_page(self, page):
        self.followed_pages.append(page)
    def init_followed_pages(self, pages):
        self.followed_pages = copy.deepcopy(pages)

    def add_event(self, event):
        self.my_events.append(event)
    def init_events(self, events):
        self.my_events = copy.deepcopy(events)


    def get_id(self):
        return self.uid
        
    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_password(self):
        return self.password
        
    def get_picture(self):
        return self.picture

    def get_friends(self):
        return list(self.friends)

    def to_json(self):
        return{
            'id':str(self.uid),
            'name':self.name,
            'email':self.email,
            'password':self.password,
            'friends':self.friends,
            'timeline':str(self.timeLine.get_id()),
            'my_pages':self.my_pages,
            'followed_pages':self.followed_pages,
            'my_groups':self.my_groups,
            'joined_groups':self.joined_groups,
            'my_events':self.my_events,
            'my_posts':self.my_posts
        }

    def get_counter(self):
        return next(self.counter)
        