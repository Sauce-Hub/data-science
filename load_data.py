import os
import pandas as pd
from pathlib import Path
from sqlalchemy import create_engine
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

DATABASE_URL = (
    f"postgresql+psycopg2://"
    f"{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}"
    f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}"
    f"/{os.getenv('DB_DATABASE')}"
    f"?sslmode={os.getenv('DB_SSLMODE', 'require')}"
)

engine = create_engine(DATABASE_URL)


def load_data():
    recipes = pd.read_sql("SELECT * FROM public.receipts", engine)
    ingredients = pd.read_sql("SELECT * FROM public.ingredients", engine)
    favorites = pd.read_sql("SELECT * FROM public.favorites", engine)
    users = pd.read_sql("SELECT * FROM public.users", engine)
    likes_receipts = pd.read_sql( "SELECT * FROM public.likes_receipts", engine )
    recommendations = pd.read_sql( 'SELECT * FROM public."Recommendations"', engine)

    return {
        "recipes": recipes,
        "ingredients": ingredients,
        "favorites": favorites,
        "users": users,
        "likes_receipts": likes_receipts,
        "recommendations": recommendations
    }