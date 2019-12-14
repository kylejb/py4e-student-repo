# how do i store values through iterative loop?
# how do i accept fractional input?

largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    try:
        fnum = float(num)
    except:
        print("Invalid Entry: Enter numerical value.")
        continue
    print(fnum)
    if largest is None and smallest is None:
        largest = fnum
        smallest = fnum
    elif fnum > largest:
        largest = fnum  
    elif fnum < smallest:
        smallest = fnum      
    
if largest == None and smallest == None:
    print("You have exited the program without entering any numerical values.")
else:
    print("Maximum is", int(largest))
    print("Minimum is", int(smallest))