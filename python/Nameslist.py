#program that prompts user to enter a list of names
names=input("Enter the names")
names_list = [name.strip() for name in names.split(",")]
# Count the number of names entered
Number_of_names = len(names_list)
#sorting the names
sorted = sorted(set(names_list))
#printing the names and the total number
print("\nTotal names number:", Number_of_names)
print("names:")
for name in sorted:
    print(name)
