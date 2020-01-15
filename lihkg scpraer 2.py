from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.discuss.com.hk/viewthread.php?tid=28810603&extra=page%3D1&page=2")

#extract list of commment base on xpath
commments=driver.find_elements_by_xpath("//div[contains(@class, 'postmessage-content t_msgfont')]/span")

for comment in commments:
    print(comment.text)

