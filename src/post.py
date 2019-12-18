class Post():
    """Provides the necessary tools to create a post"""
    def __init__(self, ownerId, content):
        self.owner= ownerId
        self.content = content

    def getOwner(self):
        return self.owner

    def getContent(self):
        return self.content

    
  