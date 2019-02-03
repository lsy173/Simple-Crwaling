import urllib

url = "http://uta.pw/shodou/img/28/214.png"
savename = "test.png"

mem = urllib.urlopen(url).read()

with open(savename, mode="wb") as f:
    f.write(mem)
    print("Saved.")