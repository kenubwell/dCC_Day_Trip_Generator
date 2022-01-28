#devCodeCamp Project 1 - DayTripGenerator
# Program will allow a user to have a random trip generated for them, making it less of a hassle to come up 
    # with trip ideas for the day! In it, you’ll utilize just a single Python file for all of the code and 
    # practice good debugging techniques, constantly testing every small chunk of code you write as you go along.
# (5 points): As a developer, I want to make at least three commits with descriptive messages. 
# (5 points): As a developer, I want to store my destinations, restaurants, mode of transportations, and entertainments in their own separate lists. 
# (5 points): As a user, I want a destination to be randomly selected for my day trip. 
# (5 points): As a user, I want a restaurant to be randomly selected for my day trip. 
# (5 points): As a user, I want a mode of transportation to be randomly selected for my day trip. 
# (5 points): As a user, I want a form of entertainment to be randomly selected for my day trip. 
# (15 points): As a user, I want to be able to randomly re-select a destination, restaurant, mode of transportation, and/or form of entertainment 
    # if I don’t like one or more of those things. 
# (10 points): As a user, I want to be able to confirm that my day trip is “complete” once I like all of the random selections. 
# (10 points): As a user, I want to display my completed trip in the console. 
# (5 points): As a developer, I want all of my functions to have a Single Responsibility. Remember, each function should do just one thing!

import random

#separate lists for each function
destinations = ['Tokyo', 'New York', 'Los Angeles', 'London', 'Singapore', 'Toronto', 'Istanbul', 'Mumbai', 'Cairo', 'Beijing', 'Las Vegas', 'Shanghai', 'Hong Kong', 'San Francisco', 'Seoul', 'Dubai', 'Saint Petersburg', 'Moscow', 'Rome', 'Madrid', 'Buenos Aires', 'Amersterdam', 'Manila', 'Chicago', 'Miami', 'Mexico City', 'Paris', 'Sydney', 'Lagos', 'Jakarta', 'San Diego', 'Orlando']

#function for random destination
def random_destination(dest_list):
    random_city = random.choice(dest_list)
    location = False
    confirmed_location = '' #for final summary
    dest_input = input(f'Welcome to the Day Trip Generator. Unsure about your next trip. Let us plan it for you. We have selected "{random_city}"! Does this sound good? ("Yes" or "No"): ')

    while location is False:
        if dest_input == 'Yes' or dest_input == 'yes' or dest_input == 'Y' or dest_input == 'y':
            location = True
            confirmed_location = random_city #for final summary
            print("That location is perfect. Let's move on to transportation.")
        elif dest_input == 'No' or dest_input == 'no' or dest_input == 'N' or dest_input == 'n':
            dest_list.remove(random_city)
            random_city = random.choice(dest_list) 
            dest_input = input(f'Not your preferred destination. Not a concern. Let us try something else. How about "{random_city}"? Enter "Yes" or "No": ')
    return confirmed_location  #for final summary  

random_destination(destinations)
