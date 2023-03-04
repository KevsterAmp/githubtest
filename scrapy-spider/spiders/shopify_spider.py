import scrapy
import re
import pandas as pd

class shopifyspider(scrapy.Spider):
    #v6
    name = 'shopify_spider'

    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.df = pd.read_csv(self.csv_file)
        self.shopify_url = list(self.df["domain_url"])

    def start_requests(self):
        for url in self.shopify_url:
            yield scrapy.Request(url=url, callback = self.parse)
            
    def parse(self, response):
        #Extracts texts, titles, meta description and alt text of a link
        text = response.css('body :not(script):not(style):not(code)::text').extract()
        title = response.css('title::text').extract()
        meta_description = response.css('meta[name="description"]::attr(content)').extract()
        alt_text = response.css('img[alt]::attr(alt)').extract()

        #List of text and titles joined into string
        stext = " ".join(text)
        stitle = " ".join(title)
        smeta_description = " ".join(meta_description)
        salt_text = " ".join(alt_text)

        #Removes special characters and newlines with re (thanks mark)
        clean_text = re.sub(r"{{.*?}}|\s+", " ", stext)
        
        #This is a weird syntax but it removes middle leading spaces and newlines
        clean_title = " ".join(stitle.split())
        clean_meta = " ".join(smeta_description.split())
        clean_alt = " ".join(salt_text.split())

        yield {
            "domain_url" : response.url,
            "title": clean_title,
            "meta_description": clean_meta,
            "texts" : clean_text,
            "alt_text": clean_alt
        }