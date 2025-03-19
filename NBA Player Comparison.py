players = [
    {"name": "Devin Booker", "height": 1.96, "weight": 93, "playstyle": ["scorer", "playmaker"]},
    {"name": "Klay Thompson", "height": 1.98, "weight": 97, "playstyle": ["shooter"]},
    {"name": "Bradley Beal", "height": 1.93, "weight": 94, "playstyle": ["scorer", "playmaker"]},
    {"name": "Stephen Curry", "height": 1.88, "weight": 84, "playstyle": ["shooter", "playmaker"]},
    {"name": "Giannis Antetokounmpo", "height": 2.11, "weight": 109, "playstyle": ["slasher", "defender"]},
]

def calculate_similarity(user, player):
    height_diff = abs(user["height"] - player["height"])
    weight_diff = abs(user["weight"] - player["weight"])
    playstyle_match = len(set(user["playstyle"]) & set(player["playstyle"]))
    
    similarity_score = (1 - height_diff) + (1 - weight_diff / 50) + (2 * playstyle_match)
    return similarity_score


user_height = float(input("Enter your height (in meters): "))
user_weight = float(input("Enter your weight (in kg): "))
user_playstyle = input("Enter your playstyle (e.g., shooter, playmaker, defender): ").split(", ")


user_profile = {"height": user_height, "weight": user_weight, "playstyle": user_playstyle}



