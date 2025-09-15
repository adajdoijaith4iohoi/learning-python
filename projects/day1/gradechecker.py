import time


print("Welcome to the Grade Checker: A fast way to check your grades!")

name = input("Please Enter Your Name: ")

print(f"Logging in as {name}...")
time.sleep(2)
print(f"Logged in as {name}!")
time.sleep(1)
print(f"Welcome, {name} to Grade Checker.")

score = int(input("Please enter your test score: "))

if score >= 90:
    letter_grade = "A"
elif 80 <= score <= 89:
    letter_grade = "B"
elif 70 <= score <= 79:
    letter_grade = "C"
elif 60 <= score <= 69:
    letter_grade = "D"
else:
    print(f"You have completely failed with your score of {score} on the test, better luck next time!")

print(f"Hi, {name} You got a score of {score} on your test and in a letter grade that is a {letter_grade}.")


