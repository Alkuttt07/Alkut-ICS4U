matrix=[[1,2,3],[4,5,6],[7,8,9,0]]
Newlist = [x if x>5 else x**2 for y in matrix for x in y]
newlist2=[]
for z in matrix:
    for m in z:
        if m>5:
            newlist2.append(m)
        else:
            newlist2.append(m**2)
print(Newlist)
print(newlist2)
#1
combinations =[]
for a in range(5):
    for b in range(5):
        combinations.append([a,b])
print(combinations)
#2
combinations2 = [[c,d] for c,d in [[2,3], [4,5]]]
print(combinations2)
combinations4 = [[x,y] for x,y in [(2,3), (4,5), (6,7)] if x>4]
print(combinations4)
#3
dices=[[x+1,y+1] for x in range(6) for y in range(6)]
print(dices)
#4
l1=[[1,2],[4,5],[8,9],[9,3],[2,6]]
combinations3=[]
for x,y in l1:
    if y>x:
        combinations3.append([x,y])
    else:
        combinations3.append([y*2,x])
print(combinations3)
#5
