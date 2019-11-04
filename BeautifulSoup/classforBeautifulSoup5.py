import requests
import pandas

from bs4 import BeautifulSoup

# 後面的 pages不加上任何數字，因為這個網址有多頁。
link = 'http://webscraperio.us-east-1.elasticbeanstalk.com/test-sites/e-commerce/static/computers/tablets?page='

# 儲存在這個網址上的所有產品。
products = []

# 共四頁產品頁，所以 range 是 1 到 5
for page in range(1,5):
    # 用 link 加上 數字，可以帶出正確的網頁
    webpage = requests.get(link + str(page))
    
    # 載入網頁裡的資料
    content = webpage.content
    
    # 解析所抓到的資料
    result = BeautifulSoup(content,'html.parser')
    
    # 利用 div 和 class 辨認在網頁上的產品
    products_on_page = result.find_all('div',{"class":"col-sm-4 col-lg-4 col-md-4"})
    
    # 將所有的產品，都寫入在 products 這個 list 裡面
    for product in products_on_page:
        products.append(product)

# 儲存產品的資訊。
names = []
links = []
prices = []

for item in products:
    # 在 a tag 裡面的 srting 就是產品名稱
    names.append(item.a.string)
    # 在 a tag 裡面的 herf 的值 就是產品網址，且要在前面加上網址才會是正確的 url
    links.append('https://www.webscraper.io' + item.a['href'])
    # 在 h4 tag 裡面的 string 就是產品價格
    prices.append(item.h4.string)

data = list(zip(names,links,prices))

d = pandas.DataFrame(data,columns = ['Name','Link','Price'])

try:
    # 如果檔案不存在，則會自己建立檔案。
    d.to_excel('MultiplePageProducts.xlsx')

except:
    print('\nSomething went wrong! Please check your code.')
else:
    print('\nWeb data successfully written to Excel.')

# 不管是否有誤，都會出現 finally
finally:
    print('\nQuitting the program. Bye!')