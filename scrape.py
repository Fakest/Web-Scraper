from bs4 import BeautifulSoup
import requests
import csv
from time import sleep

data = []
index = 1

file = 'data.csv'

with open(file, 'a') as f:
	writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	writer.writerow(['Index', 'Brand', 'Name', 'Price', 'Discount'])
	for pg in range(0, 16):
		source = requests.get('https://www.newegg.com/global/uk-en/Desktop-Graphics-Cards/SubCategory/ID-48/Page-' + str(pg)).text + '?Tid=1582767'
		print(source)
		soup = BeautifulSoup(source, 'lxml')
		data = soup.find_all('div',{'class':'item-container'})
		
		for element in data:
			try: #some items dont have a brand
				eBrand = element.find('div', 'item-info').div.a.img['title']
			except Exception as e:
				eBrand = 'N/A'
			else:
				pass
			finally:
				pass

			eName = element.find('a',{'class':'item-title'}).text
			containPrice = element.find('li',{'class':'price-current'})

			try: #some prices arent available until you add the item to your cart
				ePrice = containPrice.strong.text
				eDecimal = containPrice.sup.text
				eTotal = '£' + ePrice + eDecimal
			except Exception as e:
				eTotal = 'N/A'
			else:
				pass
			finally:
				pass
			
			try: #not all items have a discount
				eDiscount = element.find('span',{'class':'price-save-percent'}).text
			except Exception as e:
				eDiscount = 'None'
			else:
				pass
			finally:
				pass
			
			writer.writerow([index, eBrand, eName, eTotal, eDiscount])
			print(index, '\n', eBrand, '\n', eName, '\n', eTotal, '\n', eDiscount)
			index = index+1
		#attempt to stop detection of this script by slowing down its requests for new pages
		sleep(1)


