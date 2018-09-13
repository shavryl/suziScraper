import scrapy
from .constants import BOTTOMS_SELECTOR, TITLE_SELECTOR, PRICE_SELECTOR, NEXT_PAGE, PRODUCT_SELECTOR


class ScrapeBottoms(scrapy.Spider):
    name = 'bottoms'
    start_urls = [
        'https://suzyshier.com/collections/sz_bottoms_shop-all-bottoms',
    ]

    def parse(self, response):

        for bottom_url in response.css(BOTTOMS_SELECTOR).extract():
            yield response.follow(bottom_url, callback=self.parse_product)

        next_page_url = response.xpath(NEXT_PAGE).extract_first()

        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))

    def parse_product(self, response):

        yield {
            'title': response.css(TITLE_SELECTOR).extract_first(),
            'price': ''.join(response.xpath(PRICE_SELECTOR).re(r'[\d.,]+'))
            # 'color'
            # 'sizes'
            # 'specs'
            # 'description'

        }


