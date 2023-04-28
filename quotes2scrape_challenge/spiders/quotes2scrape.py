import scrapy
from scrapy_splash import SplashRequest

class Quotes2scrapeSpider(scrapy.Spider):
    name = "quotes2scrape"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["http://quotes.toscrape.com/"]

    def start_requests(self):
        yield SplashRequest(
            url='http://quotes.toscrape.com/js/',
            callback=self.parse,
        )

    def parse(self, response):
        for data in response.css("div.quote"):
            # extracting the text of quote
            quote = data.css("span.text::text").extract_first()

            # extracting the text of author
            author = data.css("small.author::text").extract_first()

            # extracting the text of tags, since there are too many tags, we are using extract()
            tags = data.css("div.tags > a.tag::text").extract()

            # yielding the data in key and its values.
            yield {
                'Quote': quote,
                'Author': author,
                'Tags': tags,
            }

        # getting the next page URL
        pagination = response.css("li.next > a::attr(href)").extract_first()

        # checking if the next page is not none, if none then spider will stop.
        if pagination is not None:
            yield SplashRequest(response.urljoin(pagination))
