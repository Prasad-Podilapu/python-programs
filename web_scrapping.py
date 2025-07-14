#web scrapping is used to collcting data from websites like flipkart,amazon apps etc
import requests
from bs4 import BeautifulSoup
import pandas

#information
store_url="https://www.bikewale.com/"
page_request=requests.get(store_url)
soup=BeautifulSoup(page_request.content,'html.parser')
#print(soup.text)

#names
names=soup.find_all('div',class_="o-jq o-j4 o-jJ")
name=[]
for i in names[0:12]:
    d=i.get_text()
    name.append(d)
#print(name)

#images
images=soup.find_all('img',class_="o-D o-hP o-iB o-iT o-G o-Q o-a0 o-aa o-hl o-ed")
image=[]
for i in images[0:12]:
    f=i['src']
    image.append(f)
#print(image)
#print(df)
data={'Names':name,
      'img':image}
#print(data)
df = pandas.DataFrame(data)
#print(df)
df.to_csv("mobiles_data.csv")

