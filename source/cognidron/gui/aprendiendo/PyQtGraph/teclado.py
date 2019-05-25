import Tkinter as tk

def keypress(event): 
    if event.keysym == 'Escape': 
        mainRoot.destroy() 
        keyPressed = event.char 
        print ("You pressed: " + keyPressed)

mainRoot = tk.Tk() 
print("Press a key (Escape key to exit):" )
mainRoot.bind_all('', keypress) 
mainRoot.withdraw() 
mainRoot.mainloop()