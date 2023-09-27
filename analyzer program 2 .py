import analyzer

htmlcode = '''

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Html Document</title>
</head>
<body>
    <div>One</div>
    <div>Two</div>
    <div>Three</div>

    <p>Hello Game : </p>

</body>
</html>

'''

url={'https://www.amazon.in/?&ext_vrnc=hi&tag=googinhydr1-21&ref=pd_sl_9iiff4sfbn_b&adgrpid=107947399415&hvpone=&hvptwo=&hvadid=617721247144&hvpos=&hvnetw=g&hvrand=9473471294606076724&hvqmt=b&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1007827&hvtargid=kwd-299123108802&hydadcr=5716_2362046'}


def dewnloadUrl(url):
    driver=webdriver.Chrome()

    driver.get(url)

    
# print(htmlCode)

divs=analyzer.GetDivs(htmlcode)
print(divs)
for div in divs:
    print(div)

ps=analyzer.GetParagraphs(htmlcode)
print(ps)
for div in divs:
    print(div)


