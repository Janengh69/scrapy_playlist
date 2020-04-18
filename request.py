from bs4 import BeautifulSoup
import requests as req

class Request:
    def __init__(self, request_list):
        self.baseUrl = 'http://last.fm'
        self.soup = ''
        self.hrefOnCurrentSong = list()
        self.request_list = request_list
        self.hrefOnSimilarSongs = list()

    def getLinkOnYouTube(self):
        for x in self.soup.findAll('a', {'class': 'header-new-playlink'}):
            self.hrefOnCurrentSong.append(x['href'])
        self.hrefOnCurrentSong = list(set(self.hrefOnCurrentSong))
        print(self.hrefOnCurrentSong)

    def getRequest(self, request):
        result = req.get(request).text
        self.soup = BeautifulSoup(result, 'html.parser')


    def getSimilarLinks(self):
        for x in self.soup.findAll('a', {'class': 'js-link-block-cover-link link-block-cover-link'}):
            self.hrefOnSimilarSongs.append(x['href'])

    def getSimilarYouTubeLinks(self, links):
        for elem in links:
            self.getRequest(self.baseUrl+elem)
            self.getLinkOnYouTube()
        print(self.hrefOnCurrentSong)


