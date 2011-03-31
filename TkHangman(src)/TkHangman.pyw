from Tkinter import *
import string, tkSimpleDialog
from random import randint

class MainMenu(Frame):

    #Constructor
    def __init__(this):
        Frame.__init__(this, bg='#CCCCCC')
        this.pack(expand=YES)
        this.master.title('TkHangman v1')
        this.master.iconname('tkhm1')
        this.master.iconbitmap(".\icon.ico")

        #Title :D
        img = PhotoImage(file='header.gif')
        title = Label(this, image=img, borderwidth=0)
        title.img = img
        title.pack(side=TOP)

        #INIT MENU BUTTONS
        btn_random = Button(this, text='Random Word', width = 20, command=this.random_word)
        btn_random.pack(side=TOP)

        btn_custom = Button(this, text='Custom Word', width = 20, command=this.custom_word)
        btn_custom.pack(side=TOP)

        #spacer
        Label(this, bg='#CCCCCC').pack(side=TOP)

        #credits button :)
        btn_random = Button(this, text='Credits', width = 20, command=this.credits)
        btn_random.pack(side=TOP)

    def random_word(this):
        #Import our overly-hugemongeous dictionary file. its only like 54277 words or so :3
        dic = open('dictionary.dic', 'r')
        wordlist = dic.readlines()

        num = randint(0,len(wordlist))
        word = wordlist[num]
        word = word[0:len(word)-1] #seems to be adding a mysterious char to the end. this should fix 'er
        mode = 1
        this.destroy()
        MainWindow(word)


    def custom_word(this):
        inp = tkSimpleDialog.askstring('Custom Word', 'Enter a custom word', parent=this)

        temp = True
        if inp != None:
            for char in inp: #check that the input i in bounds
                for i in string.punctuation:
                    if char == i:
                        temp = False
                for i in string.digits:
                    if char == i:
                        temp = False
                for i in string.whitespace:
                    if char == i:
                        temp = False
        else:
            temp = False
            
        if temp == True:
            this.destroy()
            test = MainWindow(inp)
            test.mainloop()

    def credits(this):
        this.destroy()
        creds = MessageBox(PhotoImage(file='credits.gif'),'Saxon Landers\n~AClockWorkLemon~\n\nJamie Stewart\n~Zoralord~')
        creds.mainloop()
        


