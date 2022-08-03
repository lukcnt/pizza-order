# Greetings.
print("Welcome to Maringá Pizza Deliveries!")

# Orders options.
size = input("What size pizza do you want? S, M or L: ").lower()
add_pepperoni = input("Do you want pepperoni? Y or N: ").lower()
extra_cheese = input("Do you want extra cheese? Y or N: ").lower()

# Prices.
small_pizza = 15
medium_pizza = 20
large_pizza = 25
pepperoni_small_pizza = 2
pepperoni_medium_large_pizza = 3
add_cheese = 1

# User bill.
order = 0

# Processing the user order.
if size == "s":
    order += small_pizza
elif size == "m":
    order += medium_pizza
elif size == "l":
    order += large_pizza
else:
    print("That option isn't avaible")

if add_pepperoni == "y":
    if size == "s":
        order += pepperoni_small_pizza
    else:
        order += pepperoni_medium_large_pizza

if extra_cheese == "y":
    order += add_cheese

# Show a message with the total bill.
print(f"Your final bill is: ${order}.")