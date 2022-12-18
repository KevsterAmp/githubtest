The scrapy folder contains all versions of scrapy_spiders. 
# HOW TO RUN SPIDER
First go to the spider using cd, then run the spider using:
  scrapy crawl <spider_name> -a <input_csv_file> -o <output_csv_file>
 
 via google colab
  !scrapy crawl <spider_name> -a <input_csv_file> -o <output_csv_file>

# shopify_spider_v1
Scraped the first 100 links of shopify_stores, collected the title and all the text in the <body>. The extracted text are unique words from the html.

# shopify_spider_v2
The spider will now be able to remove newlines ("\n") and the extracted texts are not unique words anymore

# shopify_spider_v3
Implemented the v2 spider to the 1000 links. Only being able to scrape a maximum of 420-440 links due to the file handling limit of my system. Limited my scraper to only scrape 250 links to prevent errors in filehandling

# shopify_spider_v4
Used google collab to scrape 2000 links with scrapy. added the .log file to settings.py to reduce lag in using google colab
  
# shopify_spider_v5
Added retry_http_codes and retry_times in settings.py, to decrease runtime of my spider
  
# shopify_spider_v6
Scraped additional data, metadescription and alt texts of images for data collection. changed retry_times in settings.py to 1.
