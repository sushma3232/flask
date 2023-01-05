

f=open("seek.txt","r")
print(f.tell())
print(f.read(3))
f.seek(0)
print(f.read())
f.close()