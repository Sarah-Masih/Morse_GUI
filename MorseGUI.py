#referred code from GeeksforGeeks, Youtube, tutorialspoint

from tkinter import*
import tkinter.font
from gpiozero import LED
import RPi.GPIO
import time
RPi.GPIO.setmode(RPi.GPIO.BCM)
Red=LED(14)

#to control lights
def RedToggle():
    Red.on()
def RedOFF():
    Red.off()
def close(): #for closing the application
    RPi.GPIO.cleanup()
    win.destroy()
    
win=Tk()  #win is short for window
win.title("Morse Blink")
frame=Frame(win)
frame.pack()
bottomframe = Frame(win)
bottomframe.pack( side = BOTTOM )

#buttons
exitButton= Button(bottomframe, text="Exit", fg="white", command=close, bg='red')
exitButton.pack( side = BOTTOM)

#call close function when window is deleted by selecting the x button on widget
win.protocol("WIN DELETE WINDOW", close)

#test morse code messages from geeksforgeeks
def encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ':
  
            # Looks up the dictionary and adds the
            # correspponding morse code
            # along with a space to separate
            # morse codes for different characters
            MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-','_':'..--.-'}
  
            cipher += MORSE_CODE_DICT[letter] + ' '
        
        else:
            # 1 space indicates different characters
            # and 2 indicates different words
            cipher += ' '
      
    return cipher

emptylabel=Label(win, fg='green', font=('Arial',14))
message=StringVar()

#my function will receive input from user and sends it to encrypt function
def myfunc():

    emptylabel.config(text='Broadcasted-> '+message.get())
    emptylabel.pack(side= BOTTOM)
    result= encrypt(message.get().upper())
    light(result)
    
#controls lights
def light(result):
    for i in result:
        if i is '.':
            RedToggle()
            time.sleep(1)
            RedOFF()
            time.sleep(1)

        elif i is '-':
            RedToggle()
            time.sleep(3)
            RedOFF()
            time.sleep(1)
            
#main function
def main():

    textbox1=Entry(win, textvariable=message, fg='blue', font=('Arial',14))
    textbox1.pack(side=LEFT)

    SubmitButton= Button(bottomframe, text="Submit", fg="white", command=myfunc, bg='black')
    SubmitButton.pack(side = BOTTOM)
    
#calling the main function   
if __name__ == '__main__':
    main()
