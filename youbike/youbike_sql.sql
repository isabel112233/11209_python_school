SELECT 站點名稱,max(更新時間) AS 更新時間,行政區,地址,總車輛數,可借,可還
from 台北市youbike
GROUP BY 站點名稱
HAVING 站點名稱 LIKE"%大安%"


SELECT 站點名稱,max(更新時間) AS 更新時間,行政區,地址,總車輛數,可借,可還
from 台北市youbike
GROUP BY 站點名稱

select * from 台北市youbike

delete from 台北市youbike

drop table 台北市youbike

INSERT INTO 台北市youbike (站點名稱, 行政區, 更新時間, 地址, 總車輛數, 可借, 可還) 
VALUES ('YouBike2.0_捷運科技大樓站','大安區','2023-11-10 10:04:05','復興南路二段235號前',100,100,100)
ON CONFLICT (站點名稱,更新時間) DO UPDATE 
  SET 總車輛數 = 100, 
      可借 = 100,
	  可還 = 100;
	  
/*衝突不做事*/	  
select * 
from 台北市youbike
where 站點名稱='YouBike2.0_捷運科技大樓站'

INSERT INTO 台北市youbike (站點名稱, 行政區, 更新時間, 地址, 總車輛數, 可借, 可還) 
VALUES ('YouBike2.0_捷運科技大樓站','大安區','2023-11-10 10:04:05','復興南路二段235號前',0,0,0)
ON CONFLICT (站點名稱,更新時間) DO NOTHING
  