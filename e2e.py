from selenium import webdriver
from selenium.webdriver.common.by import By



my_driver = webdriver.Chrome(executable_path= r'C:\webdrivers\107\chromedriver.exe')
my_driver.get('http://192.168.20.199:8777/')


