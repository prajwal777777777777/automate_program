import os;
from PIL import Image;

path="/your/image/folder";
logo_file="/your/logo/folder";



#TODO:opening logo_file
cat_logo=Image.open(logo_file);

try:
    #todo:iterating over the image file
    for file in os.listdir(path):

        copy_cat=cat_logo.resize((200,200))                        #todo:resizing logo image with 200,200
        new_width,new_height=cat_logo.size;                        #todo:saving width and height as variable which contain 200,200.


        if(file.endswith(".jpeg") or file.endswith(".png") or file.endswith(".jpg") or file.endswith(".bmp") or file.endswith(".gif")):      #todo:getting jpeg png and jpg file.
            real_image=Image.open(path+file);                                      #todo:opening image file with absolute path
            image=real_image.copy()                                                #todo:copying real_image in variable image/
            
            image_width,image_height=image.size;
            #todo:opening all image of folder and getting the width and height.

            if(image_width<200 and (image_height>200 and image_height<600)):
                image=image.resize((600,600));
                new_logo=copy_cat.resize((100,100))
                print("resizing image",file)
                
            
            elif(image_height<200 and (image_width>200 and image_width<600)):
                new_logo=copy_cat.resize((100,100))
                image=image.resize((600,600));
                print("resizing image",file)
                
            
            elif(image_height<200 and image_width<200):
                image=image.resize((600,600));
                new_logo=copy_cat.resize((100,100))
                print("resizing image",file)
                
            
            else:
                new_logo=copy_cat
                pass;
            #todo:if else condition

            #todo:basically these logic are making width and height 600 if any of it are less than 600.

            image_width,image_height=image.size;
            #todo:again getting image_width and image_height as we can modify some image (i.e which has less than 600 width and height)

            os.makedirs("/where/u/want/to/make/new_folder/",exist_ok=True); #todo:making new directory to save all image with logo
            
            
            
            image.paste(new_logo,((image_width-new_logo.width),(image_height-new_logo.height)),new_logo)
            #todo:if new_logo witdh and height are less than equal to 600 the logo size will be 100 else 200.
            #todo:pasting the logo at the end like this ------------
                                            #todo:     |         __|  -200 width(horizantol) or 100
                                        #todo           |________|__|  -200 height(vertical)  or 100

            
            image.save(f"/where/u/want/to/make_new_folder/{file}");
            #todo:saving image with same name in spoecified folder
        else:
            print("program only supports png,gif,jpeg,jpg,bmp with lowercase.")
except:
    print("An unknow error has occured.");
    