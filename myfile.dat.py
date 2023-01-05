import pickle
def write():
    f=open("myfile.dat","wb")
    lst=["cuty","nicey","princy"]
    pickle.dump(lst,f)
    f.close()
write()
print("data successfully stored")