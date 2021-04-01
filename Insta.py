from selenium import webdriver
from time import sleep
from re import sub
import time
import random

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.instagram.com/")
username = "username"
password = "pswd"
sleep(5)
driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)
driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(password)
driver.find_element_by_xpath("//button[@type=\"submit\"]").click()
sleep(8)
#notnow1
driver.find_element_by_css_selector("#react-root > section > main > div > div > div > div > button").click()
sleep(5)
#notnow2
driver.find_element_by_css_selector("body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm").click()
sleep(5)
#scoll
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(3)
driver.execute_script("window.scrollTo(0,1080)")
sleep(5)
#explore
driver.find_element_by_css_selector("#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.ctQZg > div > div:nth-child(3) > a > svg").click()
sleep(5)
#postopen
driver.find_element_by_css_selector("#react-root > section > main > div > div.K6yM_ > div > div:nth-child(1) > div:nth-child(2) > div > a > div > div._9AhH0").click()
sleep(5)
comment = ["wow","nice","amazing","Gorgeous"]
 
i=1
while i < 6:
	#follow
	sleep(3)
	driver.find_element_by_css_selector("body > div._2dDPU.CkGkG > div.zZYga > div > article > header > div.o-MQd.z8cbW > div.PQo_0.RqtMr > div.bY2yH > button").click()
	#Like
	driver.find_element_by_css_selector("body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button > div > span > svg").click()
	#save
	driver.find_element_by_css_selector("body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.ltpMr.Slqrh > span.wmtNn > div > div > button > div > svg").click()
	sleep(3)
	#click
	driver.find_element_by_css_selector("body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.sH9wk._JgwE > div > form > textarea").click()
    #comment
	driver.find_element_by_css_selector("body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.sH9wk._JgwE > div > form > textarea").send_keys(random.choice(comment))
	#post
	driver.find_element_by_css_selector("body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.sH9wk._JgwE > div.RxpZH > form > button.sqdOP.yWX7d.y3zKF").click()
	sleep(5)
	#next
	driver.find_element_by_css_selector("body > div._2dDPU.CkGkG > div.EfHg9 > div > div > a._65Bje.coreSpriteRightPaginationArrow").click()
	sleep(3 )
	i+=1
driver.find_element_by_css_selector("body > div._2dDPU.CkGkG > div.Igw0E.IwRSH.eGOV_._4EzTm.BI4qX.qJPeX.fm1AK.TxciK.yiMZG > button > div > svg").click()
sleep(5)
driver.find_element_by_css_selector("#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.ctQZg > div > div:nth-child(5) > span > img").click()
sleep(6)
driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div[2]/div[2]/div[2]").click()
sleep(5)
