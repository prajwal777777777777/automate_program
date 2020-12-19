import pyautogui,time
moves=1
print("program running.".center(40,"-"))
current_time=int(time.time())
while True:
    a=pyautogui.position()
    if(moves%2==0):
        first,second=a.x+1,a.y+1
        pyautogui.moveTo(first,second)
        time.sleep(10);
    else:
        first,second=a.x-1,a.y-1
        pyautogui.moveTo(first,second)
        time.sleep(10);
    moves+=1
