# accept five sports name from the user and write in a file 
# (each name should write in seperate line)


f=open("sportsname.txt","w")
i=0
while i<5:
    n=input("enter the name")
    f.write(n)
    f.write("\n")
    i=i+1
f.close()