from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import os
options = None
driverchosen = input("type 1 for chrome, 2 for edge, 3 for firefox, and 4 for safari")
urltoget = input("paste url of paper")
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
issiteworking = False
while issitework = False:
	driver.get("https://sci-hub.se")
	if "<form method=\"POST\" action=\"/\">" in driver.page_source:
		issiteworking = True
		continue
	driver.close()
	print("issue with https://sci-hub.se, now trying mirror site, sci-hub.ru")
	driver.get("https://sci-hub.ru")
	if "<form method=\"POST\" action=\"/\">" in driver.page_source:
		issiteworking = True
		continue
	driver.close()
	print("issue with sci-hub.ru, now trying mirror site, sci-hub.st")
	driver.get("https://sci-hub.st")
	
	
	
	
	
		

driver.quit()
