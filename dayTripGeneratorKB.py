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

#separate global lists for each function
destinations = ['Tokyo', 'New York', 'Los Angeles', 'London', 'Singapore', 'Toronto', 'Istanbul', 'Mumbai', 'Cairo', 'Beijing', 'Las Vegas', 'Shanghai', 'Hong Kong', 'San Francisco', 'Seoul', 'Dubai', 'Saint Petersburg', 'Moscow', 'Rome', 'Madrid', 'Buenos Aires', 'Amersterdam', 'Manila', 'Chicago', 'Miami', 'Mexico City', 'Paris', 'Sydney', 'Lagos', 'Jakarta', 'San Diego', 'Orlando']
restaurants = ['CAVA', 'Chipotle', 'P.F. Changs', 'Chick-fil-A', 'Asean Bistro', 'UNO Pizzeria & Grill', 'Outback Steakhouse', 'Yama Sushi', 'Boro Kabob', 'The Oceanaire Seafood Room', 'Bonefish Grill', 'Boru Ramen', 'True Food Kitchen', 'A Casa do Porco', 'Narisawa', 'Pizza Hut', 'Pho La Cay', 'Mali Thai Restaurant', 'Quintonil', 'Benu', 'Twins Garden', 'The BBQ Crew', 'The Clove Club', 'Burnt Ends', 'QDOBA', 'Atelier Crenn', 'McDonalds', 'Bonchon', 'Mission BBQ', 'First Watch', 'Taco Cabana']
transportation_options = ['airplane', 'rental car', 'train', 'Uber', 'shuttle', 'Lyft', 'subway', 'walk', 'bus', 'ferry', 'trolleybus', 'taxi']
entertainment_options = ['Light Show', 'Opera', 'Movie Theater', 'Museum', 'Amusement Park', 'City Tour', 'Shopping Mall', 'Sporting Event', 'Air Show', 'Comedy Show', 'Park', 'Tech Expo']

#function for random destination
def random_destination(dest_list):
    confirmed_location = '' #for final summary
    random_city = random.choice(dest_list)
    location = False
    dest_input = input(f'Welcome to the Day Trip Generator. Unsure about your next trip. Let us plan it for you. We have selected "{random_city}" as a destination! Does this sound good? ("Yes" or "No"): ')

    while location is False:
        if dest_input == 'Yes' or dest_input == 'yes' or dest_input == 'Y' or dest_input == 'y':
            location = True
            confirmed_location = random_city 
            print("That location is perfect. Let's move on to transportation.")
        elif dest_input == 'No' or dest_input == 'no' or dest_input == 'N' or dest_input == 'n':
            dest_list.remove(random_city)
            random_city = random.choice(dest_list) 
            dest_input = input(f'Not your preferred destination. Not a concern. Let us try something else. How about "{random_city}"? Enter "Yes" or "No": ')
        else:
            dest_input = input(f'Please enter in a correct response (e.g. "Yes" or "No") for "{random_city}": ')
    return confirmed_location  

#function for random transportation
def random_transportation(trans_list):
    confirmed_transportation = '' 
    random_trans = random.choice(trans_list)
    transpo = False
   
    trans_input = input(f'We have selected "{random_trans}" for your transportation. Does this sound good? ("Yes" or "No"): ')

    while transpo is False:
        if trans_input == 'Yes' or trans_input == 'yes' or trans_input == 'Y' or trans_input == 'y':
            transpo = True
            confirmed_transportation = random_trans 
            print("Safe Travels. Let's move on to selecting the restaurant.")
        elif trans_input == 'No' or trans_input == 'no' or trans_input == 'N' or trans_input == 'n':
            trans_list.remove(random_trans)
            random_trans = random.choice(trans_list) 
            trans_input = input(f'Not ideal. Let us try another option. How about "{random_trans}"? Enter "Yes" or "No": ')
        else:
            trans_input = input(f'Please enter in a correct response (e.g. "Yes" or "No") for "{random_trans}": ')
    return confirmed_transportation   

#function for random restaurant
def random_restaurant(rest_list):
    confirmed_restaurant = ''
    random_eatery = random.choice(rest_list)
    restaurant = False
    rest_input = input(f'We have selected "{random_eatery}" for your restaurant. Does this sound good? ("Yes" or "No"): ')

    while restaurant is False:
        if rest_input == 'Yes' or rest_input == 'yes' or rest_input == 'Y' or rest_input == 'y':
            restaurant = True
            confirmed_restaurant = random_eatery 
            print("That restaurant has great reviews. Let's move on to entertainment.")
        elif rest_input == 'No' or rest_input == 'no' or rest_input == 'N' or rest_input == 'n':
            rest_list.remove(random_eatery)
            random_eatery = random.choice(rest_list) 
            rest_input = input(f'Not the one. Let us try somewhere else to eat. How about "{random_eatery}"? Enter "Yes" or "No": ')
        else:
            rest_input = input(f'Please enter in a correct response (e.g. "Yes" or "No") for "{random_eatery}": ')
    return confirmed_restaurant  

#function for random entertainment
def random_entertainment(ent_list):
    confirmed_ent = '' 
    random_ent = random.choice(ent_list)
    venue = False
    ent_input = input(f'We have selected "{random_ent}" for your entertainment! Does this sound good? ("Yes" or "No"): ')

    while venue is False:
        if ent_input == 'Yes' or ent_input == 'yes' or ent_input == 'Y' or ent_input == 'y':
            venue = True
            confirmed_ent = random_ent 
            print('Perfect, it should be fun. Let us move on!')
        elif ent_input == 'No' or ent_input == 'no' or ent_input == 'N' or ent_input == 'n':
            ent_list.remove(random_ent)
            random_ent = random.choice(ent_list) 
            ent_input = input(f'Not feeling that activity. How about "{random_ent}"? Enter "Yes" or "No": ')
        else:
            ent_input = input(f'Please enter in a correct response (e.g. "Yes" or "No") for "{random_ent}": ')
    return confirmed_ent  


#function to execute, summarize, and confirm trip item selections
def summary_confirmation():
    conf_dest = random_destination(destinations)
    conf_trans = random_transportation(transportation_options)
    conf_rest = random_restaurant(restaurants)
    conf_ent = random_entertainment(entertainment_options)
    confirmation = False
    confirm_input = input(f'''Congrats! We have completed generating your day trip. Let's summarize and confirm the details.
    The trip that we generated for you includes:
    Destination: {conf_dest}
    Transportation: {conf_trans}
    Restaurant: {conf_rest}
    Entertainment: {conf_ent}
    Would you like to finalize this trip? Enter "Yes" or "No": ''')

    while confirmation is False:
        if confirm_input == 'Yes' or confirm_input == 'yes' or confirm_input == 'Y' or confirm_input == 'y':
            confirmation = True
            print(f"Prepare for your dream Day Trip! You'll be arriving in {conf_dest} by {conf_trans}, where you will spend the day at a {conf_ent}. You will end the evening dining at {conf_rest}. Enjoy your day!")
        elif confirm_input == 'No' or confirm_input == 'no' or confirm_input == 'N' or confirm_input == 'n':    
            print("No issues. Let's quickly go over each section again.")
            summary_confirmation()
            break
        else:
            continue
                    
#calling the summary function for final confirmation
summary_confirmation()




