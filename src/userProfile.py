from itertools import count
from timeLine import TimeLine
import copy
from counter_values import CounterValues
class UserProfile : 
    last_counter = CounterValues()
    def __init__(self,id=None, name=None, email=None, password=None,time_line_id=None):
        if id == None:
            self.uid = self.last_counter.get_next('user') 
        else:
            self.uid = id
        self.name = name
        self.email = email
        self.password=password
        self.picture=[]
        self.friends=[]
        self.my_pages = []
        self.followed_pages = []
        self.my_groups = []
        self.joined_groups = []
        self.my_events = []
        self.my_posts = []
        self.timeLine= TimeLine(self.name, self.picture, self.uid, time_line_id)
        self.timeLine.add_post(self.my_posts)

    


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
    def remove_friend(self, in_friend):
        self.friends.remove(in_friend)

    def add_my_group(self,group):
        self.my_groups.append(group)
    def init_my_groups(self,group):
        self.my_groups= copy.deepcopy(group)
    def delete_my_group(self,group_id):
        if group_id in self.my_groups:
            self.my_groups.remove(group_id)

    def join_group(self,group):
        self.joined_groups.append(group)
    def init_joined_groups(self,group):
        self.joined_groups= copy.deepcopy(group)
    def leave_group(self,group_id):
        if group_id in self.joined_groups:
            self.joined_groups.remove(group_id)

    def add_my_page(self, page):
        self.my_pages.append(page)
    def init_my_pages(self, pages):
        self.my_pages= copy.deepcopy(pages)
    def delete_my_page(self, page_id):
        if page_id in self.my_pages:
            self.my_pages.remove(page_id)

    def follow_page(self, page):
        self.followed_pages.append(page)
    def init_followed_pages(self, pages):
        self.followed_pages = copy.deepcopy(pages)
    def unfollow_page(self, page_id):
        if page_id in self.followed_pages:
            self.follow_pages.remove(page_id)

    def add_event(self, event):
        self.my_events.append(event)
    def init_events(self, events):
        self.my_events = copy.deepcopy(events)
    def delete_event(self, event_id):
        if event_id in self.my_events:
            self.my_events.remove(event_id)
    
    def add_post(self, post):
        self.my_posts.append(post)
        self.timeLine.add_post(post)
    def init_post(self,posts):
        self.my_posts = copy.deepcopy(posts)
        self.timeLine.add_post(posts)
    def delete_post(self, post_id):
        if post_id in self.my_posts:
            self.my_posts.remove(post_id)


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
        