# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# from multiprocessing import connection

import logging

import pymongo

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


class MongoDBPipeline:

    collection_name = "quotes"

    def __init__(self, mongo_server, mongo_port, mongo_db):
        self.mongo_server = mongo_server
        self.mongo_port = mongo_port
        self.mongo_db = mongo_db
        # self.collection_name = collection_name

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_server=crawler.settings.get("MONGODB_SERVER"),
            mongo_port=crawler.settings.get("MONGODB_PORT"),
            mongo_db=crawler.settings.get("MONGO_DB", "items"),
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_server, self.mongo_port)
        dbnames = self.client.list_database_names()
        if self.mongo_db not in dbnames:
            self.db = self.client[self.mongo_db]
        else:
            self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        if self.db:
            self.db[self.collection_name].insert(dict(item))
        logging.debug("Post added to MongoDB")
        return item
