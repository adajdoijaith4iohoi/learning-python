# Program asks the user how the weather is (sunny, rainy, snowy).
# Uses if/elif/else to suggest what to do (e.g., “Wear sunglasses!”, “Bring an umbrella!”, etc.).
# Bonus: include a boolean for is_cold to change the advice.

print("Welcome to the weather assistant app!")

weather = input("How is the weather (sunny, rainy, or snowy): ")
is_cold = input("Is it cold outside (yes or no): ")

if is_cold == "yes":
    cold = True
    cold_message = "It is cold outside."
else:
    cold = False
    cold_message = ""



if weather == "sunny" and cold:
    print("Wear sunglasses and make sure to bring lots of water!")
elif weather == "rainy" and cold:
    print("Make sure to bring a umbrella and boots!")
elif weather == "snowy" and cold:
    print(f"Make sure to wear a lot of warm clothes and don't be outside for too long. {cold_message}")
elif cold:
    print("It is cold today make sure to wear extra warm clothing")
else:
    print("I don't seem to have advice for that kind of weather yet...")
