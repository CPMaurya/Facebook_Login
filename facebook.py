from selenium import webdriver
from getpass import getpass

user = input("Enter your username and emailid")
pwd = getpass("Enter your valid password")

driver = webdriver.Chrome("/home/cp/chromedriver")  # your chrome driver path
driver.get('https://www.facebook.com/')

username_field = driver.find_element_by_id('email')
username_field.send_keys(user)

password_field = driver.find_element_by_id('pass')
password_field.send_keys(pwd)

login_btn = driver.find_element_by_id('u_0_2')
login_btn.submit()
