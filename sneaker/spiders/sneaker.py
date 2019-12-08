import scrapy
from scrapy_splash import SplashRequest


class SneakerSpider(scrapy.Spider):
    name = "sneaker"
    start_urls = [
        # 'https://www.nike.com/launch/?s=upcoming'
        "https://www.nike.com/w/new-3n82y"
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, args={'wait': 0.5})

    # def parse(self, response):
    #     for product in response.css("section figure")[21:25]:
    #         yield{
    #             'title': product.css("h3::text").extract(),
    #             'time': product.css("figure div div::text").getall(),
    #             'product_link': 'https://www.nike.com' + product.css("figure div div a::attr(href)").get(),
    #             'img_link': product.css('figure div div a img::attr(src)').getall()
    #         }
    def parse(self, response):
        for product in response.css("div.product-card__body"):
            yield{
                'title': product.css("div.product-card__title::text").get(),
                'price': product.css("div.css-b9fpep::text").get(),
                'product_link': 'https://www.nike.com' + product.css("div.product-card__body a.product-card__link-overlay::attr(href)").get(),
                'img_link': product.css("div.product-card__body picture img::attr(src)").extract()
            }
        # page = response.url.split("/")[-2]
        # filename = 'quotes-%s.html' % page
        # filename = 'sneaker.json'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log('Saved file %s' % filename)
