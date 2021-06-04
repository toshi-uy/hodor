#!/usr/bin/env python
"""Python script to cheat on website"""

import re
import mechanize
import pytesseract


br = mechanize.Browser()
br.open("http://158.69.76.135/level1.php")

for i in range(2):
    br.select_form(nr=0)
    br["id"] = "2785"
    # img = get_captcha("/captcha.php")
    # img.save('captcha_original.png')
    # gray = img.convert('L')
    # gray.save('captcha_gray.png')
    # bw = gray.point(lambda x: 0 if x < 1 else 255, '1')
    # bw.save('captcha_thresholded.png')
    # captcha = pytesseract.image_to_string(bw)
    # br["captcha"] = str(captcha)
    response1 = br.submit()
print("Done!")
