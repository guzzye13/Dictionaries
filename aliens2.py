# alien dictionary that stores information for more than one alien.
# This is called nesting, you can nest a set of dictionaries inside a list,
# a list of items inside a dictionary or even a dictionary inside another dictionary.
# following is an example of nesting.
alien_0 = {'color':'green','points':5}
alien_1 = {'color':'yellow','points':10}
alien_2 = {'color':'red','points':15}

aliens = [alien_0,alien_1,alien_2] # created 3 dictionaries representing a different alien.
# packed each of these dictionaries into a list called aliens.

for alien in aliens:
    print(alien)




# Make an empty list for storing aliens
# Use range() to create a fleet of 30 aliens.
print("\nStoring aliens:")
aliens = []

# Make 30 green aliens.
for alien_number in range(30): # range() returns a set of numbers
    # Tells python how many times we want the loop to repeat.
    new_alien = {'color':'green','points':5,'speed':'slow'} # each loop we create a new alien
    aliens.append(new_alien) # append each new alien to the list

# To Change the first three aliens to yellow, medium-speed, worth 10 pts, we do the following:
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    # expand this loop by adding an elif block that turns yellow aliens into red, fast-speed, 15pts:
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15


# Show the first 5 aliens.
for alien in aliens[:5]: # use a slice to print the first five aliens
    print(alien)
print("...")

# Show how many aliens have been created.
print("Total number of aliens:" + str(len(aliens))) # print the length of the list.