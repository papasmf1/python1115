# DemoFile.py 

f = open("c:\\work\\demo.txt", "wt", encoding="utf-8")
f.write("첫번째라인\n두번째\n세번째\n")
f.close()

print( f.closed )


