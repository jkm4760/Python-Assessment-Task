from Tkinter import *

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
    
    graphic = ['\n\n\n\n\n\n\n',
               '\n\n\n\n\n\n---------',
               '\n |\n |\n |\n |\n |\n-|-------',
               ' _____\n |\n |\n |\n |\n |\n-|-------',
               ' _____\n |   |\n |\n |\n |\n |\n-|-------',
               ' _____\n |   |\n |   O\n |   |\n |\n |\n-|-------',
               ' _____\n |   |\n |   O\n |  /|\\\n |\n |\n-|-------',
               ' _____\n |   |\n |   O\n |  /|\\\n |  / \\\n |\n-|-------',
               ''] #blank padder
    
    #Constructor
    def __init__(this):
        #Init the frame
        Frame.__init__(this)
        this.pack(expand=YES, fill=BOTH)
        this.master.title('TkHangman v1')
        this.master.iconname('tkhm1')

        #out_img label
        this.out_img = Label(this)
        this.out_img.pack(expand=YES, fill=BOTH)

        #out_text Label
        this.out_text = Label(this)
        this.out_text.pack(expand=YES, fill=BOTH)
        
        #Entry field
        thisinp_field = Entry(this, relief=SUNKEN)
        this.inp_field.pack(expand=NO, fill=BOTH)

        #Error Display
        this.out_err = Label(this, fg='red')
        this.out_err.pack(expand=YES, fill=BOTH)

        #Init lists
        #Read the word into a list for easy editing
        for char in 'Hello world': #REPLACE WITH RANDOM WORD FUNCTION THINGY
            this.word_ls.append(char.capitalize()) #capitalize everything so as to avoid conflicts
            if char != ' ':
                this.chars += 1

        #Initialize a display list
        for i in this.word_ls:
            if i == ' ':
                this.display_ls.append(' ')
            else:
                this.display_ls.append('_')
        
        #bind the enter key to the EnterPressed Function
        this.inp_field.bind('<Return>', this.EnterPressed)
        #bind keypresses, so we can restrict length
        this.inp_field.bind('<KeyPress>', this.RestrictLength)

    def setWord(this, newWord):
        this.word = newWord

    def RestrictLength(this, event):
        inp = this.inp_field.get()
        if len(inp) > 0:
            this.inp_field.delete(0, END)

    def EnterPressed(this, event):
        inp = this.inp_field.get()
        

        for char in this.used_letters: #already used that letter
                if inp.capitalize() == char:
                    this.clearInp('You have already used that letter!')
                    return

        this.prev_correct = this.correct

        for i in range(len(this.word_ls)): #iterate through the word
            if inp.capitalize() == this.word_ls[i]: #if the letter matches a letter in the word
                this.correct += 1 #you got one right!
                this.display_ls[i] = this.word_ls[i] #make sure they can see it :D
                
        if this.prev_correct == this.correct: #they didnt get anything :(
            this.incorrect += 1

        this.used_letters.append(inp.capitalize()) #We've used this letter now, lets disable it

        this.out_text['text'] = 'Word: ' + ' '.join(this.display_ls) + '\nUsed: ' + ' '.join(this.used_letters)
        this.out_img['text'] = this.graphic[this.incorrect]
        
        this.clearInp()

        print this.incorrect

        #win/loose conditions
        if this.incorrect == 8: #CHANGE TO CORRECT NO OF IMGS
            loss_diag = DiagBox(this)
            this.wait_window(loss_diag.top)

    def clearInp(this, error = ''):
        this.out_err['text'] = error
        this.inp_field.delete(0, END)


class DiagBox:
    #TEMPORARY DIAG BOX. WILL REPLACE WITH MESSAGE BOX.
    def __init__(this, parent):

        top = this.top = Toplevel(parent)
        b = Button(top, text="OK", command=this.ok)
        b.pack(pady=5)
        
    def ok(this):
        this.top.destroy()
        print 'test'

#Application entry point
if __name__ == '__main__':
    MainWindow().mainloop()
#img = PhotoImage(file='index.gif')
