

import pickle
with open("customer.dat","rb")as f:
# f=open("customer.dat","rb")
    while True:
        try:
            row=pickle.load(f)
            if row[0].lower()=="delhi":
                print(row)
        except EOFErorr:
            break
            