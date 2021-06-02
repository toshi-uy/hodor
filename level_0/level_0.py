#!/usr/bin/env python
"""Python script to cheat on website"""


import re
import mechanize

for i in range(1024):
    br = mechanize.Browser()
    br.open("http://158.69.76.135/level0.php")
    br.select_form(nr=0)
    br["id"] = "2785"
    response1 = br.submit()
    response2 = br.back()
    response2.get_data()
    response4 = br.reload()
print("Done!")
