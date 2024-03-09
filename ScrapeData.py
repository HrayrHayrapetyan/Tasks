import requests
import requests
from bs4 import BeautifulSoup

   
def scrape_data(https:str):
	try:
		r=requests.get(https)
		soup=BeautifulSoup(r.text,features='html.parser')
		#print(soup)
		with open('scraped.txt','w') as file:
				for item in soup.find_all(class_=['title','description card-text','ratings','float -end review count']):
					file.write(str(item))
	except (FileNotFoundError,AttributeError,NameError,SyntaxError) as exp:
		print(exp)

scrape_data('https://webscraper.io/test-sites/e-commerce/allinone')
 
                                                                                                                      		
                                                                                                                      		
