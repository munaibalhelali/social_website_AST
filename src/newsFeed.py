from itertools import count

class NewsFeed:
  counter = count(1000000)
  def __init__(self, name, icon, owner):
    self.name = name
    self.uid = next(counter)
    self.icon=icon
    self.owner=owner
    self.post=[]

  def addpost(self, post):
    self.post.append(post)   
    

  def deletepost(self, post):
      self.post.pop(post)

  def displaypost(self, post):
      return post.getcontent()
  