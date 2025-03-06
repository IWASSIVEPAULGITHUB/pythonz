customerId=int(input("Enter your cudtomer ID: "))
customerName =str(input("Enter your customer name: "))
unitconsumed = float(input("Enter total units you think you have consumed: "))
if unitconsumed <= 199:
    charges_per_unit =1.20
elif 200<=unitconsumed<400:
    charges_per_unit =1.50
elif 400<=unitconsumed<600:
    charges_per_unit =1.80
else: 
    #if the unit consumed are greater than 600
    charges_per_unit =2.00
#we are calculating the total bill here
total_bill= unitconsumed*charges_per_unit

if total_bill>400:
    surcharge = total_bill*0.15
    total_bill+=surcharge
else:
    surcharge = 0
if total_bill<100:
    total_bill=100

#Now we are displaying final result
print("Total bill: ")

print(f"CustomerID :{customerId}")
print(f"CustomerName :{customerName}")
print(f"UnitConsumed :{unitconsumed}KW")
print(f"Charges per unit: Ksh{charges_per_unit}")
print(f"Surcharge Amount :Ksh{surcharge}")
print(f"Amount to pay:Ksh{total_bill}")


   
