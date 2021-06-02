#!/usr/bin/env python
"""Python script to cheat on website"""

import re
import mechanize

br = mechanize.Browser()
br.open("http://158.69.76.135/level1.php")
for i in range(4096):
    br.select_form(nr=0)
    br["id"] = "2785"
    response1 = br.submit()
print("Done!")
