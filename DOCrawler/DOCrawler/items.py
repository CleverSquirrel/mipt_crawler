# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

# import scrapy
from scrapy.item import Field, Item


class DocrawlerItem(Item):
    title = Field()
    url = Field()
