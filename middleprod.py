x = input("Enter a number: ")

if x == '-':
    x = x[1:]

length = len(x)

if length < 3:
    print("The number must have at least 3 digits.")
else:
    mid = length // 2
    if length % 2 != 0:
        start_index = mid
        end_index = mid + 1
    else:
        start_index = mid - 1
        end_index = mid + 1
    z = 1
    for i in range(start_index, end_index):
        z *= int(x[i])

    print("The product of the middle digits (z) is:", z)
