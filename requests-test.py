import requests
r = requests.get("http://api.aoikujira.com/time/get.php")

text = r.text
print(text)

bin = r.content
print(bin)

site = requests.get("http://www.ssodam.com/link.png")

with open("logo.png", "wb") as f:
    f.write(site.content)

print("Saved.")