prompt = "\nEnter the pizza toppings"
prompt += "(enter 'quit' when you're finished): "

active = True

while active:
    topping = input(prompt)

    if topping == 'quit':
        active = False
    else:
        print(f"I will add {topping.lower()} to your pizza")


