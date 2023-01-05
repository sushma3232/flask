# COUNT THE LETTERS with space in the file ("text2.txt") 
f=open("text2.txt","r")
a=f.read()
i=0
while i<len(a):
    count=0
    j=0
    while j<len(a):
        count+=1
        j+=1
    i=i+1
print(a)
print("count:",count)


# COUNT THE LETTERS without space in the file ("text2.txt")

f=open("text2.txt","r")
a=f.read()
b=a.split()
i=0
count=0
while i<len(b):
    j=0
    while j<len(b[i]):
        count+=1
        j+=1
    i=i+1
print(b)
print("count:",count)



