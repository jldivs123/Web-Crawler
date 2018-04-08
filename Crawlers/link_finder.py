from html.parser import HTMLParser
from urllib import parse

class LinkFinder(HTMLParser):
    def __init__(self, base_url, page_url):
        super().__init__()
        super().base_url = base_url
        super().page_url = url
        super().links = set()

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (attribute, value) in attrs:
                if attribute == 'href':
                    url = parse.urljoin(attribute)
                    self.links.add(url)

    def page_links(self):
        return self.links

    def error(self, message):
        pass

finder = LinkFinder()
finder.feed('<html><head></head></html>')
