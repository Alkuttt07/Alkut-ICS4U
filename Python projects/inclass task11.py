text = "bi bi bom bom, I am R2D2!"
print(text[0])
print(text[-1])
print(text[7:12])
print(text[::-1])
a=[x for x in text if x!=" " and x!="!"]
print("".join(a[:3]),"".join(a[-3:]))
print(text.replace("b","h"))