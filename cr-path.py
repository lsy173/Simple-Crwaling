from urlparse import urljoin

base1 = "http://example.com/html/a.html"

print(urljoin(base1, "b.html"))
print(urljoin(base1, "sub/c.html"))
print(urljoin(base1, "../index.html"))
print(urljoin(base1, "../img/hoge.png"))
print(urljoin(base1, "../css/hoge.css"))

base2 = "http://example.com/html/a.html"

print(urljoin(base2, "/hoge.html"))
print(urljoin(base2, "http://otherExample.com/wiki"))
print(urljoin(base2, "//anotherExample.org/test"))