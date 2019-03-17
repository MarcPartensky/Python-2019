from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from PIL import Image

import smtplib
import credentials
import pyautogui
import urllib


import random
alea=lambda :str(random.randint(1000,10000))
password="je te chie un mot de passe"

import time

receiver="valentin.colin78@gmail.com"
title="enorme test"
message="tu pues vraiment la merde"




def createMail(adress="unnamed.beaucoup",password="password"):
    try:
        url = 'https://protonmail.com/'
        driver = webdriver.Chrome('/Users/olivierpartensky/Programs/Library/Selenium/chromedriver')
        action = webdriver.common.action_chains.ActionChains(driver)
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
        time.sleep(2)
        driver.find_element_by_id('confirmModalBtn').click()
        time.sleep(2)
        element=driver.find_element_by_id('id-signup-radio-captcha')
        element.click()
        #element=driver.find_element_by_id('id-signup-radio-donate')
        action.move_to_element_with_offset(element,20,160)
        action.click()
        action.perform()
        time.sleep(2)
        #img=driver.find_element_by_xpath('//*[@id="rc-imageselect-target"]') #/table/tbody/tr[1]/td[1]/div/div[1]/img
        #xpath    //*[@id="rc-imageselect-target"]/table/tbody/tr[1]/td[1]/div/div[1]/img
        element=driver.find_element_by_tag_name("html")
        element.send_keys(Keys.END)
        time.sleep(2)
        driver.save_screenshot("captcha.png")


        #src=img.get_attribute('src')
        time.sleep(2)
        #urllib.urlretrieve(src,"captcha.png")
        Img=Image.open("captcha.png")
        Img.show()

        #x,y=element.location["x"],element.location["y"]
        #pyautogui.moveTo(x,y)
        #print(pyautogui.position())
        #time.sleep(2)
        #pyautogui.moveTo(x+50,y)
        #driver.find_element_by_class_name('recaptcha-checkbox-checkmark').click()
        #print(pyautogui.position())
        #time.sleep(2)
        print("Email created.")
    except:
        raise Exception("Failed to create email adress.")


def sendMail(title,message,receiver):
    try:
        server=smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(credentials.SENDER,credentials.PASSWORD)
        message='Subject: {}\n\n{}'.format(title,message)
        server.sendmail(credentials.SENDER,receiver,message)
        server.quit()
        print("Email sent.")
    except:
        raise Exception("Failed to send email.")

createMail(password=password)
#sendMail(title,message,receiver)
