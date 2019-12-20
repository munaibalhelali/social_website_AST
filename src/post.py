from itertools import count
from datetime import datetime
class Post():
    """Provides the necessary tools to create a post"""
    counter = count(1000000000)
    curr_time = datetime.now()
    def __init__(self,id=None, owner=None, content=None):
        self.owner= owner
        self.content = content
        self.uid = next(self.counter) if id== None else id 
        self.time = self.curr_time.strftime("%H:%M:%S") 
        self.date = self.curr_time.strftime("%m/%d/%Y,")
        

    def set_date_time(self,date, time):
        self.time = time
        self.date = date
        

    def getOwner(self):
        return self.owner

    def getContent(self):
        return self.content


    def to_json(self):
        return {'owner':self.owner,
                'content':self.content,
                'id':str(self.uid),
                'time':self.time,
                'date':self.date }

    def get_counter(self):
        return next(self.counter)


    
  