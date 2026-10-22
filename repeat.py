x = input("Enter anything! ")
y = input("Enter a char to count: ")
index = 0
count = 0
while index < len(x):
    if x[index] == y:
        count +=1
    else:
        pass
    index += 1
print(f"The character '{y}' appears {count} time(s) in the text.")