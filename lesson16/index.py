import dataSource

def main():
    cities = dataSource.cities_info()
    #cities1 = dataSource.cities_info()   #會重覆下載,改善如dataSource.py  line5及line 26檢核是否有資料
    for city in cities:
        print(city)
    #try :
    #    data_list = dataSource.download()
    #except Exception as e:
    #    print(f"錯誤:{e}")
    #else:
    #    for row in data_list:
    #        print(row)
if __name__ =="__main__":
    main()