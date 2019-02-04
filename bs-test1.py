from bs4 import BeautifulSoup

# HTML that want to be anaylzed.
html = """
<html><body>
  <h1>What is scraping?</h1>
  <p>Analyzing Web page.</p>
  <p>Extract what we want</p>
</body></html>
"""

# Analyze what I want
soup = BeautifulSoup(html, 'html.parser')

# Extract what I want
h1 = soup.html.body.h1
p1 = soup.html.body.p
p2 = p1.next_sibling.next_sibling

# print the content
print("h1: " + h1.string)
print("p1: " + p1.string)
print("p2: " + p2.string)

