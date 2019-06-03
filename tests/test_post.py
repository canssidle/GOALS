import unittest
from app.models import Blogpost

class PostTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Post class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_post = Blogpost(id=1,title='technology',subtitle = 'smart phones',author='canssy',date_posted='05/4/2019',content='work made easier',user_id= 9)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_post,Blogpost))