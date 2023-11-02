import tkinter as tk
from tkinter import ttk
from youbikeTreeView import YoubikeTreeView
from tkinter import messagebox
from threading import Timer
import datasource

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        #---------更新資料庫資料-----------------#
        try:
            datasource.updata_sqlite_data()
        except Exception:
            messagebox.showerror("錯誤",'網路不正常\n將關閉應用程式\n請稍後再試')
            self.destroy()
        

        #---------建立介面------------------------
        #print(datasource.lastest_datetime_data())
        topFrame = tk.Frame(self,relief=tk.GROOVE,borderwidth=1)
        tk.Label(topFrame,text="台北市youbike及時資料",font=("arial", 20), bg="#333333", fg='#ffffff',padx=10,pady=10).pack(padx=20,pady=20)
        topFrame.pack(pady=30)

        #===========建立搜尋=================
        middleFrame = ttk.LabelFrame(self,text='站點搜尋')
        tk.Label(middleFrame,text="站點名稱:").pack(side='left')  #没有傳出東西
        self.search_entry = tk.Entry(middleFrame) #建立entry實體,要先取得實體才可pack
        self.search_entry.pack(side='left') #得到entry 實體所以直接pack      
        middleFrame.pack(expand=1,fill='both')          #expend後面參數為1:True 或2:False      
        
        #---------------------------------------

         #==============建立treeView=============
        bottomFrame = tk.Frame(self)
       
        self.youbikeTreeView = YoubikeTreeView(bottomFrame,show="headings",
                        columns=('sna','mday','sarea','ar','tot','sbi','bemp'),
                       height=20)   #height 設定為20行

        
        

        #=======設定捲軸===============
        self.youbikeTreeView.pack(side='left')
        vsb = ttk.Scrollbar(bottomFrame,orient="vertical",command=self.youbikeTreeView.yview)
        vsb.pack(side='left',fill='y')        
        self.youbikeTreeView.configure(yscrollcommand=vsb.set)        
        bottomFrame.pack(pady=30,padx=20)  

        
        
         
        datasource.search_sitename("entry.get()")
       

def main():    
    def update_data(w:Window)->None:
        datasource.updata_sqlite_data()
        lastest_data = datasource.lastest_datetime_data()
        w.youbikeTreeView.update_content(lastest_data)
        window.after(3*60*1000,update_data,w) #每隔3分鐘
          

    window = Window()
    window.title('台北市youbike2.0')
    #window.geometry('600x300')
    window.resizable(width=False,height=False)
    update_data(window)          
    window.mainloop()

if __name__ == '__main__':
    main()