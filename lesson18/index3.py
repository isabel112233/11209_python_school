'''
學習Canvas
'''
import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk         #查網站安裝pillow    

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.geometry("300x250")
        self.title("Images")  
        self.configure(background="#F4A7B9")                    
       

class MyFrame(ttk.LabelFrame):
    def __init__(self,master,title,**kwargs):               #自訂Class 新增加一參數title
        super().__init__(master,text=title,**kwargs)        #繼承之calss也同時增加一參數title
        self.aligement = tk.StringVar(value='left')
        ttk.Radiobutton(self,text="左邊",value='left',variable=self.aligement,command=self.choised).grid(column=0,row=0,padx=10)
        ttk.Radiobutton(self,text="中間",value='center',variable=self.aligement,command=self.choised).grid(column=1,row=0,padx=10)
        ttk.Radiobutton(self,text="右邊",value='right',variable=self.aligement,command=self.choised).grid(column=2,row=0,padx=10)
        self.pack(expand=1, fill='x',padx=10,pady=10)

    def choised(self):
        print(self.aligement.get())


def main():    
    window = Window()
    myFrame = MyFrame(window,"對齊方式")
    s.ttk.Style()
    print(s.theme_names())
    window.mainloop()


if __name__ == "__main__":
    main()