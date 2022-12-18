import scrapy
import re
import pandas as pd

class shopifyspider(scrapy.Spider):
    name = 'shopify_v2'

    def __init__(self, csv_file='shopify_stores_v2.csv'):
        self.csv_file = csv_file
        self.df = pd.read_csv(self.csv_file)
        self.shopify_url = list(self.df["domain_url"])

    def start_requests(self):
        for url in self.shopify_url:
            yield scrapy.Request(url=url, callback = self.parse)
        # first_url = self.shopify_url[0]
        # yield scrapy.Request(url=first_url, callback = self.parse)

    def parse(self, response):
        #gets all the texts and titles in the website
        text = response.css('body :not(script):not(style):not(code)::text').extract()
        title = response.css('title::text').extract()

        #list of text and titles joined into string
        ext = " ".join(text)
        extitle = " ".join(title)

        #removed special characters and newlines with re (thanks mark)
        clean_text = re.sub(r"{{.*?}}|\s+", " ", ext)
        clean_title = re.sub(r"{{.*?}}|\s+", " ", extitle)

        #removes all whitespaces between words
        clean_text = " ".join(clean_text.split())
        clean_title = " ".join(clean_title.split())

        yield {
            "domain_url" : response.url,
            "title": clean_title,
            "texts" : clean_text
        }
