import pyperclip,re;
phonenumber=re.compile('''(
(\d{3}|\(\d{3}\))?
(\s|-|\.)?
(\d{3})
(\s|-|\.)
(\d{4})
(\s*(ext|x|ext.)\s*(\d{2,5}))?
)''',re.VERBOSE)

email=re.compile('''(
[A-Za-z0-9.%-+-]+
@
[A-Za-z0-9.-]+
(\.[a-zA-Z]{2,4})
)''',re.VERBOSE)

text=str(pyperclip.paste());
matches=[]
for i in phonenumber.findall(text):
    number='-'.join([i[1],i[3],i[5]]);
    if(i[8]!=''):
        phonenumber+='x'+i[8];
    matches.append(number);
for i in email.findall(text):
    matches.append(i[0])
if len(matches)>0:
    pyperclip.copy('\n'.join(matches));
    print("copied to clipboard");
    print('\n'.join(matches));
else:
    print("no phone number found.")
