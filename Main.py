#################################
#     Python Assesment Task 1:  #
#            Hangman            #
#################################

#Main Game function
def Game(word):
    #Read the word into a list for easy editing
    word_ls = []
    for char in word:
        word_ls.append(char.capitalize()) #capitalize everything so as to avoid conflicts

    #Test word list
    print word_ls

#Entry Function
def Main():
    inp = raw_input('(TEMP) Enter Word: ')
    Game(inp)

#Application Entry Point
Main()
