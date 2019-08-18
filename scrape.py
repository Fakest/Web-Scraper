from bs4 import BeautifulSoup
import requests
data = []
source = requests.get('https://www.newegg.com/global/uk-en/Desktop-Graphics-Cards/SubCategory/ID-48?Tid=1582767').text

soup = BeautifulSoup(source, 'lxml')


data = soup.find_all('div',{'class':'item-container'})
for element in data:
	try:
		eBrand = element.find('div', 'item-info').div.a.img['title']
	except Exception as e:
		eBrand = 'NA'
	else:
		pass
	finally:
		pass

	eName = element.find('a',{'class':'item-title'})
	ePrice = element.find('li',{'class':'price-current'})
	print(eBrand, '\n', eName.text, '\n', ePrice.text)