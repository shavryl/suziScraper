SELECTOR = '.product-tile-image a ::attr("href")'

TITLE = ".header.product__header::text"

BOTTOMS_PRICE = "//span[@class='product__price  js-product-price']//text()"

NEXT_PAGE = '//a[contains(@class, "pagination-button pagination-button-next")]/@href'

BOTTOMS_COLOR = '//label[contains(@class,"product__radio radio-color")]/@data-value'

BOTTOMS_SIZE = '//div[contains(@class, "product__radio")]//text()'

BOTTOMS_DESCRIPTION = '//*[@id="toggle-product__description"]//text()'

BOTTOMS_SPECS = '//*[@id="toggle-product__specs"]/ul/li//text()'

EXCLUSIVES_PRICE = ".product__price::text"
