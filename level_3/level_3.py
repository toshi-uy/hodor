#!/usr/bin/env python
"""Python script to cheat on website"""

from http import cookiejar
import re
import mechanize
import urllib
import http.cookiejar as cookiejar

br = mechanize.Browser()

cookiejar = cookiejar.LWPCookieJar() 
br.set_cookiejar(cookiejar)

br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time = 1)
br.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
br.open("http://158.69.76.135/level2.php")
for i in range(1023):
    br.select_form(nr=0)
    br.form["id"] = "2785"
    br.submit()
print("Done!")
