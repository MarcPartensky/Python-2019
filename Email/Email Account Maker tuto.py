from selenium import webdriver
import time

def createMailAddress(adress,password):
    url = 'https://protonmail.com/'
    driver = webdriver.Chrome('/Users/olivierpartensky/Programs/Library/Selenium/chromedriver')
    driver.get(url)
    driver.find_element_by_xpath('//*[@title="Sign Up"]').click()
    time.sleep(2)
    driver.find_element_by_class_name('panel-heading').click()
    time.sleep(4)
    driver.find_element_by_id('freePlan').click()
    time.sleep(2)
    driver.find_element_by_id('username').send_keys(adress)
    time.sleep(2)
    driver.find_element_by_id('password').send_keys(password)
    time.sleep(2)
    driver.find_element_by_id('passwordc').send_keys(password)
    time.sleep(2)
    driver.find_element_by_class_name('signUpProcess-btn-create').click()
    time.sleep(1)
    driver.find_element_by_id('confirmModalBtn').click()
