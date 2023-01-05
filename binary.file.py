
# import json
# d={1:"welcome",2:"to",3:"navgurukul",4:"bangalore"}
# j_str=json.dumps(d)
# print(j_str)
# print(type(j_str))


f=open("binfile.bin","wb")
num=[5,10,15,20,25]
arr=bytearray(num)
f.write(arr)
f.close()


