from bs4 import BeautifulSoup, SoupStrainer
import requests as req

class Request:
    def __init__(self, request_list):
        self.soup = ''
        self.href = ''
        self.request_list = request_list


    def getLinkOnYouTube(self):
        self.href =  [x['href'] for x in self.soup.findAll('a',  {'class' : 'header-new-playlink' })]

    def getRequest(self):
        for request in self.request_list:
            self.result = req.get(request).text
            self.soup = BeautifulSoup(self.result, 'html.parser')
            self.getLinkOnYouTube()
            print(self.href)