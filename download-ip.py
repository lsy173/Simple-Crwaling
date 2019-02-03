import urllib

#
url = "http://api.aoikujira.com/ip/ini"
res = urllib.urlopen(url)
data = res.read()

text = data.decode("utf-8")
print(text)