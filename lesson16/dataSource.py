import requests
import csv
import io

__cities = []

def __download()->list[list] | None:

    url = 'https://data.moi.gov.tw/MoiOD/System/DownloadFile.aspx?DATA=CA18EE06-4A50-4861-9D97-7853353D7108'
    response = requests.request('GET',url)
    try:
        response.raise_for_status()     #網站連線發生錯誤時處理方式
    except:
        raise Exception("連線發生錯誤","網路中斷")
        
    else:
        if  not response.ok:
            raise Exception('下載錯誤','伺服器錯誤訊息')            
        else:
            file = io.StringIO(response.text)
            csv_reader = csv.reader(file)
            next(csv_reader)         #不列出一行
            return list(csv_reader)
        
def cities_info()->list[list]:       #以'_'命名法
    if len(__cities) == 0:

        try :
            data_list = __download()
        except Exception as e:
            print(f"錯誤:{e}")
        else:
            for row in data_list:
                if row[0]== '111' :
                    __cities.append(row)
                    #print(row)
    return __cities
    

def cityNames()->list[str] :          #駝峰式命名法
    cities = cities_info()
    names = []
    for  row in cities:
        cityName = row[1]
        names.append(cityName)
    return names


def info(name:str)->list[str]:            #((name:str)引數一定要有值,後面不用加None
    cities = cities_info()    
    for city in cities:
        if city[1] == name:        
            return city
    return []