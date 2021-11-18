# web1.py 
from bs4 import BeautifulSoup

#페이지를 로딩
page = open("c:\\work\\test01.html", "rt", encoding="utf-8").read()
#검색이 용이한 객체 생성
soup = BeautifulSoup(page, "html.parser")
#전체를 보여달라~
print( soup.prettify() )


