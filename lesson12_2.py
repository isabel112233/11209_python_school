import random

class Player:
    def __init__(self, name:str):
        self.name = name
        self.__dice1 = 0
        self.__dice2 = 0
        self.__dice3 = 0
        self.__dice4 = 0

    def __play(self) -> int:         
        self.__dice1 = random.randint(1, 6)
        self.__dice2 = random.randint(1, 6)
        self.__dice3 = random.randint(1, 6)
        self.__dice4 = random.randint(1, 6)        
        #dice = [self.__dice1, self.__dice2, self.__dice3, self.__dice4]
        return dice   
        
    @property
    #def name(self) -> str :
        #return self.__name
        

    #@property
    def value(self)->int:
        global point
        num = [self.__dice1, self.__dice2, self.__dice3, self.__dice4]
        lt = []
        score =[]
        i=0
        num = self.__play
        for i in num :    
            lt.append(num.count(i))        
        if sum(lt) ==4 or sum(lt) == 10 :
            self.__play            
        elif sum(lt) == 6 :
            j=0            
            for j in range(4):
                score.append (num[j] * (lt[j]==1))            
            point = sum(score)
        elif sum(lt) == 8 :
            j=0
            for j in range(4):
                score.append (num[j] * (num[j]==max(num)))           
            point = sum(score)
        else :
            pass
            point = num[1] + 12
        return point        
        
        #呼叫self.play()            

    def __repr__(self) ->str:
        descript = ""
        descript +=f"{self.name}\n"
        descript +=f"骰子1={self.__dice1}\n" 
        descript +=f"骰子2={self.__dice2}\n"
        descript +=f"骰子3={self.__dice3}\n"
        descript +=f"骰子4={self.__dice4}\n"
        descript +=f"得分{self.value}分\n" 
        return  descript
                    

if __name__ == "__main__":
    print("===========擲骰子遊戲開始========")
    p1 = Player("Robert")
    p1 = Player.__play
    p1.value()
    p2 = Player("John")
    p2.value()
    print(p1)
    print(p2)
    print("遊戲结束")

        
    
    