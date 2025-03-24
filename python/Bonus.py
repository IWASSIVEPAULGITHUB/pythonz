#Getting input 
salary=float(input("Enter your total salary: "))
years_of_service=int(input("Enter the number of years you have served: "))

#calculating bonus percentage
if years_of_service > 10:
    bonus_percentage = 0.10
elif 6 <= years_of_service <= 10:
    bonus_percentage = 0.08
else:
#years of service are less than 6 years
    bonus_percentage = 0.05

bonus_amount = salary * bonus_percentage
total_salary = salary + bonus_amount
print(f"your netbonus is: {bonus_amount: }")
print(f"your net salary is:{total_salary} ")