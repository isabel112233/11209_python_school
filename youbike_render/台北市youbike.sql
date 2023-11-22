CREATE TABLE  IF NOT EXISTS 台北市youbike(
            "id"	SERIAL,
            "站點名稱"	TEXT NOT NULL,
            "行政區"	TEXT NOT NULL,
            "更新時間"	TEXT NOT NULL,
            "地址"	TEXT,
            "總車輛數"	INTEGER,
            "可借"	INTEGER,
            "可還"	INTEGER,
            PRIMARY KEY("id"),
            UNIQUE(站點名稱,更新時間) 
        );



/*
沖突更新資料
*/
INSERT INTO 台北市youbike (站點名稱, 行政區, 更新時間, 地址, 總車輛數, 可借, 可還) 
VALUES ('YouBike2.0_一壽橋','文山區','2023-11-08 10:43:16','樟新街64號前方',100,10,20)
ON CONFLICT (站點名稱,更新時間) DO UPDATE 
  SET 總車輛數 = 100, 
      可借 = 10,
	    可還 = 20;


/*
沖突不做事
*/
INSERT INTO 台北市youbike (站點名稱, 行政區, 更新時間, 地址, 總車輛數, 可借, 可還) 
VALUES ('YouBike2.0_一壽橋','文山區','2023-11-08 10:43:16','樟新街64號前方',100,10,20)
ON CONFLICT (站點名稱,更新時間) DO NOTHING 

	  
	  
SELECT * 
FROM 台北市youbike
WHERE 站點名稱='YouBike2.0_一壽橋'


select *
from 台北市youbike

drop table 台北市youbike

delete from 台北市youbike

SELECT 站點名稱,MAX(更新時間) AS 更新時間,行政區,地址,總車輛數,可借,可還

    FROM 台北市youbike

    GROUP BY 站點名稱,行政區,地址,總車輛數,可借,可還

SELECT 站點名稱, 更新時間, 行政區, 地址, 總車輛數, 可借, 可還
FROM 台北市youbike
WHERE 更新時間 = (
	SELECT MAX (更新時間)
	FROM 台北市youbike
)