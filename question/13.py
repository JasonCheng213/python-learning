import os

import requests
from bs4 import BeautifulSoup

response = requests.get("http://tieba.baidu.com/p/2166231880?traceid=")
soup = BeautifulSoup(response.content, "html.parser")
img_tags = soup.find_all("img", class_="BDE_Image")
print(len(img_tags))
if not os.path.exists('download'):
    os.mkdir('download')
for index, img_tag in enumerate(img_tags):
    src = img_tag.get("src")
    try:
        image_response = requests.get(src)
        if image_response.status_code == 200:
            open('download/image_%s.jpg' % index, 'wb').write(image_response.content)
    except requests.exceptions.MissingSchema as ex:
        print("error url : %s" % src)
