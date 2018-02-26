import random
column1 = (1,2,3)
column2 = (2,3)
column3 = (2,3)
column4 = (2,3)
column5 = (2,3,4)
player= "                                  O"
enter = "                                ---||||||||||||||"
maze1 = "                                ||1||----||----||"
maze2 = "                                ||2||2||2||2||2||"
maze3 = "                                ||3||3||3||3||3||"
maze4 = "                                ||----||----||4||"
leave = "                                ||||||||||||||---"


def start():
    print("Want to start? (Yes, No)")
    decision = raw_input("Answer:")
    if decision == "Yes":
        print
        maze()

def maze():
    print player
    print enter
    print maze1
    print maze2
    print maze3
    print maze4
    print leave
    
    
start()
