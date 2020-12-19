from bs4 import BeautifulSoup;
from selenium import webdriver;
import requests,webbrowser,os;
import pyinputplus as pyip;

os.makedirs("comic",exist_ok=True);

try:

    search=pyip.inputStr("What image you want to search for:");
    print("Ctrl+c to quit.")
    imageur=requests.get("https://imgur.com/search?q="+search);

    imageur.raise_for_status();

    soup=BeautifulSoup(imageur.text,"html.parser");

    response=soup.select("#imagelist img")
    for i in range(len(response)):
        page_1_img="https:"+response[i].get("src");
        print("Downloading image %s"%page_1_img);
        downlaod_img=requests.get(page_1_img)
        downlaod_img.raise_for_status()
        image_file=open(os.path.join("comic",os.path.basename(page_1_img)),"wb");
        for chunk in downlaod_img.iter_content(1000000):
            image_file.write(chunk);
        image_file.close();
    print("Done.");

except :
    print("An error has occured.");