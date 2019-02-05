# Recursively download the python manual program
from bs4 import BeautifulSoup
from urllib import *
from urlparse import *
from os import makedirs
import os.path, time, re

# Variable to check whether already processed.
proc_files = {}

# Function that extract links inside HTML.
def enum_links(html, base):
    soup = BeautifulSoup(html, "html.parser")
    links = soup.select("link[rel='stylesheet']")
    links += soup.select("a[href]")
    result = []
    # Extract href attribute, change link to absolute link.
    for a in links:
        href = a.attrs['href']
        url = urljoin(base, href)
        result.append(url)
    return result

# Function that download and save file.
def download_file(url):
    o = urlparse(url)
    savepath = "./" + o.netloc + o.path
    if re.search(r"/$", savepath):  # if folder, index.html
        savepath += "index.html"
    savedir = os.path.dirname(savepath)
    # Check whether downloaded completely.
    if os.path.exists(savepath): return savepath
    # Make download folder.
    if not os.path.exists(savedir):
        print("mkdir=", savedir)
        makedirs(savedir)
    # Downlaod files.
    try:
        print("download=", url)
        urlretrieve(url, savepath)
        time.sleep(1) # 1 sec pause.
        return savepath
    except:
        print("Download Failed.", url)
        return None

# Download and Anaylze HTML function
def analyze_html(url, root_url):
    savepath = download_file(url)
    if savepath is None: return
    if savepath in proc_files: return
    proc_files[savepath] = True
    print("analyze_html=" , url)
    # Extract link
    html = open(savepath, "r").read()
    links = enum_links(html, url)

    for link_url in links:
        # if link is the path except root, ignore.
        if link_url.find(root_url) != 0:
            if not re.search(r".css$", link_url): continue
        # if HTML
        if re.search(r".(html|hml)$", link_url):
            analyze_html(link_url, root_url)
            continue
        # Extra file.
        download_file(link_url)

if __name__ == "__main__":
    # Download all in URL.
    url = "https://docs.python.org/3.5/library/"
    analyze_html(url, url)