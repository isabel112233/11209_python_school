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


        #標題
        heading = ttk.Label(self,text='會員登入',font=('Helvetica',20),foreground='red')
        heading.grid(column=0,row=0,columnspan=2,padx=(20,0))          #columnspah橫跨兩欄

        username_label = ttk.Label(self,text='使用者名稱',font=('Helvetica',12))
        username_label.grid(column=0,row= 1,pady=10,padx=(10,1))

        username_entry = ttk.Entry(self)
        username_entry.grid(column=1,row= 1,padx=(0,10))

        password_label = ttk.Label(self,text='密碼',font=('Helvetica',12))
        password_label.grid(column=0,row=2,sticky=tk.E,pady=10,padx=(10,1))
        
        password_entry = ttk.Entry(self,show="*")
        password_entry.grid(column=1,row= 2,padx=(0,10))

        login_button = ttk.Button(self,text='登入')
        login_button.grid(column=1,row=3,sticky=tk.E,padx=(0,10),pady=(20,0))
        
        

        

    def choised(self):
        print(self.aligement.get())


def main():    
    window = Window()
    myFrame = MyFrame(window,"對齊方式")    
    window.mainloop()


if __name__ == "__main__":
    main()