import pandas as pd

def load_data():
    recipes = pd.read_csv(r"E:\data-science\data\seed_data\Receipt.csv")
    ingredients = pd.read_csv(r"E:\data-science\data\seed_data\Ingredient.csv")
    favorites = pd.read_csv(r"E:\data-science\data\seed_data\Favorites.csv")
    users = pd.read_csv(r"E:\data-science\data\seed_data\User.csv")
    likes_recipes = pd.read_csv(r"E:\data-science\data\seed_data\Likes_Receipt.csv")
    recommendations = pd.read_csv(r"E:\data-science\data\seed_data\Recommendations.csv")
    
    return {
        "recipes": recipes,
        "ingredients": ingredients,
        "favorites": favorites,
        "users": users,
        "likes_recipes": likes_recipes,
        "recommendations": recommendations
    }
    
    
## will be replaced by read sql
'''
from sqlalchemy import create_engine
DATABASE_URL = "path"
engine = create_engine(DATABASE_URL)
'''