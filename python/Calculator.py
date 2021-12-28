from tkinter import*

def add():
    result=float(aEntry.get()) + float(bEntry.get())
    resultLabel.config(text=str(result))
    return ()

def subtract():
    result=float(aEntry.get()) - float(bEntry.get())
    resultLabel.config(text=str(result))
    return ()

def multiply():
    result=float(aEntry.get()) * float(bEntry.get())
    resultLabel.config(text=str(result))
    return ()

def divide():
    result=float(aEntry.get()) / float(bEntry.get())
    resultLabel.config(text=str(result))
    return ()

def reset():
    result=50*' '
    resultLabel.config(text=result)
    return ()

window=Tk()
window.title('Calculator')
window.config(width=640,height=480)

aLabel=Label(window, text='First number: ')
aLabel.place(x=50, y=50)

aEntry=Entry(window)
aEntry.place(x=50,y=100)

bLabel=Label(window, text='Second number: ')
bLabel.place(x=50, y=150)

bEntry=Entry(window)
bEntry.place(x=50,y=200)

addButton=Button(window, text='Add', command=add)
addButton.place(x=50, y=250)

subtractButton=Button(window, text='Subtract', command=subtract)
subtractButton.place(x=150, y=250)

multiplyButton=Button(window, text='Multiply', command=multiply)
multiplyButton.place(x=250, y=250)

divideButton=Button(window, text='Divide', command=divide)
divideButton.place(x=350, y=250)

resetButton=Button(window, text='Reset', command=reset)
resetButton.place(x=450, y=250)

resultLabel=Label(window, text='-----', font=('Calibri',20))
resultLabel.place(x=200,y=300)


window.mainloop()


