# Purple Review Scraper

This Python script is designed to scrape review data from the Purplle website for multiple products. It utilizes the requests library to send HTTP requests and extract review information from the website. The script uses concurrent threading to enhance the efficiency of data collection.

# Prerequisites

- Python 3.x
- Required Python packages: requests, json, pandas, concurrent.futures

# Usage

Clone this repository or download the script directly.

#### Install the required Python packages if you haven't already:

- `pip install requests pandas`

Prepare a CSV file containing a list of product IDs. Each row should have a unique product ID in the column named "Product id".

Modify the url and other relevant headers in the script to match the website structure, or make any necessary adjustments for your use case.

#### Run the script using the following command:

 - `python purple_review_crawler.py`

The script will scrape review data for each product ID in the CSV file and save the data in separate CSV files named "data1.csv", "data2.csv", and so on.

# Note:

- The script is provided as a starting point and may need modifications to work with changes in the website structure or design.
- Ensure that you have the legal right to scrape data from the website in question.
- Be respectful of the website's terms of use and consider rate limiting to avoid overloading the server.