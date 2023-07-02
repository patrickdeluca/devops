```python
import scrapy
from scrapy.crawler import CrawlerProcess
from web_scraper.spiders.reddit_spider import RedditSpider
from web_scraper.pipelines import JsonWriterPipeline
from web_scraper.items import RedditScraperItem

class RedditScraper:
    def __init__(self):
        self.process = CrawlerProcess(settings={
            'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
            'DOWNLOAD_DELAY': 2,
            'ITEM_PIPELINES': {'web_scraper.pipelines.JsonWriterPipeline': 1},
            'FEED_FORMAT': 'json',
            'FEED_URI': 'output.json'
        })

    def run_spider(self):
        self.process.crawl(RedditSpider)
        self.process.start()

if __name__ == "__main__":
    scraper = RedditScraper()
    scraper.run_spider()
```