class MainWindow(Frame):
    #vars
    out_img = Label()
    out_text = Label()
    out_err = Label()
    
    inp_field = Entry()

    word = ''

    correct = 0 #keep a record of how many we get correct
    incorrect = 0 #...and how many we get wrong :D
    used_letters = [] #Used to show letters that are used, and cannot be used again
    prev_correct = 0 #used to check if they got something wrong

    chars = 0

    word_ls = []
    display_ls = []
    
    graphic = [] #Padder
    
    #Constructor
    def __init__(this, word):

        this.reset_vars()

        #set the word :)
        this.word = word
        
        #Init the frame
        Frame.__init__(this, bg='#CCCCCC')
        this.pack(expand=YES, fill=BOTH)
        this.master.title('TkHangman v1')
        this.master.iconname('tkhm1')

        #out_img label
        this.out_img = Label(this)
        this.out_img.pack(expand=YES, fill=BOTH, side=TOP)

        #out_text Label
        this.out_text = Label(this, justify=LEFT, bg='#CCCCCC')
        this.out_text.pack(expand=YES, side = TOP)
        
        #Entry field
        this.inp_field = Entry(this)
        this.inp_field.pack(expand=NO, fill=BOTH, side=TOP)
        
        #Error Display
        this.out_err = Label(this, fg='red', justify=LEFT, bg='#CCCCCC')
        this.out_err.pack(expand=YES, fill=BOTH, side = BOTTOM)

        #Init lists
        #Read the word into a list for easy editing
        for char in this.word:
            this.word_ls.append(char.capitalize()) #capitalize everything so as to avoid conflicts 
            for i in string.ascii_uppercase:
                if char.capitalize() == i:
                    this.chars += 1

        #Initialize a display list
        for i in this.word_ls:
            if i == ' ':
                this.display_ls.append(' ')
            elif i == '-':
                this.display_ls.append('-')
            elif i == '\'':
                this.display_ls.append('\'')
            else:
                this.display_ls.append('_')

        #initial render
        this.render()
        
        #bind the enter key to the EnterPressed Function
        this.inp_field.bind('<Return>', this.EnterPressed)
        #bind keypresses, so we can restrict length
        this.inp_field.bind('<KeyPress>', this.RestrictKeys)

    def reset_vars(this):
        this.out_img = Label()
        this.out_text = Label()
        this.out_err = Label()
        this.inp_field = Entry()
        this.word = ''
        this.correct = 0
        this.incorrect = 0
        this.used_letters = []
        this.prev_correct = 0
        this.chars = 0
        this.word_ls = []
        this.display_ls = []
        this.graphic = [PhotoImage(file='0.gif'),
               PhotoImage(file='1.gif'),
               PhotoImage(file='2.gif'),
               PhotoImage(file='3.gif'),
               PhotoImage(file='4.gif'),
               PhotoImage(file='5.gif'),
               PhotoImage(file='6.gif'),
               PhotoImage(file='7.gif'),
               PhotoImage(file='8.gif'),
               PhotoImage(file='9.gif'),
               PhotoImage(file='9.gif')] #Padder

    def setWord(this, newWord):
        this.word = newWord

    def RestrictKeys(this, event):
        inp = this.inp_field.get()
        
        if len(inp) > 0:
            this.inp_field.delete(0, END)
        

    def EnterPressed(this, event):
        inp = this.inp_field.get()
        

        for char in this.used_letters: #already used that letter
                if inp.capitalize() == char:
                    this.clearInp('You have already used that letter!')
                    return
        temp = False
        for char in string.ascii_uppercase:
            if inp.capitalize() == char:
                temp = True
        if temp == False:
            this.clearInp('Invalid Symbol')
            return

        this.prev_correct = this.correct

        for i in range(len(this.word_ls)): #iterate through the word
            if inp.capitalize() == this.word_ls[i]: #if the letter matches a letter in the word
                this.correct += 1 #you got one right!
                this.display_ls[i] = this.word_ls[i] #make sure they can see it :D
                
        if this.prev_correct == this.correct: #they didnt get anything :(
            this.incorrect += 1

        this.used_letters.append(inp.capitalize()) #We've used this letter now, lets disable it

        this.render()
        
        this.clearInp()

        #win/loose conditions
        if this.correct == this.chars:
            this.destroy()
            creds = MessageBox(PhotoImage(file='win.gif'),'It took you '+str(len(this.used_letters))+' letters to get \''+this.word+'\'.')
            creds.mainloop()
            
        if this.incorrect == 10: #CHANGE TO CORRECT NO OF IMGS
            this.destroy()
            creds = MessageBox(PhotoImage(file='loose.gif'),'The word was \''+this.word+'\'.')
            creds.mainloop()

    def render(this):
        this.out_text['text'] = 'Word: ' + ' '.join(this.display_ls) + '\nUsed: ' + ' '.join(this.used_letters)
        this.out_img['image'] = this.graphic[this.incorrect]

    def clearInp(this, error = ''):
        this.out_err['text'] = error
        this.inp_field.delete(0, END)

class MessageBox(Frame):
    #Used to show the player a message
    def __init__(this, img, message='Default', bgcolour='#CCCCCC'):

        Frame.__init__(this, bg=bgcolour)
        this.pack(expand=YES)

        title = Label(this, image=img, borderwidth=0)
        title.img = img
        title.pack(side=TOP)
        
        m = Label(this, text=message, bg=bgcolour)
        m.pack(side=TOP)
        
        b = Button(this, text='OK', command=this.ok)
        b.pack(side=TOP)
        
    def ok(this):
        this.destroy()
        menu = MainMenu()
        menu.mainloop()

#Application entry point
menu = MainMenu()
menu.mainloop()
#img = PhotoImage(file='index.gif')
