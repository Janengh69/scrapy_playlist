from reader import XMLReader
from request import Request


class Controller:
    def __init__(self):
        self.reader: XMLReader = XMLReader("links.xml")
        self.reader.output()
        self.request: Request = Request(self.reader.info)
        self.resultLinks = list()
        self.resultRelatedLinks = list()

    def scrapy_info(self):
        self.request.getLinkOnYouTube()
        self.request.getSimilarLinks()
        self.request.hrefOnSimilarSongs = list(set(self.request.hrefOnSimilarSongs))

    def call_request(self):
        for request in self.request.request_list:
            self.request.getRequest(request)
            self.scrapy_info()
        self.resultRelatedLinks = self.request.hrefOnSimilarSongs
        self.request.hrefOnSimilarSongs = list(set(self.request.hrefOnSimilarSongs))

        self.request.getSimilarYouTubeLinks(self.resultRelatedLinks)
        self.resultLinks = self.request.hrefOnCurrentSong