from bs4 import BeautifulSoup;
import os,requests;

url="https://www.xkcd.com"
os.makedirs("comic",exist_ok=True);

while not url.endswith("#"):
    print("Downloading page %s"%url);
    response=requests.get(url)
    response.raise_for_status();
    soup=BeautifulSoup(response.text,"html.parser")
    comic_elem=soup.select("#comic img");
    if(comic_elem==[]):
        print("image could not be found.");
    else:
        image_url=comic_elem[0].get("src");
        complete_url="https:"+image_url;
        print("Downloading image %s"%complete_url);
        image=requests.get(complete_url);
        image.raise_for_status()
        image_file=open(os.path.join("comic",os.path.basename(complete_url)),"wb")
        for chunk in image.iter_content(100000):
            image_file.write(chunk);
        image_file.close();
        prevlink=soup.select('a[rel="prev"]')[0]
        url="https://xkcd.com"+prevlink.get("href");
print("done");