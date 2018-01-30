import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

def ask():
    """Asks user questions to customize a drink"""
    answers = {}
    for k, v in questions.items():
        answer = input(v)
        if answer == "y" or answer == "yes":
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

if __name__ == '__main__':
    answers = ask()
    drink = custom_drink(answers)
    print(drink)