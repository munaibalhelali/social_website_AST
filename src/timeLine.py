from newsFeed import NewsFeed

class TimeLine (NewsFeed):
    def __init__(self, name, icon,owner, id=None):
        NewsFeed.__init__(self,id= id,name=name, icon=icon, owner=owner)
        self.my_posts= []
    
    def init_my_posts(self,posts):
        self.my_posts = posts 
    
    def to_json(self):
        return{
            'name':self.name,
            'owner':self.owner,
            'id':str(self.uid),
            'posts':self.posts
        }
    def add_post(self, post):
        if type(post) == 'list':
            self.my_posts.extend(post)
        else:
            self.my_posts.append(post)


  

  