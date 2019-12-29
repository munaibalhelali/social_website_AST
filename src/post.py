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
        

    def get_owner(self):
        return self.owner

    def get_content(self):
        return self.content

    def get_date(self):
        return self.date 
    
    def get_time(self):
        return self.time 

    def to_json(self):
        return {'owner':self.owner,
                'content':self.content,
                'id':str(self.uid),
                'time':self.time,
                'date':self.date }


    def get_id(self):
        return self.uid 


    
  