# LOOPING THROUGH ALL KEY-VALUE PAIRS
user_0 = {
    'username':'enfermi',
    'first':'enrico',
    'last':'fermi',
    }
for key, value in user_0.items(): # to write a loop for a dictionary, you create
    # names for the two variables that will hold the key and value in each key-value pair.
    # You can choose any names for these two variables.
    # for k, v in user_0.items()
    print("\nKey:" + key) # Use the variables to print each key followed by the associated value.
    print("Value:" + value) # \n blank line inserted before each key-value pair in the output.
