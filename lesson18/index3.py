'''
學習Canvas
'''
import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk         #查網站安裝pillow    

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        #self.geometry("300x250")
        self.title("Images")                      
       

class MyFrame(tk.Frame):
    def __init__(self,master,**kwargs):
        super().__init__(master,**kwargs)
        self.configure(background='#9E7A7A')
        self.img = Image.open("pets.png")
        self.pets = ImageTk.PhotoImage(self.img)
        #canvas = tk.Canvas(self,width=48,height=48)
        #canvas.create_image(12,12,image=self.pets,anchor=tk.NW)
        #canvas.pack()
        petLabel = tk.Label(self,image=self.pets,width=50,height=50,background="#DDA52D")
        petLabel.pack(padx=40,pady=40)


        self.pack(expand=1, fill='both')


def main():    
    window = Window()
    myFrame = MyFrame(window)
    window.mainloop()

if __name__ == "__main__":
    main()