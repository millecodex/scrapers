# -*- coding: utf-8 -*-
"""web_scraper_selenium.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vFCmc9FwQMffOEHqYjhfOGR2nd0KNWP9
"""

import time

!pip install selenium

!apt-get update # to update ubuntu to correctly run apt install
!apt install chromium-chromedriver
!cp /usr/lib/chromium-browser/chromedriver /usr/bin
import sys
sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver')
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument('--headless')
#chrome_options.add_argument('--no-sandbox')
#chrome_options.add_argument('--disable-dev-shm-usage')
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
#wd = webdriver.Chrome('chromedriver',chrome_options=chrome_options)
wd = webdriver.Chrome('chromedriver',options=options)

wd.get("https://nvd.nist.gov/vuln/search")

print(wd.title)

search = wd.find_element_by_id("Keywords")
search.clear()
search.send_keys("bitcoin")
search.send_keys(Keys.RETURN)

vuln = wd.find_elements_by_tag_name('strong')
print(vuln[1])

