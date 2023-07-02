```python
from scrapy import Item, Field

class RedditScraperItem(Item):
    # define the fields for your item here like:
    title = Field()
    author = Field()
    upvotes = Field()
    comments = Field()
    url = Field()
```