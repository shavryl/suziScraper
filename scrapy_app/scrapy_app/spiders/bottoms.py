import scrapy
from scrapy_app.scrapy_app.spiders.constants import SELECTOR, TITLE, BOTTOMS_PRICE, \
    NEXT_PAGE, BOTTOMS_SIZE, BOTTOMS_COLOR, BOTTOMS_DESCRIPTION, BOTTOMS_SPECS


class ScrapeBottoms(scrapy.Spider):
    name = 'bottoms'
    start_urls = [
        'https://suzyshier.com/collections/sz_bottoms_shop-all-bottoms',
    ]

    def parse(self, response):

        for bottom_url in response.css(SELECTOR).extract():
            yield response.follow(bottom_url, callback=self.parse_product)

        next_page_url = response.xpath(NEXT_PAGE).extract_first()

        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))

    @staticmethod
    def parse_product(response):

        yield {
            'title': response.css(TITLE).extract_first(),
            'price': ''.join(response.xpath(BOTTOMS_PRICE).re(r'[\d.,]+')),
            'color': response.xpath(BOTTOMS_COLOR).extract(),
            'sizes': response.xpath(BOTTOMS_SIZE).extract(),
            'description': response.xpath(BOTTOMS_DESCRIPTION).extract_first().strip(),
            'specs': response.xpath(BOTTOMS_SPECS).extract()
        }
