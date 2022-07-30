favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}
print("Sarah's favorite language is " +
      favorite_languages['sarah'].title() +
      ".")
print("\nUsing a for loop:")
for name, language in favorite_languages.items(): # python to loop through each key-value pair in the dictionary.
    # the key is stored in the variable name
    # the value is stored in the variable language
    print(name.title() + "'s favorite language is " +
          language.title() + ".")

print("\nLooping through all keys in a Dictionary:")
for name in favorite_languages.keys(): # keys() useful when you don't need to work
    # with all of the values in the dictionary.
    # tells python to pull all the keys from the dictionary favorite_languages
    # and store them one at a time in the variable name.
    print(name.title())

print("\nPrinting a message: ")
friends = ['jen','sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print("  Hi " + name.title() +
              ", I see your favorite language is " +
              favorite_languages[name].title() + "!")


# LOOPING THROUGH A DICTIONARY'S KEYS IN ORDER
print("\nLooping in Order:")
for name in sorted(favorite_languages.keys()): # sorted() function to get a copy of the keys in order.
    print(name.title() + ", thank you for taking the poll!")


# LOOPING THROUGH ALL VALUES IN A DICTIONARY
print("\nThe following languages have been mentioned:")
for language in set (favorite_languages.values()): # set() around a list that contains duplicate items,
    # Python identifies the unique items in the list and builds a set from those items.
    # Used set() to pull out the unique languages in favorite_languages.values().
    print(language.title())