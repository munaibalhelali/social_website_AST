from itertools import count
import copy
class NewsFeed:
	counter = count(1000000)
	def __init__(self,id= None, name=None, icon=None, owner=None):
		self.name = name
		self.uid = id if id!= None else next(counter)
		self.icon=icon
		self.owner=owner
		self.post=[]

	def get_id(self):
		return self.uid
		
	def add_post(self, post):
		self.post.append(post)
	def init_posts(self, posts):
		self.posts = copy.deepcopy(posts)

	def delete_post(self, post):
			self.post.pop(post)

	def display_post(self, post):
			return post.getcontent()
	