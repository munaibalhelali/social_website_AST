from newsFeed import NewsFeed

class Event(NewsFeed):
    def __init__(self, name, icon, owner):
        NewsFeed.__init__(name, icon, owner)
        self.place = ''
        self.time = ''
        self.date = ''
        self.ouput = ''

  