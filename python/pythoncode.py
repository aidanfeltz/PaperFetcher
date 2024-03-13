from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import os
import json
import requests
# code for getting json
url = "https://raw.githubusercontent.com/aidanfeltz/PaperFetcher/main/sites.json"
response = requests.get(url)
if response.status_code == 200:
    sites = response.json()["sites"]
options = None
driverchosen = input("type 1 for chrome, 2 for edge, 3 for firefox, and 4 for safari")
urltoget = input("paste url of paper")
#code for getting correct browser
while options is None:
	if driverchosen == "1":
		options = webdriver.ChromeOptions()
    		driver = webdriver.Chrome(options=options)
		continue
	if driverchosen == "2":
    		options = webdrivers.EdgeOptions()
    		driver = webdriver.Edge(options=options)
		continue
	if driverchosen == "3":
		options = webdriver.FirefoxOptions()
    		driver = webdriver.Firefox(options=options)
		continue

for site, which in enumerate(sites):
	driver.get(str(site))
	if "<form method=\"POST\" action=\"/\">" in driver.page_source:
		break
	driver.close()
	print("issue with " + str(sites[which]) + "now trying mirror site" + str(sites[which+1])

	      
	      
	      
	      
	      
driver.quit()
