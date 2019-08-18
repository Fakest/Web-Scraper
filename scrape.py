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

	eName = element.find('a',{'class':'item-title'}).text
	ePrice = element.find('li',{'class':'price-current'})
	try:
		eDiscount = element.find('span',{'class':'price-save-percent'}).text
	except Exception as e:
		eDiscount = 'None'
	else:
		pass
	finally:
		pass
	print(eBrand, '\n', eName, '\n', '£', ePrice.strong.text, ePrice.sup.text, '\n', eDiscount)