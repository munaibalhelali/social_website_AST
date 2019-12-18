from newsFeed import NewsFeed
class Group(NewsFeed):
    def __init__(self, name, icon, owner):
        NewsFeed.__init__(name,icon,owner)
        self.members = []
        self.admins = []
    
