import random

questions = {
    "strong": "Do ye like yer drinks strong? ",
    "salty": "Do ye like it with a salty tang? ",
    "bitter": "Are ye a lubber who likes it bitter? ",
    "sweet": "Would ye like a bit of sweetness with yer poison? ",
    "fruity": "Are ye one for a fruity finish? ",
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

names = {
    "adjective": ["Slippery", "Wet", "Prickly", "Briny", "Rough", "Callused"],
    "noun": ["Flipper", "Fin", "Paw", "Palm", "Boot"],
}

customer = {
    "David": ["slug of whisky", "salt-dusted rim"]
}

def ask():
    """Asks user questions to customize a drink"""
    answers = {}
    for style, question in questions.items():
        response = input(question)
        if response == "y" or response == "yes":
            answers[style] = True
        else:
            answers[style] = False
    return answers
    
def custom_drink(answers):
    """Generates a custom drink based off of the users responses"""
    drink = []
    for style, options in ingredients.items():
        if answers[style] == True:
            drink.append(random.choice(options))
    return drink        

def name_generator():
    """Generates random name for drink"""
    return random.choice(names["adjective"]) + " " + random.choice(names["noun"])

def customer_name():
    """Gets the user's name"""
    user = input("Who are you? ")
    for name, preference in customer.items():
        if user in customer == False:
            drink = custom_drink(ask())
            print(name_generator())
            print(drink)
            customer[name].append(user)
        else:
            print(customer[preference])
    return customer

if __name__ == '__main__':
    # while True:
        customer_name()
        # another = True
        # response = input("Another? ")
        # if response != "y" or response != "yes":
        #     another = False
        #     break