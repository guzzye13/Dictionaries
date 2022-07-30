# Dictionaries allow us to connect pieces of related information
# This dictionary stores information about a particular alien:
alien_0 = {'color': 'green', 'points': 5} # this dictionary stores alien's color and point value.
new_points = alien_0['points'] # pulls value with the key 'points' from the dictionary.
print("You just earned " + str(new_points) + " points!\n") # converts int value to a string
print("Dictionary contains:", alien_0)

# ADDING TO THE DICTIONARY
alien_0['x_position'] = 0 # add new key value pair to the dictionary
alien_0['y-position'] = 25
print("Modified dictionary contains:", alien_0)


# STARTING WITH AN EMPTY DICTIONARY
print("\nStarting with empty dictionary")
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)




# Tracking the position of an alien that can move at different speeds.
alien_0 = {'x_position':0,'y_position':25, 'speed': 'medium'}
print("\nOriginal x-position:" + str(alien_0['x_position']))

# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow': # determines how far the alien should move
    x_increment = 1 # if slow then it moves one unit to the right.
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3
# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment # once incremented, its added to the value of x_position.
# the result is stored in the dictionary's x_position.

print("New x-position:" + str(alien_0['x_position']))


# REMOVING KEY-VALUE POINTS
alien_0 = {'color': 'green', 'points': 5}
print("\nKey-Value Points:", alien_0)
del alien_0['points'] # del tells python to delete the key 'points' and to remove value associated with that key as well.
print("Key-Value Points after deleting:", alien_0)

