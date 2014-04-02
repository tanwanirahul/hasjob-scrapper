# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
from hasjobs.items import Job
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector

XPATHS = {
            "title": "//h1/text()",
            "postedDate": "//p[@class='post-date']/text()",
            "location": "//span[@class='post-location']/text()",
            "companyName": "//span[@class='post-company-name']/text()",
            "companyURL": "//span[@class='post-company-url']/a/text()",
            "companyDescription": "//span[@class='post-company-name']/text()",
            "companyLogo": "//img[@class='post-company-logo']/@src",
            "description": "//div[@id='detailed-info']",
            "jobPerks" : "//div[@id='detailed-info']/ul[last()]/li/text()"
          }

class HasGeekSpider(CrawlSpider):
    '''
        Crawler for HasGeek job board (hasjob)
    '''
    name = "hasjob"
    allowed_domains = ["hasjob.co"]
    start_urls = ["http://hasjob.co"]
    rules = [Rule(SgmlLinkExtractor(allow=['/view/\w+']), 'parse_job')]

    def parse_job(self, response):
        '''
            Parses the job information.
        '''
        sel = Selector(response)
        first = 0
        job = Job()
        job["source"] = response.url

        job["title"] = sel.xpath(XPATHS["title"]).extract()[first]

        job["postedDate"] = sel.xpath(XPATHS["postedDate"]).extract()[first]

        job["location"] = sel.xpath(XPATHS["location"]).extract()[first]

        job["companyName"] = sel.xpath(XPATHS["companyName"]).extract()[first]
        job["companyURL"] = sel.xpath(XPATHS["companyURL"]).extract()[first]
        job["companyDetails"] = sel.xpath(XPATHS["companyDescription"]).extract()[first]
        job["companyLogo"] = self.transform_company_logo(sel.xpath(XPATHS["companyLogo"]).extract()[first])

        job["description"] = sel.xpath(XPATHS["description"]).extract()[first]

        job["jobPerks"] = sel.xpath(XPATHS["jobPerks"]).extract()

        return job

    def transform_company_logo(self, relative_img_uri):
        '''
            Given the relative image URI, constructs the fully qualified URL for hasgeek.
        '''
        return "https://hasjob.co%s" %(relative_img_uri)
