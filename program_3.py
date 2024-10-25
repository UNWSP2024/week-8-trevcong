#AUTHOR: Trevor Conger UNWSP
#DATE: 10/25/24
#TITLE: Guess the capital!

import random


#MAIN calls func
#GETS BACK number of correct and incorrect guesses
def main():
    correct, incorrect = func()
    print("You got", correct, "correct!")
    print("You got", incorrect, "incorrect!")

#FUNCTION to quiz the user on States and their Capitals
#RETURN back number of correct and incorrect guesses
#USER enters 0 to exit program
def func():
    us_state_capitals = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock',
    'California': 'Sacramento',
    'Colorado': 'Denver',
    'Connecticut': 'Hartford',
    'Delaware': 'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
    'Hawaii': 'Honolulu',
    'Idaho': 'Boise',
    'Illinois': 'Springfield',
    'Indiana': 'Indianapolis',
    'Iowa': 'Des Moines',
    'Kansas': 'Topeka',
    'Kentucky': 'Frankfort',
    'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta',
    'Maryland': 'Annapolis',
    'Massachusetts': 'Boston',
    'Michigan': 'Lansing',
    'Minnesota': 'St. Paul',
    'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City',
    'Montana': 'Helena',
    'Nebraska': 'Lincoln',
    'Nevada': 'Carson City',
    'New Hampshire': 'Concord',
    'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe',
    'New York': 'Albany',
    'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck',
    'Ohio': 'Columbus',
    'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem',
    'Pennsylvania': 'Harrisburg',
    'Rhode Island': 'Providence',
    'South Carolina': 'Columbia',
    'South Dakota': 'Pierre',
    'Tennessee': 'Nashville',
    'Texas': 'Austin',
    'Utah': 'Salt Lake City',
    'Vermont': 'Montpelier',
    'Virginia': 'Richmond',
    'Washington': 'Olympia',
    'West Virginia': 'Charleston',
    'Wisconsin': 'Madison',
    'Wyoming': 'Cheyenne'
    }
    correct = 0
    incorrect = 0

    while(True):
        state, capital = random.choice(list(us_state_capitals.items()))
        print("Enter 0 to exit")
        print("What is the capital of ", state)
        userInput = input(": ")
        if userInput == "0":
            break
        if userInput == capital:
            correct +=1
        else:
            incorrect +=1

    return correct, incorrect


if __name__ == "__main__":
    main()