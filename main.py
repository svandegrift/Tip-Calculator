# Day 2 - Steven Vandegrift
# Tip Calculator

print("Welcome to the Tip Calculator")

total = float(input("What was the total bill?\n$"))
percent = int(input("What percentage tip would you like to give? 10, 12, or 15?\n"))/100
people = int(input("How many people to split the bill?\n"))

result = round((total + (total * percent)) / people, 2)
result = "{:.2f}".format(result)
print(f"Each person should pay ${result}")
