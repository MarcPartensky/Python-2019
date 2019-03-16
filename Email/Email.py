from selenium import webdriver
import time

def createMailAddress(adress,password):
    try:
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
    except:
        raise Exception("Failed to create email adress.")


def sendEmail(subject,msg,receiver):
    try:
        server=smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(credentials.SENDER, credentials.PASSWORD)
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(credentials.SENDER, receiver, message)
        server.quit()
        print("Success: Email sent!")
    except:
        print("Email failed to send.")
