import xml.etree.ElementTree as etree
import xml.etree.cElementTree as ET

class XMLReader:
    def __init__(self, filename):
        self.doc = etree.parse(filename).getroot()
        self.info = list()


    def to_list(self):
        for elem in self.doc:
            print(elem.text)
            self.info.append(elem.text)

    def output(self, filename, lst):
        root = ET.Element("root")
        doc = ET.SubElement(root, "doc")

        for elem in lst:
            ET.SubElement(doc, "linkOnSong", genre=elem['genre']).text = elem['link']
        tree = ET.ElementTree(root)
        tree.write(filename)
        return True