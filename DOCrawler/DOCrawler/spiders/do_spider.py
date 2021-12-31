import scrapy


class DOSpider(scrapy.Spider):
    name = "DigitalOceanSpider"
    start_urls = [
        # "https://www.digitalocean.com/community/tutorials/how-to-use-break-continue-and-pass-statements-when-working-with-loops-in-python-3"
        "https://www.digitalocean.com/community/tutorials"
    ]

    def parse(self, response):
        TUTORIAL_SELECTOR = ".tutorial"
        FEATURED_ITEM_SELECTOR = "body.feature-filter-bar div.wrapper div.tutorial-footer div div a::attr(href)"

        if response.css(TUTORIAL_SELECTOR):
            for tutorial in response.css(TUTORIAL_SELECTOR):
                TITLE_SELECTOR = ".tutorial h3 a::text"
                URL_SELECTOR = ".tutorial h3 a::attr(href)"
                yield {
                    "title": tutorial.css(TITLE_SELECTOR).extract_first().strip(),
                    "url": tutorial.css(URL_SELECTOR).extract_first(),
                }
                yield from response.follow_all(css=URL_SELECTOR, callback=self.parse)

                yield from response.follow_all(css=".tutorial h3 a", callback=self.parse)
        elif response.css(FEATURED_ITEM_SELECTOR):
            yield {"url": response.css(FEATURED_ITEM_SELECTOR).extract_first()}
            yield from response.follow_all(css=FEATURED_ITEM_SELECTOR, callback=self.parse)
