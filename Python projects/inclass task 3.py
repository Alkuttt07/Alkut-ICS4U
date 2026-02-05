import random
list1 = [random.randint(10,20),random.randint(10,20),random.randint(10,20),random.randint(10,20),random.randint(10,20)]
list1[1] = 16
list1.sort(reverse=True)
print(list1[:4],list1[-4:])