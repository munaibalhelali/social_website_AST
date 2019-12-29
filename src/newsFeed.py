from itertools import count
import copy
from counter_values import CounterValues
class NewsFeed:
	last_counter = CounterValues()
	
	def __init__(self,id, name, icon, owner):
		self.name = name
		if id == None :
			self.uid = self.last_counter.get_next('news_feed')
		else: 
			self.uid = id 
		self.icon=icon
		self.owner=owner
		self.posts=[]
		self.is_timeline = False

	def get_id(self):
		return str(self.uid)

	def get_name(self):
		return self.name	
	def get_owner(self):
		return str(self.owner) 
	
	def add_post(self, post):
		self.posts.append(post)
	def init_posts(self, posts):
		self.posts = copy.deepcopy(posts)
	def set_as_timeline(self):
		self.is_timeline = True
	def get_posts(self):
		return self.posts[:]
	def delete_post(self, post):
			self.posts.pop(post)

	def display_post(self, post):
			return post.getcontent()
	
	def get_counter(self):
		return next(self.counter)
	