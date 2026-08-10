import pandas as pd

def remove_duplicate(data):
    for name, df in data.items():
        data[name] = df.drop_duplicates()
    
    return data

def remove_invalid_values(data):
    recipes = data["recipes"]

    recipes = recipes[recipes["estimated_time"] > 0]
    recipes = recipes[recipes["calories"] >= 0]
    recipes = recipes[recipes["fats"] >= 0]
    recipes = recipes[recipes["carbs"] >= 0]
    recipes = recipes[recipes["protein"] >= 0]

    data["recipes"] = recipes

    return data

def missing_data_fill(data):
    recipes = data["recipes"]
    
    recipes["estimated_time"] = recipes["estimated_time"].fillna(0)
    recipes["calories"] = recipes["calories"].fillna(0)
    recipes["fats"] = recipes["fats"].fillna(0)
    recipes["carbs"] = recipes["carbs"].fillna(0)
    recipes["protein"] = recipes["protein"].fillna(0)
    
    data["recipes"] = recipes
    
    return data

def check_category(data):
    recipes = data["recipes"]
    categories = data["categories"]
    
    known_category = set(categories["name"])
    
    new_category = recipes[
        ~recipes["category"].isin(known_category)
    ]["category"].dropna.unique()
    
    new_category = new_category.rename(columns={"category", "name"})
    
    data["category"] = pd.concat(
        [categories, new_category],
        ignore_index=True
    )
    
    return data
        
def process_data(data):
    data = remove_duplicate(data)
    data = remove_invalid_values(data)
    data = missing_data_fill(data)
    data = check_category(data)
    
    
    