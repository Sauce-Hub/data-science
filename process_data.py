import pandas as pd

def remove_duplicate(data):
    for name, df in data.items():
        data[name] = df.drop_duplicates()
    
    return data

def missing_data_fill(data):
    recipes = data["recipes"]

    # convert to minutes
    recipes["estimated_time"] = pd.to_timedelta(
        recipes["estimated_time"],
        errors="coerce"
    ).dt.total_seconds() / 60

    recipes["estimated_time"] = recipes["estimated_time"].fillna(0)

    recipes["Calories"] = recipes["Calories"].fillna(0)
    recipes["Fats"] = recipes["Fats"].fillna(0)
    recipes["Carbs"] = recipes["Carbs"].fillna(0)
    recipes["Protein"] = recipes["Protein"].fillna(0)

    data["recipes"] = recipes

    return data


def remove_invalid_values(data):
    recipes = data["recipes"]

    recipes = recipes[recipes["estimated_time"] > 0]
    recipes = recipes[recipes["Calories"] >= 0]
    recipes = recipes[recipes["Fats"] >= 0]
    recipes = recipes[recipes["Carbs"] >= 0]
    recipes = recipes[recipes["Protein"] >= 0]

    data["recipes"] = recipes

    return data

def process_data(data):
    data = remove_duplicate(data)
    data = missing_data_fill(data)
    data = remove_invalid_values(data)
    
    return data
    