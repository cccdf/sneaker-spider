import scrapy

class SneakerSpider(scrapy.Spider):
    name = "sneaker"
    start_urls = [
        'https://www.nike.com/w/new-3n82y'
    ]



    def parse(self, response):
        for product in response.css("div.product-card__body"):
            yield{
                'title': product.css("div.product-card__title::text").get(),
                'price': product.css("div.css-b9fpep::text").get()
            }
        # page = response.url.split("/")[-2]
        # filename = 'quotes-%s.html' % page
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log('Saved file %s' % filename)
        