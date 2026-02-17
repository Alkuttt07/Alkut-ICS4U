words = ["apple", "banana", "cherry", "kiwi"]
words1=[x for x in words if "a" in x]
print(words1)
#1
numbers=[y for y in range(1,101) if y%3==0 and y%5==0]
print(numbers)
#2
nums = [1, -2, 3, -4, 5]
nums1= [z if z>=0 else 0 for z in nums]
print(nums1)
#3
words2=["dog", "cat", "parrot"]
words3=[m[-1] for m in words2]
print(words3)
#4