from reader import Reader
from request import Request

if __name__ == "__main__":
    reader: Reader = Reader("links.xml")
    reader.output();
    request: Request = Request(reader.info)
    request.getRequest()