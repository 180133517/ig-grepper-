from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

driver = webdriver.Chrome()

#driver.get("https://www.discuss.com.hk/viewthread.php?tid=28810603&extra=page%3D1&page=2")

#extract list of commment base on xpath
#commments=driver.find_elements_by_xpath("//div[contains(@class, 'postmessage-content t_msgfont')]/span")

for page_no in range(1,100):
	driver.get('https://www.discuss.com.hk/viewthread.php?tid=28810603&extra=page%3D1&page=%s'.format(page_no   ))


#for comment in commments:
   # print(comment.text)


