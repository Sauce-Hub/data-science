import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity

def get_recommendation(data, user_id, num = 20):
    features = [
        "calories",
        "fats",
        "carbs",
        "protein",
        "estimated_time"
    ]
    
    recipes = data["recipes"]
    favorites = data["favorites"]
    likes_recipe = data["likes_recipes"]
    cur_recommend = data["recommendations"]
    
    # to reset index to match cosine similarity
    recipes = recipes.reset_index(drop=True)
    
    user_likes = likes_recipe[likes_recipe["user_id"] == user_id]
    likes_ids = user_likes["receipt_id"].tolist()
    
    user_favs = favorites[favorites["user_id"] == user_id]
    favs_ids = user_favs["receipt_id"].tolist()
    
    if not favs_ids and not likes_ids:
        return []
    
    fav_indices = recipes.index[ recipes["receipt_id"].isin(favs_ids)].tolist()
    likes_indices = recipes.index[recipes["receipt_id"].isin(likes_ids)].tolist()
    
    # Find most prefered category
    category_scores = {}
    
    for idx in fav_indices:
        category = recipes.loc[idx, "category"]
        category_scores[category] = (category_scores.get(category,0)+2)
        
    for idx in likes_indices:
        category = recipes.loc[idx, "category"]
        category_scores[category] = (category_scores.get(category,0)+1)
    
    top_category = max(category_scores, key = category_scores.get)
    
    
    featured = recipes[features]
    scaler = StandardScaler()
    
    matrix = scaler.fit_transform(featured)
    
    similarity = cosine_similarity(matrix)
    
    recipe_scores = {}
    for recipe_idx in range(len(recipes)):
        score = 0
        weight = 0
        
        for fav_idx in fav_indices:
            score += 2 * similarity[fav_idx][recipe_idx]
            weight += 2
        
        for like_idx in likes_indices:
            score += similarity[like_idx][recipe_idx]
            weight += 1
            
        if weight > 0:
            score /= weight
            
        if recipes.loc[recipe_idx, "category"] == top_category:
            score += 3
        
        recipe_scores[recipe_idx] = score
        
        
    # reomve already recommended before
    recommendations = cur_recommend[cur_recommend["user_id"] == user_id]
    recommed_ids = recommendations["receipt_id"].tolist()
    recommend_indices = recipes.index[recipes["receipt_id"].isin(recommed_ids)].tolist()
    
    for idx in recommend_indices:
        recipe_scores[idx] = -1
    
    top = sorted(recipe_scores, key=recipe_scores.get, reverse=True)[:num]
    
    recommendations = []
    
    for idx in top:
        if recipe_scores[idx] == -1:
            continue
        
        recommendations.append({
            "user_id":user_id,
            "receipt_id":recipes.loc[idx, "receipt_id"],
            "seen": False
        })
        
    return recommendations
        
        
# Answer for each user, what recipes should I suggest