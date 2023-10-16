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
        #self.configure(background="#F4A7B9")                    
       

class MyFrame(ttk.LabelFrame):
    def __init__(self,master,title,**kwargs):               #自訂Class 新增加一參數title
        super().__init__(master,text=title,**kwargs)        #繼承之calss也同時增加一參數title
        self.pack(expand=1,fill="both",padx=10,pady=10)

        self.tree = ttk.Treeview(self,columns=['#1','#2','#3'],show='headings')        
        self.tree.heading('#1',text='第一欄') 
        self.tree.heading('#2',text='第二欄')
        self.tree.heading('#3',text='第三欄')

        contacts = []
        for n in range(1,100):
            contacts.append([f'first{n}',f'last{n}',f'email{n}:example.com'])
        
        for contact in  contacts :
            self.tree.insert('',tk.END,value=contact)
        self.tree.pack()

        
        
        

        

    def choised(self):
        print(self.aligement.get())


def main():    
    window = Window()
    myFrame = MyFrame(window,"對齊方式")    
    window.mainloop()


if __name__ == "__main__":
    main()