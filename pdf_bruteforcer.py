import PyPDF2,os;
import pyinputplus as pypi;
cracked_prompt="password cracked";
dictionary_file=open("/home/your_Path/automate_additional/pdf_file/dictionary.txt");
password=dictionary_file.readlines();
new_list=[]

for i in password:
    password=i.strip("\n")
    new_list.append(password)


new_files=[]
for directory,sub,files in os.walk("/home/your_Path/automate_additional/pdf_file"):
    for fil in files:
        if(fil.endswith("_encrypted.pdf")):
            new_files.append(fil);


for encrypted in new_files:
    pdffile=open("/home/your_Path/automate_additional/pdf_file/"+encrypted,"rb");
    pdfread=PyPDF2.PdfFileReader(pdffile);
    print(f"Preapring to crack password for {encrypted} file.")
    for i in new_list:
        print(f"Trying password {i}");
        a=pdfread.decrypt(i);
        if(a==1):
            print(cracked_prompt.center(40,'-')+"\n"+f"password={i}"+"\n"+f"file={encrypted}");
            break;
        else:
            pass;
    if(a==0):
        print("password not found in provided wordlist.");
    ask_again=pypi.inputYesNo(prompt="Do you want to try for another file[Y/N]:").lower();
    if(ask_again=="yes" or ask_again=="y"):
        pass;
    elif(ask_again=="no" or ask_again=="n"):
        print('Bye'.center(40,'-'));
        break;
    else:
        pass;
    
