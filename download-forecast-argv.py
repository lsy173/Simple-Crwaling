import sys
import urllib

# Extract the command line parameters.
if len(sys.argv) <= 1:
    print("USAGE: download-forecast-argv <Region Number>")
    sys.exit()
regionNumber = sys.argv[1]

# Encode parameters.
API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
values = {
    'stnId': regionNumber
}
params = urllib.urlencode(values)
url = API + "?" + params
print("url= ", url)

# Download data.
data = urllib.urlopen(url).read()
text = data.decode("utf-8")
print(text)