
# import pickle
# f=open("student.dat","wb")
# pickle.dump([23,"reena",12],f)
# pickle.dump([24,"tina",13],f)
# f.close()



import pickle
with open("file.dat","wb") as f:
    while True:
        op=int(input("enter 1 to add data,0 to quit"))
        if op==1:
            name=input("enter the name")
            rollno=int(input("roll no"))
            pickle.dump(name,rollno,f)
        elif op==0:
            break