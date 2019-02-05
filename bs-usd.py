from bs4 import BeautifulSoup
import urllib

# Bring HTML
url = "http://info.finance.naver.com/ketindex/"
res = urllib.urlopen(url)

# Analyze HTML
soup = BeautifulSoup(res, "html.parser")

# Extract data
price = soup.select_one("div.head_info > span.value").string
print("usd/krw = " + price)