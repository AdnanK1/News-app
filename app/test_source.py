import unittest
from models import source
Source = source.Source
class SourceTest(unittest.TestCase):

    def setUp(self):
        self.new_source = Source('engadget','Engadget')

    def test_instance(self):
        self.assertTrue(isinstance( self.new_source,Source))

if __name__ == '__main__':
    unittest.main()