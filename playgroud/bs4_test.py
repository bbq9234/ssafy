import json
import os
import re
import urllib.request

from bs4 import BeautifulSoup

url = "https://store.steampowered.com/app/990650/Survivor_Pass_Vikendi/"
sourcecode = urllib.request.urlopen(url).read()
soup = BeautifulSoup(sourcecode, "html.parser")

print(soup.get_text())