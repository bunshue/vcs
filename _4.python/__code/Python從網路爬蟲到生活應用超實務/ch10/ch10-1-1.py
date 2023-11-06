from selenium import webdriver

url = "https://www.youtube.com/results?search_query=pytube3"

driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
driver.get(url)
print(driver.title)
tags = driver.find_elements_by_xpath('//*[@id="video-title"]')
links = []
for tag in tags:
    href = tag.get_attribute('href')
    if href:
        links.append(href)
        print(href)
print(len(links))
driver.quit()