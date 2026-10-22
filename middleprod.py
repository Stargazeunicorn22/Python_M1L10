x = int(input("Enter a number: "))
if x<0:
    x = -x
temp = x
length =0
while temp >0:
    length +=1
    temp//=10

if length<=3:
    print("Num must have at least 4 digits")
else:
    mid_pos = length//2
    if length % 2 != 0:
        chop = mid_pos
    else:
        chop = mid_pos - 1

    i = 0
    while i < chop:
        x //= 10
        i += 1
    if length % 2 != 0:
        z = x % 10
    else:
        digit2 = x % 10
        x //= 10
        digit1 = x % 10
        z = digit1 * digit2
    print("The product of the middle digits (z) is:", z)