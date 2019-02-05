from bs4 import BeautifulSoup
import urllib

url = "https://ko.wikisource.org/wiki/%EC%A0%80%EC%9E%90:%EC%9C%A4%EB%8F%99%EC%A3%BC"
res = urllib.urlopen(url)
soup = BeautifulSoup(res, "html.parser")

print("Crwaling start")

a_list = soup.select("#mw-content-text > div > ul > li a")

print("Crwaling done")

for a in a_list:
    name = a.string
    print("-" + name)