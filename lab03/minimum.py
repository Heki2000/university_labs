cnt=0
print("Type 3 numbers (use Enter after type each number): ")
first, second, third = int(input()),int(input()),int(input())
if first <= second and first <= third:
    print("Minimum is: ", first)
elif second<=first and second<=third:
    print("Minimum is: ", second)
else:
    print("Minimum is: ", third)
