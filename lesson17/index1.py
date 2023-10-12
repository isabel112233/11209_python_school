import dataSource
import tkinter as tk
from tkinter import ttk     #ttk是tkinter 之套件

class Window(tk.Tk):                #設定tk.Tk為父類別
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title("這是我的第一個視窗")
        label = tk.Label(self,text="Hello! Tkinter!",font=("Helvetica","30"))
        label.pack(padx=100,pady=50)

def main():
    window = Window()         #呼叫父類別Window(tk,Tk)置入window
    #window.title("這是我的第一個視窗")   #改置於父類別     
    #label = tk.Label(window,text="Hello! Tkinter!",font=("Helvetica","30"))   #改置於父類別 
    #label.pack(padx=100,pady=50)   #改置於父類別 
    window.mainloop()           #讓程式一直執行,視窗不會關閉


if __name__ == "__main__":
    main()