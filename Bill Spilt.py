print("  Welcome To Bill And Tip Calculator  ")
print("**************************************")
print("Enter Total Bill")
n=float(input("Rs : "))
print("\nHow much tip would you like to pay")
m=int(input("Percent : "))
print("\nHow many people are you")
p=int(input("People : "))

q=("{:.2f}".format((n*(m/100)+n)/p))

print(f"\nBill to Spilt : {q}")