import dataSource
import tkinter as tk
from tkinter import ttk     #ttk是tkinter 之套件

def main():
    window = tk.Tk()         #呼叫tk預設的class TK()
    window.title("這是我的第一個視窗") 
       
    label = tk.Label(window,text="Hello! Tkinter!",width=12,height=3,font=("Helvetica","30"))
    label.pack(padx=100,pady=50)
    window.mainloop()           #讓程式一直執行,視窗不會關閉


if __name__ == "__main__":
    main()