import urllib

url = "http://uta.pw/shodou/img/28/214.png"
savename = "test.png"

urllib.urlretrieve(url, savename)
print("Saved.")
