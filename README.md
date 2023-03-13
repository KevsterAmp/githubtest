# texts-website-scraper
This is a Scrapy Project designed to extract specific information from a list of websites.

## Installation
To install Scrapy, you must have Python 3.5 or higher installed on your computer. You can install Scrapy using pip, by running the following command:
   pip install scrapy

## Usage
1. Clone the repository to your local machine.
2. Create a CSV file containing a list of domain URLs with a column name of `domain_url`.
3. Navigate to the cloned repository in your command line interface.
4. Run the following command:

         scrapy crawl shopify_spider -a csv_file=<path_to_csv_file> -o <output_csv_file>

Replace `<path_to_csv_file>` with the path to your CSV file and replace the `<output_csv_file>` to the name of the output csv file.

The spider will start crawling the URLs in the CSV file and extracting the text, title, meta description, and alt text from each website. The extracted data will be saved in a CSV file you indicated in the `-o <output_csv_file>`.

## Customization
You can modify the spider to extract additional information from the websites, such as product names or prices. To do so, you will need to modify the parse method in the spider.