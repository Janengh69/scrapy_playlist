from reader import XMLReader
from request import Request
import gevent
import gevent.monkey

gevent.monkey.patch_socket()
from gevent.pool import Pool
import requests
class Controller:

    def __init__(self):
        self.reader: XMLReader = XMLReader("links.xml")
        self.reader.to_list()
        self.request: Request = Request(self.reader.info) #list with links
        self.resultLinks = list()
        # self.resultRelatedLinks = list()
        self.geventList = list()

    def scrapy_info(self):
        '''
        gets you tube links on songs from xml file and hrefs on similar songs
        '''

        #adds you tube link to list
        self.request.getLinkOnYouTube()
        #gets similar links from current song
        self.request.getSimilarLinks()

    def control(self, request):
            self.request.getRequest(request)
            self.scrapy_info()

    def call_request(self):
        for request in self.request.request_list:
            self.control(request)
        self.request.hrefOnSimilarSongs = self.unique(self.request.hrefOnSimilarSongs)
        #links on you tube for similar links
        self.request.getSimilarYouTubeLinks(self.request.hrefOnSimilarSongs)
        self.resultLinks = self.request.hrefOnCurrentSong
        self.request.hrefOnCurrentSong = self.sort_by_genre()
        self.write_to_xml("result.xml")


    def sort_by_genre(self):
        sort = self.request.hrefOnCurrentSong
        sort = sorted(sort,  key = lambda i: i['genre'])
        return sort


    def write_to_xml(self, filename):
        self.reader.output(filename, self.request.hrefOnCurrentSong)

    # def task(self):
    #     self.check_urls(self.reader.info)

    # def gevent_call(self):
    #     threads = [gevent.spawn(self.task) for links in self.reader.info]
    #     gevent.joinall(threads)

    def unique(self, to_be_unique):
        return list(set(to_be_unique))

    def check_urls(self, urls):
        def fetch(url):
            response = requests.request('GET', url)
            print("Status: [%s] URL: %s" % (response.status_code, url))
            self.geventList += response

        pool = Pool(20)
        for url in urls:
            pool.spawn(fetch, url)
        pool.join()