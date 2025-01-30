citizenship=(input("Enter your nationality: "))
age=int(input("Enter your age: "))
if( citizenship == "kenyan"or citizenship == "ugandan" or citizenship =="Tanzanee" and age >=18):
    print("You are eligible to vote")
else:
    print("you are not eligible to vote")