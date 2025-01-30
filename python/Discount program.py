#Discount program
amount=int(input("Enter the amount"))
if (amount >= 5000):
    discount = 0.1*amount
    print(discount)
elif (amount >1000 and amount < 4999):
    discount = 0.05*amount
    print(discount)
else:
    print("no discount")
