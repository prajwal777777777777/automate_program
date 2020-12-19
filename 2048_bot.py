from selenium import webdriver;
import random;
from selenium.webdriver.common.keys import Keys;
try:
    browser=webdriver.Firefox();
    browser.get("https://play2048.co/");
    html=browser.find_element_by_tag_name("html");

    lists=[Keys.LEFT,Keys.RIGHT,Keys.DOWN,Keys.UP]
    while True:
        random_num=random.choice(lists)
        html.send_keys(random_num);
        if(browser.find_element_by_class_name('retry-button').text)=="Try again":
            choice=input("Print u want to play again[y/n]:");
            if(choice=="y"):
                browser.find_element_by_class_name('retry-button').click();
            else:
                break;
            
    print("bye");
except:
    print("An error has occured.")