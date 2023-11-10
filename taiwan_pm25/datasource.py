import requests
import psycopg2
import password as pw
import json



def __download_pm25_data()->list[dict]:    
        pm25_url = f'https://data.moenv.gov.tw/api/v2/aqx_p_02?api_key={pw.apikey}'
        response = requests.get(pm25_url)
        response.raise_for_status()     
        print("下載成功")
        return response.json()

def __create_table(conn):    
    cursor = conn.cursor()
    cursor.execute(
        '''
        CREATE TABLE  IF NOT EXISTS taiwan_pm25(
            "id"	SERIAL,
            "城市名稱"	TEXT NOT NULL,
            "縣市名稱"	TEXT NOT NULL,                         
            "pm25"	TEXT NOT NULL,             
            "時間"	TEXT NOT NULL,  
            PRIMARY KEY("id"),
            UNIQUE(城市名稱,時間)           
        );
        '''
    )
    conn.commit()
    cursor.close
    print("create_table成功")

def __insert_data(conn,values:list[any])->None:
    cursor = conn.cursor()
    
    sql= '''
    INSERT INTO taiwan_pm25(城市名稱,縣市名稱,pm25,時間)VALUES(%s,%s,%s,%s)ON CONFLICT (城市名稱,時間) DO NOTHING

        '''
       
    cursor.execute(sql,values)
    conn.commit()
    conn.close()
    


def updata_pm25_data()->None:
    '''
    下載,並更新資料庫
    '''
    
    data= __download_pm25_data()
    conn = psycopg2.connect(database=pw.DATABASE,
                        user=pw.USER, 
                        password=pw.PASSWORD,
                        host=pw.HOST, 
                        port="5432")
    __create_table(conn)   
    for item in data['records']:        
        __insert_data(conn,[item['sitename'],
                            item['county'],                            
                            item['itemname'],                       
                            item['monitordate']])        
        conn.close()