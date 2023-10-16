"""
學習Canvas
"""
import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):            #繼承Tk
    def __init__(self,**kwargs):            #使用別人的class(tk.Tk)參數先用**kwargs
        super().__init__(**kwargs)          #繼承父類別
        self.geometry("400x250+300+300")
        self.title("Lines")
        self.configure(background="#F17C67")

class MyFrame(tk.Frame):
    def __init__(self,**kwargs):
        super().__init__(master,**kwargs)
        self.congigure(background="#DDA52D")        
        self.pack(expand=1,fill="both")


def main():
    window = Window()
    myFrame = MyFrame(window)
    window.mainloop()
    
   
if __name__ == "__main__":                
    main()