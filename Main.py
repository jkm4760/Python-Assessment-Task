#################################
#     Python Assesment Task 1:  #
#            Hangman            #
#################################
import sys, time
from os import system
from random import randint

#Main Game function
def Game(word):
    system('cls')
    #Read the word into a list for easy editing
    word_ls = []
    for char in word:
        word_ls.append(char.capitalize()) #capitalize everything so as to avoid conflicts

    #Initialize a display list
    display_ls = []
    for i in word_ls:
        display_ls.append('_')
    

    correct = 0 #keep a record of how many we get correct
    incorrect = 0 #...and how many we get wrong :D
    used_letters = [] #Used to show letters that are used, and cannot be used again
    prev_correct = 0 #used to check if they got something wrong

    while correct != len(word_ls):
        #Game loop

        #Make sure input is valid
        Boolean = True
        while Boolean == True:
            Boolean = False #set to false, meaning while will only loop if conditions are met

            render_graphic(incorrect) #render our stickman
            print 'Word: ' + ' '.join(display_ls)
            print 'Used: ' + ' '.join(used_letters)

            inp = raw_input('Letter: ')
            if len(inp) != 1: #not a single charachter
                Bolean = True
                system('cls')
            for char in used_letters: #already used that letter
                if inp.capitalize() == char:
                    Boolean = True
                    system('cls')

        prev_correct = correct #initialize previous correct var

        for i in range(len(word_ls)): #iterate through the word
            if inp.capitalize() == word_ls[i]: #if the letter matches a letter in the word
                correct += 1 #you got one right!
                display_ls[i] = word_ls[i] #make sure they can see it :D

        if prev_correct == correct: #they didnt get anything :(
            incorrect += 1

        used_letters.append(inp.capitalize()) #We've used this letter now, lets disable it

        system('cls')

        if incorrect == 8:
            print '''Naww, sadfaec. You didnt get it.
The word was ''' + word + '''!
Better luck next time!'''
            playAgain()

    print word + '''!\nYou got it! Congratulations!
It took you '''+str(len(used_letters))+''' tries.'''  #You won! GRATS!
    playAgain()

def render_graphic(i): #just a nice function to render our buddy the stickman
    graphic = ['\n\n\n\n\n\n\n',
               '\n\n\n\n\n\n---------',
               '\n |\n |\n |\n |\n |\n-|-------',
               ' _____\n |\n |\n |\n |\n |\n-|-------',
               ' _____\n |   |\n |\n |\n |\n |\n-|-------',
               ' _____\n |   |\n |   O\n |   |\n |\n |\n-|-------',
               ' _____\n |   |\n |   O\n |  /|\\\n |\n |\n-|-------',
               ' _____\n |   |\n |   O\n |  /|\\\n |  / \\\n |\n-|-------']
    print graphic[i]

#Who knows? maybe you WANT to be thwarted yet again!
def playAgain():
    global mode
    
    b = True
    while b == True:
        inp = raw_input('\nDo you want to play again?\n   [y/n]: ')
        if inp.capitalize() == 'Y':
            system('cls')
            if mode == 1:
                RandomWord()
            elif mode == 2:
                CustomWord()
        elif inp.capitalize() == 'N':
            Menu()
        else:
            system('cls')
            print 'Sorry, i don\'t understand that command.'
            playAgain()

#Entry Function
def RandomWord():
    global mode
    #Import our overly-hugemongeous dictionary file. its olnly like 54277 words or so :3
    dic = open('dictionary.dic', 'r')
    wordlist = dic.readlines()

    num = randint(0,len(wordlist))
    word = wordlist[num]
    word = word[0:len(word)-1] #seems to be adding a mysterious char to the end. this should fix 'er
    mode = 1
    Game(word)

def CustomWord():
    global mode
    system('cls')
    word = raw_input('Please enter a word or phrase:\n')
    mode = 2
    Game(word)

def Credits():
    system('cls')
    text = '''##########################
#        CREDITS         #
#                        #
#      Saxon Landers     #
#    ~AClockWorkLemon~   #
#                        #
#      Jamie Stewart     #
#       ~Zoralord~       #
##########################\n'''
    printText(text)
    a = raw_input('Press enter to return to menu...')
    Menu()

def Menu(b = False):
    system('cls')
    text = '''##########################
#      PyHangman v1      #
#                        #
#  [1] Random word       #
#  [2] Pick a word       #
#                        #
#  [c] Credits           #
#  [q] Quit              #
##########################\n'''
    printText(text)
    if b:
        print 'Invalid choice. Please choose an appropriate option!'
    inp = raw_input('   Choice: ')
    if inp == '1':
        RandomWord()
    elif inp == '2':
        CustomWord()
    elif inp.capitalize() == 'C':
        Credits()
    elif inp.capitalize() == 'Q':
        quit()
    else:
        Menu(False)

def printText(text):
    for character in text:
        sys.stdout.write(character);sys.stdout.flush(),time.sleep(.01)

#Application Entry Point
mode = 0
Menu()

