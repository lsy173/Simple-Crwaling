from bs4 import BeautifulSoup
import urllib

url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

# Bring data using urlopen()
res = urllib.urlopen(url)

# Analyze using BeautifulSoup
soup = BeautifulSoup(res, "html.parser")

# Extract data that I want
title = soup.find("title").string
wf = soup.find("wf").string
print(title)
print(wf)