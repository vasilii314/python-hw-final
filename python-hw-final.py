from selenium import webdriver
from selenium.webdriver.common.keys import Keys

drv = webdriver.Chrome('/Users/vasilijderevankin/Desktop/IBS/pyhton-hw/python-hw-final/chromedriver')
drv.get('http://google.com/ncr')
assert 'Google' in drv.title
elem = drv.find_element_by_name('q')
elem.send_keys('selenide')
elem.send_keys(Keys.RETURN)
txt = drv.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div/div/div/div/div[1]/a/div/cite').text[-12:]
assert 'selenide.org' == txt
drv.find_element_by_xpath('//*[@id="hdtb-msb"]/div[1]/div/div[2]/a').click()
txt = drv.find_element_by_xpath('//*[@id="islrg"]/div[1]/div[1]/a[2]/div').text
assert 'selenide.org' != txt
drv.find_element_by_xpath('//*[@id="yDmH0d"]/div[2]/c-wiz/div[1]/div/div[1]/div[1]/div/div/a[1]').click()
txt = drv.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div/div/div/div[1]/a/div/cite').text[-12:]
assert 'selenide.org' == txt
drv.close()