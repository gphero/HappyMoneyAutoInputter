import sqlite3

con = sqlite3.connect("happylist.db")
cursor = con.cursor()

#ppomList 테이블이 존재하면 DROP 에서 오류
cursor.execute("CREATE TABLE happyList(number text, date text)")

con.commit()

cursor.execute("SELECT * FROM happyList")

# for row in cursor:
#      print( "%s 의 주소는 %s 입니다." % (row[1], row[2]) )

con.close()