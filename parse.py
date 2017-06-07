import os
from lxml import etree

source_file_path = os.path.abspath(os.path.join("..", "saved.html"))
parser = etree.HTMLParser()
root = etree.parse(source_file_path, parser)
divs = root.findall("//div[@class='_4bl9 _5yjp']")
print("This page include %s links" % len(divs))
for i, div in enumerate(divs):
    print("%s ===========" % (i+1))
    a = div.find("a")
    print(a.attrib['href'])
    span = a.find("span")
    print(span.text)
    