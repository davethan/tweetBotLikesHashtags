# -*- coding: utf-8 -*-
"""
Created on Fri May 29 15:03:07 2020

@author: danis
"""
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

class TwitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox(executable_path="C:\\Users\\danis\\Downloads\\geckodriver.exe")
        
    def login(self):
        bot = self.bot
        bot.get("https://twitter.com/login/")
        time.sleep(10)
        email = bot.find_element_by_name("session[username_or_email]")
        password = bot.find_element_by_name("session[password]")
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(10)
        
    def like_tweets(self, hashtag):
        bot = self.bot
        bot.get('https://twitter.com/search?q=%23'+hashtag+'&src=typed_query')
        time.sleep(10)
        for i in range(1,3):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(10)
            tweetLinks = [i.get_attribute('href')
            for i in bot.find_elements_by_xpath("//a[@dir='auto']")]
            filteredLinks = list(filter(lambda x: 'status' in x,tweetLinks))

            for link in filteredLinks :
                    bot.get(link)
                    time.sleep(5)
                    try:
                        bot.find_element_by_xpath("//div[@data-testid='like']").click()
                        time.sleep(10)
                    except Exception :
                        time.sleep(10)

robot = TwitterBot("danis_desipris@hotmail.com", "that is not my password")
robot.login()
robot.like_tweets("nimportequoi")
        