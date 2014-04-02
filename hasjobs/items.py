# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class Job(Item):
    '''
        Represent a Job object from Hasjob board.
    '''
    source = Field()
    title = Field()
    company = Field()
    description = Field()
    location = Field()
    postedDate = Field()
    jobPerks = Field()
