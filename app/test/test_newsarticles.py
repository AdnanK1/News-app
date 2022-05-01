import unittest
from models import newsarticles
Newsarticles = newsarticles.Newsarticles

class NewsarticlesTest(unittest.TestCase):
    def setUp(self):
        self.new_newsarticles = Newsarticles('Wikipedia editors vote to block cryptocurrency donations','Wikipedia editors have voted in favor of dropping cryptocurrency from the Wikimedia Foundation\'s donation options. As Ars Technica reports, an editor for the online encyclopedia called GorillaWarfare wrote a proposal for the foundation to stop accepting crypt…','"https://s.yimg.com/os/creatr-uploaded-images/2021-07/9f595ce0-de17-11eb-bef2-e1b1456d84ae','2022-04-14T11:35:49Z','"https://www.engadget.com/wikipedia-editors-vote-to-block-cryptocurrency-donations-113549175.html')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_newsarticles,Newsarticles))

if __name__ == '__main__':
    unittest.main()