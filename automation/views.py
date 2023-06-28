from django.shortcuts import render
from django.http import HttpResponse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time
import random

def automate_chrome(request):
    # create a new Chrome browser instance
    s = Service()

    chrome_options = Options()
    chrome_options.add_argument("--incognito")

    chrome_options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(service=s, options=chrome_options)

    #Pass Generator

    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNIPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "!@#$%^&*,?"
    all = lower + upper + numbers + symbols
    length = 10
    password = "".join(random.sample(all, length))

    #Emails Generator

    def random_line(frame):
        lines = open(frame).read().splitlines()
        return random.choice(lines)

    val = (random_line('automation/emails.txt'))

    #UserName Generator

    us = upper + lower
    user = "".join(random.sample(us, length))

    # direct the browser to the URL
    #driver.get('https://www.google.com')

    driver.get("https://app.celia.finance/register?referral_code=52JSILCLT")

    driver.find_element("xpath","//*[@id='validationCustom02']").send_keys(val);

    driver.find_element("xpath","//*[@id='validationCustom03']").send_keys(password);

    driver.find_element("xpath","/html/body/div[1]/div[3]/div/div/form/div[6]/button").click();

    driver.find_element("xpath","/html/body/div[1]/div[3]/div/div/form/div[2]/input").send_keys(user);

    driver.find_element("xpath","/html/body/div[1]/div[3]/div/div/form/div[3]/select").click();

    driver.find_element("xpath","/html/body/div[1]/div[3]/div/div/form/div[3]/select/option[17]").click();


    driver.find_element("xpath","/html/body/div[1]/div[3]/div/div/form/div[4]/div[1]/input").click()


    time.sleep(10)

    # your automation code here

    # don't forget to quit the browser once finished
    driver.quit()

    return HttpResponse("Task completed")
