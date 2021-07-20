import scrapy
from scrapy.crawler import CrawlerProcess

class farfetchspider(scrapy.Spider):
    name = 'farfetrchscr'

    def start_requests(self):
        yield scrapy.Request('')
    
    def parse(self, response):
        products = response.css('li.product-grid__item')
        for item in products:
            yield {
                'name': item.css('p.product-card__name::text').get(),
                'price': item.css('p.product-card__price::text').get(),
            }

        for x in range(2,10):
            yield(scrapy.Request(f'', callback=self.parse))

process = CrawlerProcess(settings = {
    'FEED_URI': 'FFarfetch.json',
    'FEED_FORMART': 'json'
})           

process.crawl(farfetchspider)
process.start()