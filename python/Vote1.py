#Program to check if a person is eligible of voting in kenya
citizenship=(input("Enter your nationality: "))
age=int(input("Enter your age: "))
if( citizenship == "kenyan" and age >=18):
    print("You are eligible to vote")
else:
    print("you are not eligible to vote")