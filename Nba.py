import sqlite3
import webbrowser

def conectar_db():
    return sqlite3.connect("/Users/fernandosoriano/Downloads/nba.sqlite")

def convert_height_to_meters(height_str):
    try:
        feet, inches = map(int, height_str.split("-"))
        total_inches = feet * 12 + inches
        meters = total_inches * 0.0254
        return round(meters, 2)
    except:
        return None

def convert_lbs_to_kg(lbs):
    return round(lbs * 0.453592, 2)

def convert_height_to_inches(height_str):
    try:
        feet, inches = map(int, height_str.split("-"))
        return feet * 12 + inches
    except:
        return None

def load_players(conn):
    cursor = conn.cursor()
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
    return players




