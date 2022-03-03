programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}

#Retrieving items from the dictionary.
#print(programming_dictionary["Function"])

#Adding new items to the dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."


empty_dictionary = {}

#Wipe an existing dictionary
'''programming_dictionary = {}
print(programming_dictionary)'''

#Edit an item in the dictionary
programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary)

#Loop through the dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

#Nesting dictionary in a dictionary
travel_log = {
    'France' : {'cities_visited' :['Paris', 'Lille', 'Dijo'], 'total_visits' : 12},
    'Germany' : {'cities_visited' : ['Berlin', 'Hamburg', 'Stuttgart'], 'total_visits' : 5}
}

#Nesting dictionary in a list

travel_log = [
    {
        'country' : 'France',
        'cities_visited' :['Paris', 'Lille', 'Dijo'],
        'total_visits' : 12
    },
    {
        'country' : 'Germany',
        'cities_visited' : ['Berlin', 'Hamburg', 'Stuttgart'],
        'total_visits' : 5
    }
]
