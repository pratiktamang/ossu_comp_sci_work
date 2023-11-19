from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import pdb

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# url = input("Enter - ")
url = "http://py4e-data.dr-chuck.net/known_by_Verity.html"
position = 18
count = 7


def find_link(position, url):
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    links = soup("a")
    return links[position - 1].get("href", None)


while count > 0:
    url = find_link(position, url)
    count -= 1

print(url.split("_")[2].split(".")[0])
