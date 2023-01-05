
# count a letter "s" in the file "passage.txt"
f=open("passage.txt","r")
count=0
a=f.read()
for i in a:
    if "s" in i:
        count+=1
print(count)

# count "ing" in the file "passage.txt"
f=open("passage.txt","r")
count=0
a=f.read()
b=a.split()
for i in b:
    if "ing" in i:
        count+=1
print(count)
print(b)





