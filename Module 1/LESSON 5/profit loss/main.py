cp = float(input("Cost Price: "))
sp = float(input("Selling Price: "))

if sp > cp:
    print("Profit")
elif sp < cp:
    print("Loss")
else:
    print("No Profit, No Loss")
