# scrapy_playlist
## Program that creates playlist

It goes through the pages in the url set specified in the input links.xml file,
as well as the pages referenced from those pages with the specified nesting depth. Program finds all links to mp3 files on all these pages, 
filters the found files by the specified genre stored in the ID3 record, and saves the result to an xml file.
