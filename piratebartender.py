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

def question(y, n, yes, no):
    """Asks user questions to customize a drink"""
    for k, v in questions.items():
        print(v)
    
def custom_drink():
    """Produces the ingredients for the custom drink"""
    if questions.key() == True:
        for k, v in ingredients.item():
            print(random.choice(ingredients.values()))
        
if __name__ == '__main__':
