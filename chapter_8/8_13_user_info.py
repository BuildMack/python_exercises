# Exercise 8-13 from Python Crash Course Book
# Completed by Mack Sell

def build_profile(first,last,location = 'princeton',  **user_info):
    """Build a dictionary, contraining everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    user_info['location'] = location
    return user_info

user_profile = build_profile('albert','einstein',
                             field = 'physics')

print(user_profile)