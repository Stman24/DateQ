from scrapling.fetchers import Fetcher

fetcher = Fetcher(auto_match = True)  # Enable auto-matching to handle website changes gracefully!


page = fetcher.get('https://captcha.com/demos/features/captcha-demo.aspx', stealthy_headers=True)  # Fetch website under the radar!
products = page.css('.product', auto_save=True)                                        # Scrape data that survives website design changes!
products = page.css('.product')                                         # Later, if the website structure changes, pass `adaptive=True` to find them!

products = page.get_all_text(ignore_tags=('script', 'style'))  # Extract all text while ignoring irrelevant tags!
print(products)  # Print the extracted products to see the results!