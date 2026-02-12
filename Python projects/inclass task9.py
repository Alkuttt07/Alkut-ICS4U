print([x for x in range(22) if x%2==0 and x!=0])
#1
print([(y+1)**2 for y in range(10)])
#2
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print([z for z in numbers if z%2==0])
#3
print([n+1 for n in range(20) if (n+1)%3==0])
#4
matrix = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
print([p for m in range(3) for p in matrix[m]])
#5
celsius_temperatures = [0, 25, 10, 32, 15]
print([(q*9/5)+32 for q in celsius_temperatures])
#6
words = ["hello", "world", "python", "list", "comprehension"]
print([len(r) for r in words])
#7
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(["Even" if s%2==0 else "Odd" for s in numbers])
#8
words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
print([t for t in words if len(t)>=5])
#9
print([v for v in [u+2 for u in range(49)] if all([v%w for w in range(2,v)])==True])