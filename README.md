# Web-Scraper
Newegg webscraper

This is a basic web scraper that scans the Graphic cards from New Egg and extracts the data on their brand, name, price and discount.

This data is then output to a CSV file for further use.

Newegg detects when a script is being used and presents a captcha, to try and handle this I have added a timer that should make the script appear more human like.

Libraries used:
	CSV,
	Beautiful Soup 4,
	Requests
	
Further development ideas:
	I would like to enable my code to scan through all the pages on the website. Some cards also do not have prices displayed until they have been added to the basket, so I would like to work out how to find these prices.
	I would also like to output this data to a website, this would allow me to build more webscrapers for other websites and begin to compare prices.
	
What I learned:
	This is the first time I have worked with Python since 2017 so it served as a good reminder on basic syntax and operations.
	The requests library was used to download the html code on the website and store it in an xml document. This was done so that the data is now stored in a format that the beautiful soup library can work with.
	I learned about beautiful soup and how to extract data from an xml file using it.
