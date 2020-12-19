import sys;
try:
    import random,time,copy;
    WIDTH = 60;
    HEIGHT = 20;

    #CREATE A LIST OF LIST FOR CELLS
    nextCells=[];
    for x in range(WIDTH):
        column=[]; #CREATE A NEW COLUMN
        for y in range(HEIGHT):
            if random.randint(0,1)==0:
                column.append("#") #ADD A LIVING CELL
            else:
                column.append(' ') #ADD A DEAD CELL
        nextCells.append(column);
    while  True: #Main PROGRAM LOOP
        print('\n\n\n\n\n'); # SEPRATE EACH OTHER WITH NEWLINE
        currentCells=copy.deepcopy(nextCells)
        # PRINT CURRENTCELLS ON THE SCREEN
        for y in range(HEIGHT):
            for x in range(WIDTH):
                print(currentCells[x][y],end='');
            print();
        for x in range(WIDTH):
            for y in range(HEIGHT):
                # GET NEIGHBOURING COORDINATES
                # %WIDTH ensures leftcordinates is always between 0 and width -1
                leftCoord=(x-1)%WIDTH;
                rightCoord=(x+1)%WIDTH;
                aboveCoord=(y-1)%HEIGHT;
                belowCoord=(y+1)%HEIGHT;

                numNeighbours=0;
                if(currentCells[leftCoord][aboveCoord]=='#'):
                    numNeighbours+=1;
                if(currentCells[leftCoord][belowCoord]=='#'):
                    numNeighbours+=1;
                if(currentCells[rightCoord][aboveCoord]=='#'):
                    numNeighbours+=1;
                if(currentCells[rightCoord][belowCoord]=='#'):
                    numNeighbours+=1;
                if(currentCells[x][aboveCoord]=='#'):
                    numNeighbours+=1;
                if(currentCells[x][belowCoord]=='#'):
                    numNeighbours+=1;
                if(currentCells[rightCoord][y]=='#'):
                    numNeighbours+=1;
                if(currentCells[leftCoord][y]=='#'):
                    numNeighbours+=1;
                #set cell based on conway game of life rules
                if(currentCells[x][y]=='#'and (numNeighbours==2 or numNeighbours==3)):
                    nextCells[x][y]='#'
                elif(currentCells[x][y]==' 'and numNeighbours==3):
                    nextCells[x][y]='#'
                else:
                    nextCells[x][y]=' ';
        time.sleep(1);
except KeyboardInterrupt:
    print("---------------BYE------------------------");
    sys.exit(); 