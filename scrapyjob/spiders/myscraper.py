import scrapy
from scrapyjob.items import ScrapyjobItem

class MyscraperSpider(scrapy.Spider):
    name = 'myscraper'
    allowed_domains = ['sieuthivieclam.vn']
    # start_urls = ['https://sieuthivieclam.vn/tim-viec-lam/']

    def start_requests(self):
        for page_number in range(1,2):
            yield scrapy.Request(url=f'https://sieuthivieclam.vn/tim-viec-lam/trang-{page_number}.html'.format(page_number),callback=self.parse) 

    def parse(self, response):
        courseList = response.xpath('//div[@class="job-info"]/h3/a/@href').getall()
        for courseItem in courseList:
            item = ScrapyjobItem()
            item['courseUrl'] = response.urljoin(courseItem)
            request = scrapy.Request(url = response.urljoin(courseItem), callback=self.parseCourseDetailPage)
            request.meta['datacourse'] = item
            yield request

    def parseCourseDetailPage(self, response):
        item = response.meta['datacourse']
        item['job_name'] =  response.xpath('normalize-space(//*[@id="main"]/div[1]/div/div/div[1]/div/h1/text())').get()
        item['name_company'] =  response.xpath('//*[@id="main"]/div[1]/div/div/div[1]/div/h3/text()').get()
        item['upadte_date'] = response.xpath('//*[@id="main"]/div[1]/div/div/div[1]/div/div[1]/span/text()').get()

        # thông tin tuyển dụng
        item['rank'] = response.xpath('//*[@id="main"]/div[1]/div/div/div[1]/div/div[2]/ul/li[1]/span[2]/text()').get()
        item['amount'] = response.xpath('normalize-space(//*[@id="main"]/div[1]/div/div/div[1]/div/div[2]/ul/li[5]/span[2]/text())').get().strip()
        item['age'] = response.xpath('//*[@id="main"]/div[1]/div/div/div[1]/div/div[2]/ul/li[7]/span[2]/text()').get().strip()
        item['level'] = response.xpath('//*[@id="main"]/div[1]/div/div/div[1]/div/div[2]/ul/li[9]/span[2]/text()').get()
        item['experience'] = response.xpath('//*[@id="main"]/div[1]/div/div/div[1]/div/div[2]/ul/li[2]/span[2]/text()').get()
        item['salary'] = response.xpath('//*[@id="main"]/div[1]/div/div/div[1]/div/div[2]/ul/li[4]/span[2]/text()').get().strip()
        item['headquarters'] = response.xpath('//*[@id="main"]/div[1]/div/div/div[1]/div/div[2]/ul/li[8]/span[2]/text()').get().strip()
        item['technical_requirements'] = response.xpath('(//*[@id="main"]/div[1]/div/div/div[1]/div/div[5]/div/p/text())').getall()
        yield item