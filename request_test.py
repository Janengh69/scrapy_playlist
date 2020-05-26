import unittest

from controller import Controller



class MyTestCase(unittest.TestCase):
    tst = Controller()

    def test_contoller_control(self):
        self.tst.control("https://www.last.fm/ru/music/Nirvana/_/Smells+Like+Teen+Spirit")
        self.assertTrue(self.tst.reader.info, ['https://www.last.fm/ru/music/Nirvana/_/Smells+Like+Teen+Spirit', 'https://www.last.fm/ru/music/Nirvana/_/Come+as+You+Are', 'https://www.last.fm/ru/music/Kanye+West/_/Stronger'])

    def test_controller_(self):
        self.tst.control("https://www.last.fm/ru/music/Nirvana/_/Smells+Like+Teen+Spirit")
        self.assertTrue(self.tst.request.hrefOnCurrentSong, [{'link': 'https://www.youtube.com/watch?v=hTWKbfoikeg', 'genre': 'grunge'}, {'link': 'https://www.youtube.com/watch?v=vabnZ9-ex7o', 'genre': 'grunge'}])

    def test_controller_unique(self):
        lst = ["a", "a, b"]
        self.assertTrue(list(set(lst)), self.tst.unique(lst))

    def test_controller_unique(self):
        self.assertTrue(True, self.tst.write_to_xml("test.xml"))
    def test_controller_unique(self):
        self.assertTrue(True, self.tst.check_urls(self.tst.request.request_list))

if __name__ == '__main__':
    unittest.main()
