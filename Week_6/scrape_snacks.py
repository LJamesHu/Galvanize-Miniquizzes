from bs4 import BeautifulSoup
import requests

# baseurl = 'http://www.snackdata.com'
# r = requests.get(baseurl)

# soup = BeautifulSoup(r.content, 'html.parser')

# for link in soup.find(id='indexholder').find_all('a'):
#     r2 = requests.get(baseurl + link['href'])
#     soup2 = BeautifulSoup(r2.content, 'html.parser')
#     name = soup.find(id='rightstuff').find('h1').get_text()
#     number = soup.find(class_='seriftyper').find('em').contents[0]
#     flavor = soup.find_all(class_='dropped')[0].get_text()
#     cuisine = soup.find_all(class_='dropped')[1].get_text()
#     series = soup.find_all(class_='dropped')[2].get_text()
#     composition = ''
#     for img in soup.find(class_='clearfix notdropped').find_all('img'):
#         composition += img['alt'] + ', '
#     composition = composition[:-2]
#     date = 
#     description = 
#     taste = 
#     break

r = requests.get('http://www.snackdata.com/corn_dog')

soup = BeautifulSoup(r.content, 'html.parser')

print soup.find(id='rightstuff')

# [name, number, flavor, cuisine, series, composition, date, description, taste]