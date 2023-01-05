
# aceept five hobbies from the user and write in a file "hobby.txt"
# without using write()function

f=open("hobby.txt","a+")
i=0
while i<5:
    n=input("enter the hobby")
    f.writelines(n)
    f.writelines("\n")
    i=i+1
f.close()