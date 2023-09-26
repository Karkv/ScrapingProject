import time
import pandas as pd
from selenium import webdriver


def readExcel():

    df = pd.read_csv('urls.csv')
    asins = df["Asin"]
    countries = df["country"]
    # print(asins)
    # print(countries)
    return countries, asins


def getUrls(asins, countries):
    url = "https://www.amazon.{0}/dp/{1}"
    n = len(asins)
    urls = []
    for i in range(n):
        country = countries[i]
        asin = asins[i]
        urls.append(url.format(country, asin))
    return urls


def downloadUrl(url):
    # driver = webdriver.Chrome(
    #     'D:/chrome/chromedriver.exe')  # Optional argument, if not specified will search path.
    # Optional argument, if not specified will search path.
    driver = webdriver.Chrome()

    driver.get(
        url)

    time.sleep(20)  # Let the user actually see something!

    src = driver.page_source
    driver.quit()
    return src


# url="https://www.amazon.de/dp/1015"
# data=downloadUrl(url)
# print(data)
countries, asins = readExcel()
urls = getUrls(asins, countries)
u=[]
d=[]
downloadeddata = {}
n = 1
for url in urls:
    html =downloadUrl(url)
    u.append(url)
    d.append(html)
    n += 1
    if n > 3:
        break
for i in range(len(u)):
    downloadeddata[i]=[u[i],d[i]]
print(downloadeddata)
df=pd.DataFrame.from_dict(downloadeddata, orient='index',columns=["URL","HTML"])
df.to_csv("downloaded.csv")

