import xml.etree.ElementTree as etree

class XMLReader:
    def __init__(self, filename):
        self.doc = etree.parse(filename).getroot()
        self.info = list()

    def output(self):
        for elem in self.doc:
            self.info.append(elem.text)

