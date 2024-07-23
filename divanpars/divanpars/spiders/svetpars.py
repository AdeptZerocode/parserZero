import scrapy
import csv

class DivannewparsSpider(scrapy.Spider):
    name = "svetpars"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.csv_file = open('output.csv', 'w', newline='', encoding='utf-8')
        self.csv_writer = csv.writer(self.csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        self.csv_writer.writerow(['name', 'price', 'url'])

    def parse(self, response):
        lights = response.css('div._Ud0k')
        for light in lights:
            name = light.css('div.lsooF span::text').get()
            price = light.css('div.pY3d2 span::text').get()
            url = light.css('a').attrib['href']
            if price:
                price = price.replace(' ', '')
            self.csv_writer.writerow([name, price, url])
            yield {
                'name': name,
                'price': price,
                'url': url
            }

    def closed(self, reason):
        self.csv_file.close()