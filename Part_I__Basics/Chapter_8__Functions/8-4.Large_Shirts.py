def make_shirt(size='large', text='I love Python'):
    print(f"\nThe size of the t-shirt is {size} and the text printed on it is '{text}'.")

# Using default values.
make_shirt()    # large shirt
make_shirt('medium')    # medium shirt

# Using keyword arguments.
make_shirt(size='extra large', text='I use Arch btw') 
