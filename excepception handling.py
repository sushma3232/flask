
# a=10
# b=0
# c=a/b
# print(c)

# try:
#     a=int(input("enter the num"))
#     b=int(input("enter the num"))
#     c=a/b
# except:
#     print("can't divide with zero")
    
    
# a=70
# b=0
# try:
#     print(a/b)
#     print("new line")
# except ZeroDivisionError:
#     print("do not divide number with zero")
# print("completed")


a=10
b=0
try:
    print(a/b)
except Exception as a:
    print("do not divide number by zero",a)
print("completed")



x=-15
if x<0:
    raise Exception("sorry,no number below zero")