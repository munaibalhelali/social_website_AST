from newsFeed import NewsFeed
class Page(NewsFeed):

    def __init__(self, name, icon, owner):
        NewsFeed.__init__(name, icon, owner)
        self.followers =[]
        self.admins = []