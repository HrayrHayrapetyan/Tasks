import requests
from bs4 import BeautifulSoup

                                                                                                                       		
def scrape_data(url:str):
        try:
            r=requests.get(url)
            soup=BeautifulSoup(r.text,features='lxml')
            items=soup.find_all(class_='col-md-4 col-xl-4 col-lg-4')
            with open('scraped.txt','w') as file:
                    file.write(str(items))
        except Exception as exp:
            print(exp)

scrape_data('https://webscraper.io/test-sites/e-commerce/allinone')

            
            


         
                    
            

        
        
