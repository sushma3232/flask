

bank_list=["kotak","HDFC","SBI","Bank of Baroda","RBI"]
f=open("banklist.txt","w")
i=0
while i<len(bank_list):
    if bank_list[i]:
        f.write(bank_list[i]+"\n")
    i=i+1
f.close()