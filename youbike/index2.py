import tkinter as tk
from tkinter import ttk
from youbikeTreeView import YoubikeTreeView
from tkinter import messagebox
import datasource          #import自訂的modul datadource
from threading import Timer


class Window(tk.Tk):   #繼承TK的功能,1.先自定義如下第1列,呼叫繼承的用super如下第2列     
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        #========更新資料庫資料=============
        try:
            datasource.updata_sqlite_data()
        except Exception:
            messagebox.showerror('錯誤\n網路發生錯誤\n將關閉應用程式請稍後再試')
            self.destroy()          #關閉視窗

        ##=========建立介面=============
        #print(datasource.lastest_datetime_data())

        topFrame = tk.Frame(self,relief=tk.GROOVE,borderwidth=1)
        tk.Label(topFrame,text='台北市youbike及時資料',font=("arial",20),bg="#333333",fg="#ffffff",padx=10,pady=10).pack(padx=20,pady=20)
        topFrame.pack(pady=30)

        bottomFrame = tk.Frame(self)  
        #=========建立treeView===============
        self.youbikeTreeView = YoubikeTreeView(bottomFrame,show='headings',columns=('sna','mday','sarea','ar','tot','sbi','bemp'))
        self.youbikeTreeView.pack()
        bottomFrame.pack(pady=30)


        #========更新treeView資料=========
        lastest_data= datasource.lastest_datetime_data()
        self.youbikeTreeView.update_content(lastest_data)

    

def main():        
    def update_data(w:Window)->None:
        datasource.updata_sqlite_data()        
        window.after(3*60*1000,update_data,w)



    window = Window()
    window.title('台北市youbike2.0')
    #window.geometry('600x300')
    window.resizable(width=False,height=False)  #改變最大化按鈕固定視無法調整
    update_data(window)    
    window.mainloop()




if __name__ =='__main__':
    main()