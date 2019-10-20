import threading #thread
import time #time sleep
from tkinter import * #GUI 

from queue import Queue


import random #used to generate random numbers

val1 = 0
val2 = 0

appRunning = True

window = Tk()
window.title("Test window")

def exitButtonCallback():
    global appRunning
    appRunning = False
    time.sleep(1)#let the threads finish their processing
    print("exiting app")
    window.quit()
    window.destroy()

#exit button:
exitButton = Button(window, text="Exit", command=exitButtonCallback)
exitButton.grid(column=0, row=2)

#first value:
val1Label = Label(window, text="Val1  =")
val1Label.grid(column=0, row=0)

val1LabelValue = Label(window, text="0")
val1LabelValue.grid(column=1, row=0)

#second value:
val2Label = Label(window, text="Val2  =")
val2Label.grid(column=0, row=1)

val2LabelValue = Label(window, text="0")
val2LabelValue.grid(column=1, row=1)

def updateVals(name):
    global val1
    global val2
    while(appRunning):
        val1 = float("{0:.3f}".format(random.uniform(-99999, 99999)))
        val2 = float("{0:.3f}".format(random.uniform(-99999, 99999)))
        time.sleep(0.1)

def updateLbl(name):
    while(appRunning):
        val1LabelValue.configure(text=str(val1))
        val1LabelValue.grid(column=1, row=0)
        val2LabelValue.configure(text=str(val2))
        val2LabelValue.grid(column=1, row=1)

        window.update()        
        time.sleep(0.3)



updateValsThread = threading.Thread(target=updateVals, args=(1,))
updateValsThread.daemon = True
updateValsThread.start()

updateLblThread = threading.Thread(target=updateLbl, args=(1,))
updateLblThread.daemon = True
updateLblThread.start()

window.mainloop()
