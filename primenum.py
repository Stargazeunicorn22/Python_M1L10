x = int(input("Enter the lower part of range: "))
y = int(input("Enter the upper part of the range: "))

print(f"Prime numbers between {x} and {y} are:")
for i in range (x, y+1):
    if i > 1:
        for j in range (2,i):
            if (i%j)==0:
                break

        else: print(i, end=" ")
print()