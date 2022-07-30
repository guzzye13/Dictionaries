# A DICTIONARY IN A DICTIONARY
users = {
    'aeinstein':{
        'first':'albert',
        'last':'einstein',
        'location':'princeton',
    },
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris',
    }
}
for username, user_info in users.items():  # loop through the users dictionary.
    # Python stores each key in the variable username, and the dictionary associated with each
    # username goes into the variable user_info.
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']  # variable user_info contains the dictionary
    # of user information, has three keys: 'first','last', and 'location'
    location = user_info['location']

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())