from bs4 import BeautifulSoup
import requests
import csv
data = []
source = requests.get('https://www.newegg.com/global/uk-en/Desktop-Graphics-Cards/SubCategory/ID-48?Tid=1582767').text

soup = BeautifulSoup(source, 'lxml')

file = 'data.csv'
data = soup.find_all('div',{'class':'item-container'})
with open(file, 'a') as f:
	writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
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
		
		writer.writerow([eBrand, eName, eTotal, eDiscount])
		print(eBrand, '\n', eName, '\n', eTotal, '\n', eDiscount)

