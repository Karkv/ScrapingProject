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

</body>
</html>

'''

# print(htmlcode)
divs = analyzer.GetDivs(htmlcode)
print(divs)
for div in divs:
    print(div)
