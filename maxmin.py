largest = None
smallest = None
while True:
    try:
        num = input("Enter a number: ")
        if num == "done":
            break
        num = int(num)

    except:
        print("Invalid input")

    if smallest is None or num < smallest:
        smallest = num
    if largest is None or num > largest:
        largest = num
        
print("Maximum", largest)
print("Minimum", smallest)