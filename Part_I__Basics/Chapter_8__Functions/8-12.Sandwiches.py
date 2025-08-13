def sandwich(*ingredients):  
    print("\nThe customer wants a sandwich with the following ingredients:")
    for ingredient in ingredients:  
        print(f"- {ingredient}")

# Call the function three times, using a difffent number of arguments each time.
if __name__ == '__main__':
    sandwich("bread", "lettuce", "tomato", "mayo")
    sandwich('bread', 'cheese', 'mayonnaise', 'ham', 'tomatoes')
    sandwich('bread', 'avocado', 'mayonnaise', 'tuna salad')

