numbers = []

n = int(input("Enter the number of elements in the list: "))
for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    numbers.append(element)

print("Input= list: ", numbers)
print("Positive numbers in the list:")
for num in numbers:
    if num > 0:
        print(num)