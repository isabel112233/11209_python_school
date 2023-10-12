import dataSource
import tkinter as tk
from tkinter import ttk     #ttk是tkinter 之套件

class Window(tk.Tk):                #設定tk.Tk為父類別
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title("鄉鎮人口統計")
        self.configure(background='#9E7A7A')

        topFame = tk.Frame(self,background='#FEDFE1')
        label = ttk.Label(topFame,text="鄉鎮人口統計",font=("Helvetica","25"),background='#B19693')
        label.pack(padx=20,pady=20)    
        topFame.pack()


        bottomFrame = tk.Frame(self,background="#DB4D6D")
        choices = dataSource.cityNames()
        choicesvar = tk.StringVar(value=choices)
        #listbox = tk.Listbox(bottomFrame,listvariable=choicesvar,width=12)   #listbox為區域變收無法為其他物件使用,改為屬性如line 22,23
        #listbox.pack(pady=20)      
        self.listbox = tk.Listbox(bottomFrame,listvariable=choicesvar,width=12)
        self.listbox.pack(pady=20)  
        bottomFrame.pack(expand=True,fill='x')
        self.listbox.bind("<<ListboxSelect>>",self.user_selected)    #self.user_selected  註冊

        #建立表格資料使用grid
        resultFrame = tk.Frame(self)
        tk.Label(resultFrame,text='年度').grid(column=0,row=0,sticky='E',pady=5)
        tk.Label(resultFrame,text='地區').grid(column=0,row=1,sticky='E',padx=5)
        tk.Label(resultFrame,text='人口數').grid(column=0,row=2,sticky='E',padx=5)
        tk.Label(resultFrame,text='土地面積').grid(column=0,row=3,sticky='E',padx=5)
        tk.Label(resultFrame,text='人口密度').grid(column=0,row=4,sticky='E',padx=5)
        self.yearVar = tk.StringVar()
        tk.Label(resultFrame,textvariable=self.yearVar).grid(column=1,row=0,sticky='W')
        self.cityVar = tk.StringVar()
        tk.Label(resultFrame,textvariable=self.cityVar).grid(column=1,row=1,sticky='W')
        self.populationVar = tk.StringVar()
        tk.Label(resultFrame,textvariable=self.populationVar).grid(column=1,row=2,sticky='W')
        self.areaVar = tk.StringVar()
        tk.Label(resultFrame,textvariable=self.areaVar).grid(column=1,row=3,sticky='W')
        self.densityVar = tk.StringVar()
        tk.Label(resultFrame,textvariable=self.densityVar).grid(column=1,row=4,sticky='W')
        resultFrame.pack()

    def user_selected(self,event):
        selectedIndex = self.listbox.curselection()[0]
        cityName = self.listbox.get(selectedIndex)
        #print(dataSource.info(cityName))
        datalist = dataSource.info(cityName)
        self.yearVar.set(datalist[0])
        self.cityVar.set(datalist[1])
        self.populationVar.set(datalist[2])
        self.areaVar.set(datalist[3])
        self.densityVar.set(datalist[4])




        #print("user selected")

def main():
    window = Window()         #呼叫父類別Window(tk,Tk)置入window
    #window.title("這是我的第一個視窗")   #改置於父類別     
    #label = tk.Label(window,text="Hello! Tkinter!",font=("Helvetica","30"))   #改置於父類別 
    #label.pack(padx=100,pady=50)   #改置於父類別 
    window.mainloop()           #讓程式一直執行,視窗不會關閉


if __name__ == "__main__":
    main()