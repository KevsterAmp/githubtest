import scrapy
import re
import pandas as pd

class shopifyspider(scrapy.Spider):
    name = 'shopify'

    def __init__(self, csv_file='shopify_stores_v2.csv'):
        self.csv_file = csv_file
        self.df = pd.read_csv(self.csv_file)
        self.shopify_url = list(self.df["domain_url"])

    def start_requests(self):
        for url in self.shopify_url:
            yield scrapy.Request(url=url, callback = self.parse)

    
    def parse(self, response):
        #gets all the texts in the website
        text = response.css('body :not(script):not(style):not(code)::text').extract()
        title = response.css('title::text').extract()

        #removes spaces and blanks
        clean_txt = [x.strip() for x in text if x.strip()]
        clean_title = [x.strip() for x in title if x.strip()]

        #removes special characters
        data = []
        pattern = re.compile(r'\{+')
        pattern1 = re.compile(r'\}+')

        for x in clean_txt:
            x = pattern.sub('', x).strip("(")
            x = pattern1.sub('', x).strip(")")
            data.append(x.strip())

        #removes duplicates
        udata = [x for x in set(data)]
        uclean_title = [x for x in set(clean_title)]
            
        #joins into a string
        ext = " ".join(udata)
        extitle = " ".join(uclean_title)

        yield {
            "domain_url" : response.url,
            "title": extitle,
            "texts" : ext
        }
