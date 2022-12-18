import scrapy
import re
import pandas as pd

class shopifyspider(scrapy.Spider):
    name = 'shopify_v4'

    def __init__(self, csv_file='shopify_stores_1000_v2.csv'):
        self.csv_file = csv_file
        self.df = pd.read_csv(self.csv_file)
        self.shopify_url = list(self.df["domain_url"])

    def start_requests(self):
        for url in self.shopify_url:
            yield scrapy.Request(url=url, callback = self.parse)
            
    def parse(self, response):
        #gets all the texts and titles in the website
        text = response.css('body :not(script):not(style):not(code)::text').extract()
        title = response.css('title::text').extract()

        #list of text and titles joined into string
        stext = " ".join(text)
        stitle = " ".join(title)

        #removed special characters and newlines with re (thanks mark)
        clean_text = re.sub(r"{{.*?}}|\s+", " ", stext)
        clean_title = stitle.strip()

        yield {
            "domain_url" : response.url,
            "title": clean_title,
            "texts" : clean_text
        }