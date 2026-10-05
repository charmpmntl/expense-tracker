# Laboratory 2 - Installment 2: Talking to the User
# Author: Charmei Pimentel
# A personal expense tracker that records two expenses.

print("=" * 40)
print("\tEXPENSE TRACKER")
print("\tI love Money.")
print("=" * 40)

print("MAIN MENU")
print("[1] Add an expense\t(coming soon)")
print("[2] View all expenses\t(coming soon)")
print("[3] Show total spent\t(coming soon)")
print("[4] Exit\t\t(coming soon)")

name = input("\nWhat's your name? ")
print(f"\nWelcome, {name}! Let's log two expenses.\n")

item1 = input("First expense? ")
amount1 = float(input("Amount? "))

item2 = input("Second expense? ")
amount2 = float(input("Amount? "))

total = amount1 + amount2
average = total / 2

print("-" * 40)
print("SUMMARY")
print(f"\t- {item1}:\t${amount1}")
print(f"\t- {item2}:\t${amount2}")
print(f"Total spent:\t${total}")
print(f"Average:\t${average}")
print("-" * 40)

print(f"Made by: {name}\t| Installment 2")