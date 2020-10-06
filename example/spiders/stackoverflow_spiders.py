import scrapy
import datetime

class StackOverflowSpider (scrapy.Spider):
    name = 'StackOverflow'

    def start_requests(self):
        urls = [
            'https://stackoverflow.com/questions/tagged/python'
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        filename = "test.html"

        #ab - append binary
        #wb - write binary
        #w - write
        with open(filename, 'ab') as f:
            questions = response.xpath('//*[@class="fs-body3 grid--cell fl1 mr12 sm:mr0 sm:mb12"]/text()').get().strip()
            questions = questions[:-10].strip()
            date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            output = date + " | " + questions + "\n"
            f.write(output.encode())
    
    