print("Welcome to the Movie Ticket Checker!")

name = input("Please enter your name: ")
age = int(input("Please enter your age: "))

if age >= 18:
    ticket_type = "Adult Ticket"
elif 13 <= age <= 17:
    ticket_type = "Teen Ticket"
else:
    ticket_type = "Child Ticket"
    

#Display ticket type and other information

print(f"Here is the reciept for your ticket: {name}, {age}, and {ticket_type}")

# Under 13 → “Child ticket”
# 13–17 → “Teen ticket”
# 18 and above → “Adult ticket”