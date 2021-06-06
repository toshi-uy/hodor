#!/usr/bin/env python
"""Python script to cheat on website"""

from http import cookiejar
from pathlib import Path
from urllib import request
import mechanize
import http.cookiejar as cookiejar
from PIL import Image, ImageOps, ImageEnhance
import requests
import io
import os
from subprocess import check_output
from bs4 import BeautifulSoup
import pytesseract

def resolve(path):
	print("Resampling the Image")
	return pytesseract.image_to_string(Image.open(path))

def main():
    # Open Browser and getting cookies
    # br = mechanize.Browser()

    # Handling things on browser
    # br.set_handle_equiv(True)
    # br.set_handle_redirect(True)
    # br.set_handle_referer(True)
    # br.set_handle_robots(False)

    # Adding headers
    # br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time = 1)
    # br.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

    # Opening page
    url = "http://158.69.76.135/level3.php"
    # br.open(url)
    headers = {
        'Referer': 'http://158.69.76.135/level3.php',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }

    session = requests.Session()
    data = {
            'id': "2785",
            'key':'',
            'captcha':'',
            'holdthedoor':'Submit'
        }

    for i in range(2):
        URL = "http://158.69.76.135/captcha.php"
        try:
            page = requests.get(URL).content
        except:
            print(f"ERROR - Could not download {URL} - {e}")
        try:
            image_file = io.BytesIO(page)
            image = Image.open(image_file).convert('RGB')
            file_path = os.path.join("./captcha" + '.png')
            with open(file_path, 'wb') as f:
                image.save(f, "PNG", quality=85)
            print(f"SUCCESS - saved {URL} - as {file_path}")
            captcha_text = resolve(file_path)
        except Exception as e:
            print(f"ERROR - Could not save {URL} - {e}")
        data['captcha'] = captcha_text
        response = session.get(url)
        cookies = session.cookies
        dict = cookies.get_dict()
        data['key'] = dict.get('HoldTheDoor')
        print(data['key'])
        page = session.post(url, data=data, headers=headers)
        session.cookies.clear()

        print("Done!")

if __name__ == '__main__':
    main()