import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

class triangle():
    def trian(self,a,b,c):
        driver = webdriver.Chrome()
        driver.get("https://testpages.eviltester.com/styled/apps/triangle/triangle001.html")
        driver.maximize_window()
        sleep(5)
        s1 = driver.find_element(By.ID,"side1")
        s1.send_keys(a)
        s2 = driver.find_element(By.ID, "side2")
        s2.send_keys(b)
        s3 = driver.find_element(By.ID, "side3")
        s3.send_keys(c)
        driver.find_element(By.ID,"identify-triangle-action").click()
        res = driver.find_element(By.ID,"triangle-type").text
        return res

#t = triangle()
#print(t.trian(1,2,1))
