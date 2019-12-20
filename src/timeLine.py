from newsFeed import NewsFeed

class TimeLine (NewsFeed):
    def __init__(self, name, icon,owner):
        NewsFeed.__init__(self,id=None,name=name, icon=icon, owner=owner)
        self.my_posts= []
    
    def init_my_posts(self,posts):
        self.my_posts = posts 
    


  

  