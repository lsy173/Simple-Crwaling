from bs4 import BeautifulSoup

html = """
<html><body>
  <h1 id="title">What is Scraping?</h1>
  <p id="body">Anaylzing Web page</p>
  <p>Extract What I want</p>
  </body></html>
"""

# Anaylze What I want
soup = BeautifulSoup(html, 'html.parser')

# Extract What I want by find()
title = soup.find(id="title")
body = soup.find(id="body")

# print the text part
print("#title = " + title.string)
print("#body = " + body.string)