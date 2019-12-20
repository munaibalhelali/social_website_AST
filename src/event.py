from newsFeed import NewsFeed

class Event(NewsFeed):
    def __init__(self,id = None, name = None, icon = None, owner = None):
        NewsFeed.__init__(id,name, icon, owner)
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


  