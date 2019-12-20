from itertools import count
import copy
class NewsFeed:
	counter = count(1000000)
	def __init__(self,id, name, icon, owner):
		self.name = name
		self.uid = id if id!= None else next(self.counter)
		self.icon=icon
		self.owner=owner
		self.posts=[]

	def get_id(self):
		return self.uid
		
	def add_post(self, post):
		self.posts.append(post)
	def init_posts(self, posts):
		self.posts = copy.deepcopy(posts)

	def delete_post(self, post):
			self.posts.pop(post)

	def display_post(self, post):
			return post.getcontent()
	
	def get_counter(self):
		return next(self.counter)
	