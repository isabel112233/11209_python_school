class Person:          #建立class實體
    def __init__(self,name:str,weight:int,height:int): #實體名稱屬性
        self.__name = name     #name前面加2個底線表不能由實體P1修改
        self.weight = weight
        self.height = height
    #property    建立readonly供查詢
    @property
    def name(self) -> str :
        return self.__name
    
    @property
    def getBMI(self) ->float :
        #return round(self.weight /(self.height/100)**2,ndigits=2)
        return self.bmi()


    #method  實體方法  ,執行實體方法要用實體名稱。例:1.p1.name
    def bmi(self)-> float:
        return round(self.weight /(self.height/100)**2,ndigits=2)


    def __str__(self) -> str:
        return f"name={self.__name}\nwight={self.weight}\nheight={self.height}"
    
        
if __name__=='__main__':         #程式預設執行開始
    p1 = Person("robert",78,183)
    print(p1.name)            #實體不能讀、寫private 的__name，要用readonly方式 ，看property
    #p1.name = "vivian"       #name為private只能讀不能改,會出錯                
    print(p1.getBMI)          #property不用括號

