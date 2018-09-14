import scrapy
from .constants import SELECTOR, NEXT_PAGE, TITLE, EXCLUSIVES_PRICE


class ScrapeExclusives(scrapy.Spider):
    name = 'exclusives'
    start_urls = [
        'https://suzyshier.com/collections/sz_sale_shop-all-sale',
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
            'price': ''.join(response.css(EXCLUSIVES_PRICE).re(r'[\d.,]+'))
            # there are no discounted prices in web_exclusives
            # of course I could make selector on Sales page
            # and try it there with 2 kind of prices: real and discounted
            # but it couldn't be checked in web_exclusives anyway
            # 'discounted': response.xpath(EXCLUSIVES_DISCOUNTED).extract(),
        }
