import os;
from PIL import Image;

path="/your/path/to/search";           #todo:we specify the path to search for.


try:
    for directory,sub,files in os.walk(path):                         #todo:we are searching filesfor each and every folder in path.
        numoffile=0                                     #todo:for counting file 
        for file in files:                              #todo:checking files.

            if(file.endswith(".jpg") or file.endswith(".png") or file.endswith(".bmp") or file.endswith(".gif")):
                #todo:if file ends with the following extension it will pass(image).
                image=Image.open(directory+"/"+file);
                width,height=image.size
                
                #todo:opening image and getting its size.

                if((width and height)>500):

                    file_abs_path=directory+"/"+file
                    numoffile+=1
                    print("%s"%(file_abs_path));
                    #todo:getting absoulute path of image in file_abs_path and counting the files.
                else:
                    pass;
                    #todo:if the size of image is less than 500 we are not counting that as image.
        
        #todo:after it finishes one image folder it will break and come here and below conditon will check if the folder really contains image by giving condition num_of_file>1.
        if(numoffile>=1):
            print(f"\n{directory} contains {numoffile} images\n".center(200,"-"));
        #todo:we are printing this for every folder if it contains image.
except KeyboardInterrupt:
    print("bye.");
except:
    print("An unknown error has occured.");
    #todo:handling errors