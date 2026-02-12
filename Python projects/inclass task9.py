even_numbers=[x for x in range(22) if x%2==0 and x!=0]
print(even_numbers)
#1
squares=[(y+1)**2 for y in range(10)]
print(squares)
#2
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers=[z for z in numbers if z%2==0]
print(even_numbers)
#3
divisible_by_3=[n+1 for n in range(20) if (n+1)%3==0]
print(divisible_by_3)
#4
matrix = [
 	   [1, 2, 3],
 	   [4, 5, 6],
 	   [7, 8, 9]
]
flat_matrix =[p for m in range(3) for p in matrix[m]]
print(flat_matrix)
#5
