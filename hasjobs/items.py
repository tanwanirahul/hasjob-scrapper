# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class HasjobsItem(Item):
    # define the fields for your item here like:
    # name = Field()
    pass

class Job(Item):
    source = Field()
    title = Field()
    company = Field()
    description = Field()
    location = Field()
    postedDate = Field()
    jobPerks = Field()
    experience = Field()