import random
import time
import os
import platform

NUMBER_OF_RACERS = 6
FINISH_LINE_MARKER = 70
MARKER = "*"
FINISH = "FINISH"

def next_step(standing, not_finished):

    winner = list()

    #while not_finished:

    #one step further
    for i in range(NUMBER_OF_RACERS):
        help = standing[i]
        standing[i] = int(help + int(random.randrange(0,9)))
       # standing[i] = 5
        if standing [i] > FINISH_LINE_MARKER:
            not_finished = False
            winner.append(i + 1 )

    drawPage(standing, winner, not_finished)

#        print (line)
#        time.sleep(1)
    return not_finished

#determine the winner

    for n, _  in enumerate (winner):
        print ("Winner #",n+1,"is",_) 

#function is based on the assumption: NUMBER_OF_RACERS = 6  
def drawPage(standing,winner,not_finished):
    
    
    #prepare drawing
    line=""
    for _ in range(FINISH_LINE_MARKER):
        line=line + "-"
    line += "<br>"

    with open('MinimalisticRefresh.html', 'w') as file:

        for _ in range(NUMBER_OF_RACERS):
            file.write (line)
            currentLine = ""
            toCountTo = 0
            if standing[_] >= FINISH_LINE_MARKER:
                toCountTo = standing[_]
            else:
                toCountTo = FINISH_LINE_MARKER
        
            for i in range (1,toCountTo+1):
                if (i == standing[_]):
                    currentLine += MARKER
                elif (i == FINISH_LINE_MARKER):
                    currentLine += FINISH[_]
                else:
                    currentLine += "&nbsp;"
            currentLine += "<br>"
            
            file.write (currentLine)
        
        if not not_finished:
            file.write("The winner is: " + str(winner[0]))
            
  #  print("End of Round")



