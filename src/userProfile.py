from itertools import count
from timeLine import TimeLine
class UserProfile : 
    counter = count(0)
    def __init__(self, name, email, password):
        self.uniqueId = next(counter)
        self.name = name
        self.email = email
        self.password=password
        self.picture=[]
        self.friends=[]
        self.timeLine= TimeLine(self.name, self.picture, self.uniqueId)
        self.my_pages = []
        self.subscribed_pages = []
        self.my_groups = []
        self.subscribed_groups = []
        self.my_events = []
    


def setName(self, in_name):
    self.name = in_name

def setEmail(self, in_email):
    self.email = in_email

def setPassword(self, in_password):
     self.password = in_password
    
def setPicture(self, in_pic):
    self.picture = in_pic

def addFriend(self, in_friend):
    self.friends.append(in_friend)
  
def getName(self):
    return self.name

def getEmail(self):
    return self.email

def getPassword(self):
     return self.password
    
def getPicture(self):
    return self.picture

def getFriends(self):
    return list(self.friends)


     