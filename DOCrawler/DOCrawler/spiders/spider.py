# import scrapy
import logging

import scrapy
from DOCrawler.items import QuotesbotItem


class DOSpider(scrapy.Spider):
    name = "toscrape"
    start_urls = [
        "http://quotes.toscrape.com/",
    ]

    def parse(self, response):
        for quote in response.css("div.quote"):
            item = QuotesbotItem()
            item["text"] = quote.css("span.text::text").extract_first()
            item["author"] = quote.css("small.author::text").extract_first()
            yield item

        next_page_url = response.css("li.next > a::attr(href)").extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))
