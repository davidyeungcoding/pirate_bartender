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

def customer_name():
    """Gets the user's name"""
    name = {}
    for k, v in name.items():
        user = input("Who are you? ")
        for user in name == True:
            one_more = input("Want another?")
        name.append(k)
    return name

def ask():
    """Asks user questions to customize a drink"""
    answers = {}
    for k, v in questions.items():
        response = input(v)
        if response == "y" or response == "yes":
            answers[k] = True
        else:
            answers[k] = False
    return answers
    
def custom_drink(answers):
    """Generates a custom drink based off of the users responses"""
    drink = []
    for k, v in ingredients.items():
        if answers[k] == True:
            drink.append(random.choice(v))
    return drink        

def name_generator():
    """Generates random name for drink"""
    drink_name = []
    for k, v in names.items():
        drink_name.append(random.choice(v))
    return drink_name

if __name__ == '__main__':
    while True:
        answers = ask()
        drink = custom_drink(answers)
        drink_name = name_generator()
        print(drink_name)
        print(drink)
        another = True
        response = input("Another? ")
        if response == "y" or response == "yes":
            another = True
        else:
            another = False
            break