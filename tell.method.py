

f=open("text.txt","r")
print(f.tell())
f.close()


f=open("text.txt","r")
# print(f.tell())
print(f.read(3))
print(f.tell())
f.close()



f=open("text.txt","r")
print(f.readline())
print(f.tell())
f.close()

