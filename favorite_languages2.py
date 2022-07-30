# A LIST IN A DICTIONARY
favorite_Languages2 = {  # value associated with each name is now a list.
    'jen':['python','ruby'],
    'sarah':['c'],
    'edward':['ruby','go'],
    'phil':['python','haskell'],
}
for name, languages in favorite_Languages2.items():    # we use the variable name languages to hold each value from the
    # dictionary, because we know that each value will be a list.
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:   # Inside the main dictionary loop, we use another for loop to run through
        # each person's list of favorite languages.
        print("\t" + language.title())