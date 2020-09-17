import unittest
from app.models import News

class NewsTest(unittest.TestCase):

    def setUp(self):
        '''
        Set up method that will run before every test
        '''
        self.new_news = News(1234,'news', 'entertainment news', 'England', 'https://news.co.com"')

    def test_instance(self):

        self.assertTrue(isinstance(self.new_news, News))   