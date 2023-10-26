import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import datasource          #import自訂的modul datadource
from threading import Timer


class Window(tk.Tk):   #繼承TK的功能,1.先自定義如下第1列,呼叫繼承的用super如下第2列     
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        try:
            datasource.updata_sqlite_data()

        #except Exception as e :             #Exception是父類別
        except Exception:
            #messagebox.showerror("錯誤",f'{e}\n將關閉應用程式請稍後再試')
            messagebox.showerror('錯誤\n網路發生錯誤\n將關閉應用程式請稍後再試')
            self.destroy()          #關閉視


#def on_closing(w:Window):     #功能只在main呼叫,可移至main下面
#    print('window關閉')
#    t.cancel()
#    w.destroy()

#t = None
#def update_data()->None:
#   print('做事')
#    global t        #宣告為全域使用
#   t = Timer(20,update_data)  #每隔20秒執行update_data一次   
#    t.start()


    
t = None
def main():
    def on_closing():          #在window底下不用寫
        print('window關閉')
        t.cancel()
        window.destroy()      #在window底下直接用window 

    
    def update_data()->None:
        datasource.updata_sqlite_data()
        global t                 #宣告為全域使用
        t = Timer(20,update_data)  #每隔20秒執行update_data一次   
        t.start()



    window = Window()
    window.title('台北市youbike2.0')
    window.geometry('600x300')                  #設定大小
    window.resizable(width=False,height=False)  #改變最大化按鈕固定視無法調整
    update_data()
    window.protocol("WM_DELETE_WINDOW",on_closing)   
    window.mainloop()




if __name__ =='__main__':
    main()