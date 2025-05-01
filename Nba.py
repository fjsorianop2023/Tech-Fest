import sqlite3
import webbrowser


conn = sqlite3.connect("/Users/fernandosoriano/Downloads/nba.sqlite")
cursor = conn.cursor()


def convert_height_to_inches(height_str):
    try:
        feet, inches = map(int, height_str.split("-"))
        return feet * 12 + inches
    except:
        return None


cursor.execute("""
    SELECT display_first_last, school, country, height, weight, jersey, position, team_name, draft_year, draft_round, draft_number
    FROM common_player_info
    WHERE height IS NOT NULL 
      AND weight IS NOT NULL 
      AND position IS NOT NULL 
      AND draft_year IS NOT NULL
""")
rows = cursor.fetchall()

players = []
for row in rows:
    name, school, country, height_str, weight_str, jersey, position, team, draft_year, draft_round, draft_number = row
    height_in = convert_height_to_inches(height_str)
    if height_in is None or not weight_str:
        continue
    try:
        weight_lbs = float(weight_str)
    except ValueError:
        continue
    players.append({
        "name": name,
        "school": school.lower() if school else "",
        "country": country.lower() if country else "",
        "height_in": height_in,
        "weight_lbs": weight_lbs,
        "jersey": str(jersey),
        "position": position.lower() if position else "",
        "team": team.lower() if team else "",
        "draft_year": str(draft_year),
        "draft_round": str(draft_round),
        "draft_pick": str(draft_number)
    })

print("NBA Player Comparison Tool")
school = input("Enter the school you played for: ").strip().lower()
country = input("Enter your country: ").strip().lower()
height = input("Enter your height (e.g., 6-10): ").strip()
weight = float(input("Enter your weight in lbs (e.g., 220): "))
jersey = input("Enter your jersey number: ").strip()
position = input("Enter your position (e.g., guard, forward, center): ").strip().lower()
team = input("Enter your current or favorite team: ").strip().lower()
draft_year = input("Enter your draft year: ").strip()
draft_round = input("Enter your draft round: ").strip()
draft_pick = input("Enter your draft pick number: ").strip()


height_in = convert_height_to_inches(height)


user = {
    "school": school,
    "country": country,
    "height_in": height_in,
    "weight_lbs": weight,
    "jersey": jersey,
    "position": position,
    "team": team,
    "draft_year": draft_year,
    "draft_round": draft_round,
    "draft_pick": draft_pick
}


def similarity_score(user, player):
    score = 0
    if user["school"] == player["school"]:
        score += 3
    if user["country"] == player["country"]:
        score += 3
    if user["jersey"] == player["jersey"]:
        score += 2
    if user["position"] == player["position"]:
        score += 3
    if user["team"] == player["team"]:
        score += 2
    if user["draft_year"] == player["draft_year"]:
        score += 2
    if user["draft_round"] == player["draft_round"]:
        score += 2
    if user["draft_pick"] == player["draft_pick"]:
        score += 2
    score += 1 - abs(user["height_in"] - player["height_in"]) / 20
    score += 1 - abs(user["weight_lbs"] - player["weight_lbs"]) / 50
    return score


best_match = max(players, key=lambda p: similarity_score(user, p))


print("\n--- Your NBA Comparison ---")
print(f"Most similar to: {best_match['name']}")
print(f"Team: {best_match['team'].title()}")
print(f"School: {best_match['school'].title()}")
print(f"Country: {best_match['country'].title()}")
print(f"Height: {height}")
print(f"Weight: {weight} lbs")
print(f"Jersey #: {best_match['jersey']}")
print(f"Position: {best_match['position'].title()}")
print(f"Draft Year: {best_match['draft_year']} | Round: {best_match['draft_round']} | Pick: {best_match['draft_pick']}")


query = best_match['name'].replace(" ", "+") + "+nba+player"
url = f"https://duckduckgo.com/?q={query}&t=h_&iax=images&ia=images"
webbrowser.open(url)

conn.close()





