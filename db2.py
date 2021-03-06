# db1.py 
import sqlite3

#연결객체 리턴받기(임시로 메모리 작업)
#con = sqlite3.connect(":memory:")
#영구적으로 파일에 남기기 
con = sqlite3.connect("c:\\work\\sample2.db")

#실제 구문을 실행한 커서 객체 
cur = con.cursor()
#테이블 구조(스키마) 생성
cur.execute("create table PhoneBook (Name text, PhoneNum text);")
#1건을 입력
cur.execute("insert into PhoneBook values ('derick','010-222');")
#입력 파라메터 처리(입력창을 통해서 받기)
name = "gildong"
phoneNumber = "010-111"
cur.execute("insert into PhoneBook values (?, ?);", (name, phoneNumber) )
#다중의 레코드 입력(2차원: 2행2열 데이터)
datalist = (("tom","010-123"), ("dsp","010-456"))
cur.executemany("insert into PhoneBook values (?, ?);", datalist )

#데이터 조회(Curor클래스: Command + ResultSet)
cur.execute("select * from PhoneBook;")
#ctrl + / 
for row in cur:
    print(row)

#지금 상태는 전부 롤백(취소)
#입력, 수정, 삭제작업을 완료한 경우(작업 완료)
con.commit() 
con.close() 


