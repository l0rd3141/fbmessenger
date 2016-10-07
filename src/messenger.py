#Import necessary modules

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys,os
import time
from bs4 import BeautifulSoup
email_id=raw_input("Enter the email: ")
password=raw_input("Enter your password: ")
message=raw_input("Enter your message, Hit enter if you want a generic message: ")
#Can take custom message from input
if(message==""):
    message="Hey,Thanks for your message, I will reply as soon as I can"


#Calculate the number of message received
def message_number(html_file):
    soup = BeautifulSoup(html_file,"lxml")
    unrefined_msg = soup.find('span',id='u_0_f')
    refined_msg = unrefined_msg.span.contents
    unicode_val = refined_msg[0]
    number_of_message = int(unicode_val)
    return number_of_message

#Load Selenium for work
browser = webdriver.Chrome()
browser.get("http://facebook.com")
email = browser.find_element_by_id("email")
email.send_keys(email_id)
passwd = browser.find_element_by_id("pass")
passwd.send_keys(password)
passwd.send_keys(Keys.ENTER)
time.sleep(2)

message_count = message_number(browser.page_source)
browser.get("http://facebook.com/messages")
msg_box = browser.find_element_by_css_selector("textarea.uiTextareaNoResize.uiTextareaAutogrow._1rv")

#Temporary workaround, hoping to build something better
for val in range(10):
    msg_box.send_keys(Keys.UP)
x=0
while(x<message_count):
    #browser.get("http://facebook.com/messages")
    msg_box = browser.find_element_by_css_selector("textarea.uiTextareaNoResize.uiTextareaAutogrow._1rv")
    msg_box.send_keys(message)
    msg_box.send_keys(Keys.ENTER)
    msg_box.send_keys(Keys.DOWN)
    time.sleep(2)
    x=x+1

