import random

def intro():
    print('Welcome to my game of random trivia!')
    print
    print('Go/Close')
    print
    answer = raw_input('Decision: ')
    print
    if answer == 'Go' or answer == 'go':
    	print
        thequiz()
        print
    if answer == 'Close' or answer == 'close':
        print('see ya!')
        print
    else:
        print('boi can you read')
        answer = raw_input('Answer: ')
        print
        print
        intro()

def thequiz():
    print('HERE WE GO!')
    questionlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    points = 0
    while (len(questionlist) != 0):
        q1 = 'Who is Billy Herrington?',
        q2 = 'How do you open a locked graveyard?', 
        q3 = 'Who invented the first electrostatic generator?',
        q4 = 'When does the Night of Walpurgis start?', 
        q5 = "Who was Cu Chulainn's mentor?",
        q6 = "What was the name of King Arthur's Spear?"
        q7 = 'Who was Mordred?'
        q8 = 'When did the Great Spanish Armada set sail for Britain??'
        q9 = 'Who shot first?'
        q10 = 'Who was the mom of Mordred?'
        question = random.choice(questionlist)
        if question == 1:
            questionlist.remove(1)
            print q1
            print('a)The Boss of the Gym')
            print('b)Who?')
            print('c)That muscular guy')
            print('d)( ͡° ͜ʖ ͡°)')
            guess = raw_input('Answer: ')
            if guess == 'A' or guess == 'a':
                print 'Aw yea boii'
                points += 1
                print
            else:
                print('W R O N G')
                print
                
        if question == 2:
            questionlist.remove(2)
            print q2
            print('a)With a skeleton key')
            print('b)You break in')
            print('c)Who locks graveyards?')
            print('d)Why would you break in a graveyard?')
            guess = raw_input('Answer: ')
            if guess == 'a' or guess == 'A':
                points += 1
                print
            else:
                print('W R O N G')
                print
                
        if question == 3:
            questionlist.remove(3)
            print q3
            print('a)Rudolf von Nezrouge')
            print('b)Otto von Guericke')
            print('c)Nikola Tesla')
            print('d)Elon Musk')
            guess = raw_input('Answer: ')
            if guess == 'b' or guess == 'B':
                print ('a y y')
                points += 1
                print
            else:
                print('W R O N G')
                
        if question == 4:
            questionlist.remove(4)
            print q4
            print('a)April 28')
            print('b)April 29')
            print('c)April 30')
            print('d)April 31')
            guess = raw_input('Answer: ')
            if guess == 'c' or guess == 'C':
                print ('ayy')
                points += 1
                print
            else:
            	print ('W R O N G')
        if question == 5:
             questionlist.remove(5)
             print q5
             print('a)Fergus mac Roich')
             print('b)Beowulf')
             print('c)Scathach')
             print('d)Lugh')
             guess = raw_input('Answer: ')
             if guess == 'c' or guess == 'C':
                 print ('ayyy')
                 points += 1
                 print
             else:
                print('W R O N G')      
        if question == 6:
             questionlist.remove(6)
             print q6
             print('a)Speart')
             print('b)Rhongomyniad')
             print('c)Carnwennan')
             print('d)Clarent')
             guess = raw_input('Answer: ')
             if guess == 'b' or guess == 'B':
                 print('ayyy')
                 points += 1
                 print
             else:
                 print('W R O N G')
                 print
        if question == 7:
            questionlist.remove(7)
            print q7
            print('a)The rebellious son of King Arthur')
            print('b)A knight')
            print('c)Who?')
            print('d)The offspring of incest')
            guess = raw_input('Answer: ')
            if guess == 'a' or guess == 'A':
                print ('ayy')
                points += 1
                print
            else:
                print('W R O N G')
        if question == 8:
            questionlist.remove(8)
            print q8
            print('a)1588')
            print('b)1602')
            print('c)1592')
            print('d)1560')
            guess = raw_input('Answer: ')
            if guess == 'a' or guess == 'A':
                print ('a y y')
                points += 1
                print
            else:
                print('W R O N G')
        if question == 9:
            questionlist.remove(9)
            print q9
            print('a)Greedo')
            print('b)Han')
            guess = raw_input('Answer: ')
            if guess == 'b' or guess == 'B':
                print ('a y y')
                points += 1
            else:
                print('W R O N G')
        if question == 10:
            questionlist.remove(10)
            print q10
            print('a)Morguase')
            print('b)Morganna le Fay')
            print('c)Merlin')
            print('d)The Lady of the Lake')
            guess = raw_input('Answer: ')
            if guess == 'a' or guess == 'A':
                print('a y y')
                print
                points += 1
            else:
                print('W R O N G')


intro()