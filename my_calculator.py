import tkinter
import turtle
from tkinter import *
#creates a frame
def iCalc(source, side):
    storeObj = Frame(source, borderwidth = 14 , bd= 4, bg = "powder blue")
    storeObj.pack(side=side, expand = YES, fill = BOTH)
    return storeObj
#adds buttons

def button(source, side , text, command = None):
    storeObj = Button(source, text = text, command=command)
    storeObj.pack(side=side, expand = YES, fill = BOTH)
    return storeObj
class app(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.option_add('*Font', 'arial 20 bold')
        self.pack(expand = YES, fill=BOTH)
        self.master.title('OLVINES CALC')
        display = StringVar()
        Entry(self,relief=RIDGE, textvariable=display,justify= 'right',bd=30,bg="powder blue").pack(side =TOP,expand=YES, fill = BOTH)
        for clearButton in (["X"]):
            erase=iCalc(self,TOP)
            for ichar in clearButton:
                button(erase, LEFT, ichar, lambda storeObj=display, q = ichar:storeObj.set(''))
        for numButton in ("123/","456*","789-","0.+", "%"):
             FunctionNum=iCalc(self,TOP)
             for iEquals in numButton:
                 button(FunctionNum, LEFT,iEquals,lambda storeObj=display, q= iEquals: storeObj.set(storeObj.get() +q))
        EqualButton = iCalc(self, TOP)
        for iEquals in "=":
            if iEquals == "=":
                btniEquals = button(EqualButton, LEFT, iEquals)
                btniEquals.bind('<ButtonRelease-1>',lambda e,s = self, storeObj=display:s.calc(storeObj),'+')
            else:
                btniEquals = button(EqualButton,LEFT,iEquals, lambda storeObj=display, s='%s' % iEquals:StoreObj.set(storeObj.get()+s))
    def calc(self, display):
        try:
            display.set(eval(display.get()))
        except:
            display.set("ERROR")
          
if __name__=='__main__':
    app().mainloop()
    

            
         
            

    


    
    
