import requests
import pandas
from bs4 import BeautifulSoup

# 抓取網址內的資料。
webpage = requests.get('https://www.webscraper.io/test-sites/e-commerce/allinone/computers/tablets')

# 載入網頁裡的資料。
content = webpage.content

# 解析所抓到的資料
result = BeautifulSoup(content,'html.parser')

# 利用div和class辨認在網頁上的產品資料。
products = result.find_all('div',{"class":"col-sm-4 col-lg-4 col-md-4"})

# 儲存產品的資料。
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

# 將相同資料對應再一起。
data = list(zip(names,links,prices))

# 將資料轉成pandas dataframe，並建立行列。
d = pandas.DataFrame(data,columns = ['Name','Link','Price'])

try:
    # 如果檔案不存在，則會自己建立檔案。
    d.to_excel('Products.xlsx')

except:
    print('\nSomething went wrong! Please check your code.')
else:
    print('\nWeb data successfully written to Excel.')

# 不管是否有誤，都會出現 finally
finally:
    print('\nQuitting the program. Bye!')