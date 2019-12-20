from newsFeed import NewsFeed
import copy
class Group(NewsFeed):
    def __init__(self, name=None, icon=None, owner=None):
        NewsFeed.__init__(name,icon,owner)
        self.members = []
        self.admins = []

    def add_member(self, member):
        self.members.append(member)
    def init_members(self, members):
        self.members = copy.deepcopy(members)

    def add_admin(self, admin):
        self.admins.append(admin)
    def init_admins(self, admins):
        self.admins = copy.deepcopy()
    
