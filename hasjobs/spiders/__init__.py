# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
from hasjobs.items import Job
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector


class HasGeekSpider(CrawlSpider):
    name = "hasjob"
    allowed_domains = ["hasjob.co"]
    start_urls = ["hasjob.co"]
    rules = [Rule(SgmlLinkExtractor(allow=['/view/\w+']), 'parse_job')]

    def parse_job(self, response):
        '''
            Parses the job information.
        '''
        sel = Selector(response)
        job = Job()
        job["source"] = response.url
        job["title"] = sel.xpath("//h1/text()").extract()
        job["postedDate"] = sel.xpath("//p[@class='post-date']/text()").extract()
        job["location"] = sel.xpath("//span[@class='post-location']/text()").extract()
        job["company"]["name"] = sel.xpath("//span[@class='post-company-name']/text()").extract()
        job["company"]["url"] = sel.xpath("//span[@class='post-company-name']/text()").extract()
        job["company"]["description"] = sel.xpath("//span[@class='post-company-name']/text()").extract()
        job["description"] = sel.xpath("//span[@class='post-company-name']/text()").extract()
        return job
