#!/usr/bin/env python
"""Python script to cheat on website"""

from http import cookiejar
from pathlib import Path
import sys
import mechanize
import http.cookiejar as cookiejar
from PIL import Image, ImageOps, ImageEnhance
import requests
import io
import os
import hashlib
from subprocess import check_output
from bs4 import BeautifulSoup
import pytesseract

def resolve(path):
	print("Resampling the Image")
	check_output([path, '-resample', '600', path])
	return pytesseract.image_to_string(Image.open(path))

# Open Browser and getting cookies
br = mechanize.Browser()
cookiejar = cookiejar.LWPCookieJar() 
br.set_cookiejar(cookiejar)

# Handling things on browser
br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

# Adding headers
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time = 1)
br.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

# Opening page
br.open("http://158.69.76.135/level3.php")

# Resolve captcha
URL = "http://158.69.76.135/captcha.php"
try:
    page = requests.get(URL).content
except:
    print(f"ERROR - Could not download {URL} - {e}")
try:
        image_file = io.BytesIO(page)
        image = Image.open(image_file).convert('RGB')
        file_path = os.path.join("level_3/captchas",hashlib.sha1(page).hexdigest()[:10] + '.jpg')
        with open(file_path, 'wb') as f:
            image.save(f, "JPEG", quality=85)
        print(f"SUCCESS - saved {URL} - as {file_path}")
        captcha_text = resolve(file_path)
        print('Extracted Text',captcha_text)
except Exception as e:
    print(f"ERROR - Could not save {URL} - {e}")



# for i in range(1023):
#     br.select_form(nr=0)
#     br.form["id"] = "2785"
#     br.submit()
print("Done!")
