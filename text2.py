# write a python programm to read a file line by line store into a variable

def file_read(fname):
    f=open(fname,"r")
    a=f.read()
    print(a)
file_read("text2.txt")


# print longest word in a file
f=open("text2.txt","r")
a=f.read().split()
print(a)
i=0
max=a[i]
while i<len(a):
    if len(a[i])>len(max):
        max=a[i]
    i=i+1
print("max:",max)
f.close()
    
