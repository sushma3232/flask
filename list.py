# print in a list   
a=[]
f=open("text.txt","r")
b=f.read()
for i in b:
    a.append(i)
print(a)
f.close()