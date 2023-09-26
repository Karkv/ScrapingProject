import time 
import pandas as pd
from selenium import webdriver

from seleniumdownloader import downloadUrl

def readExecl():
    df = pd.read_csv('urls.csv')
    asins=df['Asin']
    countries=df["country"]

    return countries,asins


def getUrls(asins,countries):
    url="https://www.amazon.{0}/dp/{1}"
    n=len(asins)
    urls=[]
    for i in range(n):
        country=countries[i]
        asin=asins[i]
        urls.append(url.format(country,asin))
    return urls

def downlaodUrls(url):
    driver=webdriver.Chrome()

    driver.get(url)

    time.sleep(10)
    src=driver.page_source
    driver.quit()
    return src

countries,asins=readExecl()
urls=getUrls(asins,countries)
u=[]
d=[]
downlaodeddata={}

n=1
for url in urls:
    html=downloadUrl(url)
    u.append(url)
    d.append(html)
    n+=1
    if n>3:
        break
for i in range(len(u)):
    downlaodeddata[i]=[u[i],u[i]]
print(downlaodeddata)

df=pd.DataFrame.from_dict(downlaodeddata,orient='index',columns=['URL','HTML'])
df.to_csv("downloalded.csv")