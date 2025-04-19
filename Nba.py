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






