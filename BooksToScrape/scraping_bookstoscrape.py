import time
import requests
import mysql.connector
from bs4 import BeautifulSoup
from getpass import getpass
pwd = getpass('MySQL root user Password:')
cnx = mysql.connector.connect(
    user = 'root',
    password = f'{pwd}',
    host = 'localhost',
    database = 'scrape')

cursor = cnx.cursor()
book_lst = []
PART_URL = 'https://books.toscrape.com/catalogue/'
sql = ("INSERT INTO `books` "
"(`title`, `book_url`, `price`, `availability`) "
" VALUES (%s, %s, %s, %s)")


for i in range(1,51):
    time.sleep(1)
    req = requests.get(f'https://books.toscrape.com/catalogue/page-{i}.html')
    soup = BeautifulSoup(req.text,'lxml')
    products = soup.findAll("article",{"class":"product_pod"})
    for j in range(20):
        book = products[j].h3.a.attrs['title']
        url = PART_URL + products[j].h3.a.attrs['href']
        price = products[j].find('p',{'class':"price_color"}).getText()
        in_stock = products[j].find('p',{'class':'instock availability'}).getText().strip()
        book_lst.append((book,url,price,in_stock))
try:
    for data in book_lst:
        cursor.execute(sql,data)
except mysql.connector.errors.IntegrityError:
    cnx.commit()
    print('Duplicate Primary Key')
except:
    cnx.commit()
    print('Error Occured')
finally:
    cnx.commit()
    cursor.close()
    cnx.close()





 