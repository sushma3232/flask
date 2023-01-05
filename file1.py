# import os
file=open("text1.txt","w")
file.write("indhu")
file.write("abhi")
file.close()

# CREATING NEW FILE
import os
file=open("text.txt","x")
file.write("sunshine")
file.close()

# DELETE A FILE
import os
os.remove("text2.txt")


# CHECK IF FILE EXISTS OR NOT
import os
if os.path.exists("today.txt"):
    os.remove("today.txt")
else:
    print("there is no file with name today")