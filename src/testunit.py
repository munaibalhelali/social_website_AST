import unittest
from dataManipulator import DataManipulator
from userProfile import UserProfile
from group import Group
from page import Page
from event import Event
from post import Post
import copy 
class TestWriteToFile(unittest.TestCase):
    database = DataManipulator()
    user = UserProfile(None,'Tester', 'test@gmail.com', '0000')
    def test_create_user(self):
        result = self.database.add_new_user(self.user)
        self.assertEqual(True, result) 

    def test_create_page(self):
        page = Page('testpage',None,self.user.get_id())
        result = self.database.write_page_to_file(page.to_json())  
        self.assertEqual(True, result)   
    
    def test_create_group(self):
        group = Group('testgroup',None,self.user.get_id())
        result = self.database.write_group_to_file(group.to_json())
        self.assertEqual(True, result)

    def test_create_event(self):
        event = Event('testing event',None,self.user.get_id())
        event.set_place('at home')
        event.set_date('13/01/2020')
        event.set_time('15:55')
        event.set_about('testing the functionality of testing unit')
        result = self.database.write_event_to_file(event.to_json())
        self.assertEqual(True, result)

    def test_create_post(self):
        post_content = 'this is a sample post to test the functionality of the test unit'
        post = Post(id=None, owner =self.user.get_id(),content=post_content)
        result = self.database.write_post(post.to_json())
        self.assertEqual(True, result)

class TestDeleteUser(unittest.TestCase):
    database = DataManipulator()

    def test_delete_usr(self):
        users = copy.deepcopy(self.database.users)
        result = None
        for user in users.values():
            user = user.to_json()
            if user['name'] == 'Tester':
                result = self.database.delete_user(user['id'])
        self.assertEqual(True, result)
        

if __name__ == '__main__':
    unittest.main()

    
    
    