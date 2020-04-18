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
            self.hrefOnCurrentSong.append({x['href']: self.getGenre()})
            break
        # self.hrefOnCurrentSong = list(set(self.hrefOnCurrentSong))

    def getRequest(self, request):
        try:
            result = req.get(request).text
            self.soup = BeautifulSoup(result, 'html.parser')
        except req.exceptions.ConnectionError:
            print("Error")



    def getSimilarLinks(self):
        for x in self.soup.findAll('a', {'class': 'js-link-block-cover-link link-block-cover-link'}):
            self.hrefOnSimilarSongs.append(x['href'])

    def getSimilarYouTubeLinks(self, links):
        for elem in links:
            self.getRequest(self.baseUrl+elem)
            self.getLinkOnYouTube()

       # print(self.hrefOnCurrentSong)

    def getGenre(self):
        for x in self.soup.findAll('li', {'class': 'tag'}):
            # print(x.text)
            return x.text

