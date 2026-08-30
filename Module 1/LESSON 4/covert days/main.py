days = int(input("Enter days: "))

print("Years:", days // 365)
print("Weeks:", days % 365 // 7)
print("Days:", days % 365 % 7)
