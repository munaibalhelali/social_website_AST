from newsFeed import NewsFeed

class Event(NewsFeed):
    def __init__(self, name , icon , owner,id = None):
        NewsFeed.__init__(self,id,name, icon, owner)
        self.place = ''
        self.time = ''
        self.date = ''
        self.about = ''

    def set_place(self, place):
        self.place = place
    
    def set_time(self, time):
        self.time = time
    
    def set_date(self, date):
        self.date = date

    def set_about(self,about):
        self.about = about
    def get_time(self):
        return self.time 
    
    def get_date(self):
        return self.date 
    
    def get_place(self):
        return self.place 

    def get_description(self):
        return self.about 
        
    def to_json(self):
        return{
            'name':self.name,
            'owner':self.owner,
            'id':str(self.uid),
            'place':self.place,
            'time':self.time,
            'date':self.date,
            'about':self.about,
            'posts':self.posts,
            'timeline':False
        }


  