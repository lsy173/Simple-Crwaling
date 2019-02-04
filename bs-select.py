from bs4 import BeautifulSoup

# target HTML
html = """
<html><body>
<div id="suyeong">
 <h1>Sogang University</h1>
 <ul class="items">
   <li>Computer Science and Engineering</li>
   <li>Mathematics</li>
   <li>Physics</li>
  </ul>
</div>
</body></html>
"""

# HTML analyze
soup = BeautifulSoup(html, "html.parser")

# Extract what I need by CSS query
# Extract title
h1 = soup.select_one("div#suyeong > h1").string
print("h1 = " + h1)

# Extract list
li_list = soup.select("div#suyeong > ul.items > li")
for li in li_list:
    print("li = " + li.string)
