import pandas as pd

def load_data():
    recipes = pd.read_csv(r"E:\data-science\data\seed\recipes.csv")
    ingredients = pd.read_csv(r"E:\data-science\data\seed\ingredients.csv")
    favorites = pd.read_csv(r"E:\data-science\data\seed\favorites.csv")
    comments = pd.read_csv(r"E:\data-science\data\seed\comments.csv")
    users = pd.read_csv(r"E:\data-science\data\seed\users.csv")
    chat_history = pd.read_csv(r"E:\data-science\data\seed\chat_history.csv")
    
    return (
        recipes,
        ingredients,
        favorites,
        comments,
        users,
        chat_history
    )
    
    
## will be replaced by read sql