from bs4 import BeautifulSoup

html ="""
<html><body>
<ul>
  <li><a href="http://www.naver.com">naver</a></li>
  <li><a href="http://www.daum.net">daum</a></li>
</ul>
</body></html>
"""

# Analyze HTML
soup = BeautifulSoup(html, 'html.parser')

# Extract using find_all() method.
links = soup.find_all("a")

# print the link list.
for a in links:
    href = a.attrs['href']
    text = a.string
    print(text, ">", href)