prompt = "\nEnter the pizza toppings"
prompt += "(enter 'quit' when you're finished): "

while True:
    topping = input(prompt)
    
    if topping == 'quit':
        break
    else:
        print(f"I will add {topping} to your pizza.")

