import time
print("Press enter to continue and ctrl + c to exit the program.");
try:
    def function():
        input()
        print("Program started");
        lapnum=1;
        starttime=time.time()
        laptime=starttime
        while True:
            input();
            laptimes=round(time.time()-laptime,2)
            totaltime=round(time.time()-starttime,2)
            print("Lap #%s   %s   %s"%(lapnum,laptimes,totaltime))
            laptime=time.time()
            lapnum+=1
    function();
except:
    print("\nBYE") ;       
