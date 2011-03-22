#################################
#     Python Assesment Task 1:  #
#            Hangman            #
#################################

from os import system

#Main Game function
def Game(word):
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
The word was''' + word + '''!
Better luck next time!'''
            playAgain()

    print '''You got it! Congratulations!
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
    b = True
    while b == True:
        inp = raw_input('\nDo you want to play again?\n   [y/n]: ')
        if inp.capitalize() == 'Y':
            system('cls')
            Main()
        elif inp.capitalize() == 'N':
            quit()
        else:
            system('cls')
            print 'Sorry, i don\'t understand that command.'
            playAgain()

#Entry Function
def Main():
    inp = raw_input('(TEMP) Enter Word: ')
    Game(inp)

#Application Entry Point
Main()
