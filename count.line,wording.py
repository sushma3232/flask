# COUNT THE LINE AND WORDING in the file ("text2.txt")


f=open("text2.txt","r")
count=0
a=f.read()
b=a.split("\n")
for i in b:
    count+=1
f1=open("text2.txt","r")
count1=0
x=f1.read()
y=x.split()
for j in y:
    count1+=1
print(b)
print("lines:",count)
print(y)
print("wording:",count1)



# while loop:
f=open("text2.txt","r")
count=0
a=f.read()
b=a.split("\n")
i=0
while i<len(b):
    count+=1
    i=i+1
f1=open("text2.txt","r")
count1=0
x=f1.read()
y=x.split()
j=0
while j<len(y):
    count1+=1
    j=j+1
print(b)
print("lines:",count)
print(y)
print("wording:",count1)


