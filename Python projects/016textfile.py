a=open("016text.txt")
print(a.readlines()[0])
a.close()
#1
with open("016text.txt") as a:
    print(a.readlines())
#2
with open("016text.txt","a") as f:
    f.write("\nhahaha")