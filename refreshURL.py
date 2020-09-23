import time
from selenium import webdriver

driver = webdriver.Chrome('chromedriver')  # Optional argument, if not specified will search path.
evgaurl = 'https://www.evga.com/products/productlist.aspx?type=0&family=GeForce+30+Series+Family&chipset=RTX+3080'
driver.get(evgaurl)
time.sleep(10)
i = 1
while i < 240:
    driver.refresh()
    time.sleep(10)
    url = driver.current_url
    if url != evgaurl:
        driver.quit()
        driver.get(evgaurl)
        time.sleep(10)
    driver.execute_script("window.scrollTo(0, 1080)")
    time.sleep(10) 
    i += 1
driver.quit()