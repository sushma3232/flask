shimla=open("shimla.txt","a")
delhi=open("delhi.txt","a")
other=open("other.txt","a")
f=open("people3.txt","r")
a=f.read()
b=a.split("\n")
# print(b)
i=0
while i<len(b):
    if "delhi" in b[i]:
        delhi.write(b[i])
        delhi.write("\n")
    elif "shimla" in b[i]:
        shimla.write(b[i])
        shimla.write("\n")
    else:
        other.write(b[i])
        other.write("\n")
    i=i+1
f.close()
        
    