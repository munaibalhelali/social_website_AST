from itertools import count
from datetime import datetime
from counter_values import CounterValues
class Post():
    """Provides the necessary tools to create a post"""
    last_counter = CounterValues()
    curr_time = datetime.now()
    def __init__(self, owner, content,id=None):
        self.owner= owner
        self.content = content
        self.uid = id if id != None else self.last_counter.get_next('post')
        self.time = self.curr_time.strftime("%H:%M:%S") 
        self.date = self.curr_time.strftime("%m/%d/%Y")
        
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

    def get_id(self):
        return self.uid 


    
  