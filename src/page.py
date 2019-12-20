from newsFeed import NewsFeed
import copy
class Page(NewsFeed):

    def __init__(self, name, icon, owner,id=None):
        NewsFeed.__init__(self,id,name, icon, owner)
        self.followers =[]
        self.admins = []

    def add_follower(self, member):
        self.followers.append(member)
    def init_followers(self, members):
        self.members = copy.deepcopy(members)

    def add_admin(self, admin):
        self.admins.append(admin)
    def init_admins(self, admins):
        self.admins = copy.deepcopy(admins)

    def to_json(self):
        return{
            'name':self.name,
            'owner':self.owner,
            'id':str(self.uid),
            'followers':self.followers,
            'admins':self.admins,
            'posts':self.posts
        }