
# count uppercase letters in a file "text2.txt"

upper=0
f=open("text2.txt","r")
line=f.read()
for i in line:
    if (i.isupper()==True):
        upper+=1
print("total number of upper case alphabets",upper)



# count lowercase letters in a file "text2.txt"

lower=0
f=open("text2.txt","r")
line=f.read()
for i in line:
    if (i.islower()==True):
        lower+=1
print("total number of lowercase alphabets",lower)
