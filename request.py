from typing import List, Any

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
        '''
        :return:
        '''
        for x in self.soup.findAll('a', {'class': 'header-new-playlink'}):
            self.hrefOnCurrentSong.append({"link" : x['href'], 'genre': self.getGenre()})
            break
        # self.hrefOnCurrentSong = list(set(self.hrefOnCurrentSong))

    def getRequest(self, request):
        '''
        sends get-request and the result wraps in beautiful soup
        :param request:
        :return: none
        '''
        try:
            result = req.get(request).text
            self.soup = BeautifulSoup(result, 'html.parser')
        except req.exceptions.ConnectionError:
            print("Error")
    def getSimilarLinks(self):
        '''
        gets similar links from the page
        :return: none
        '''
        countSongs = 0;
        for x in self.soup.findAll('a', {'class': 'js-link-block-cover-link link-block-cover-link'}):
            if countSongs == 3: break
            countSongs+=1;
            self.hrefOnSimilarSongs.append(x['href'])

    def getSimilarYouTubeLinks(self, links):
        for elem in links:
            self.getRequest(self.baseUrl+elem)
            self.getLinkOnYouTube()

    def getGenre(self):
        '''
        gets genre
        :return: the first genre that is on the page
        '''
        for x in self.soup.findAll('li', {'class': 'tag'}):
            # print(x.text)
            return x.text