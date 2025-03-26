import sqlite3

def conectar_db():
    return sqlite3.connect("/Users/Saul/Downloads/archive/nba.sqlite")

def convert_height_to_meters(height_str):
    try:
        feet, inches = map(int, height_str.split("-"))
        total_inches = feet * 12 + inches
        meters = total_inches * 0.0254
        return round(meters, 2)
    except:
        return None

def meters_to_feet_inches(meters):
    total_inches = int(round(meters / 0.0254))
    feet = total_inches // 12
    inches = total_inches % 12
    return f"{feet}-{inches}"

def lbs_to_kg(lbs):
    return round(lbs * 0.453592, 2)

def kg_to_lbs(kg):
    return round(kg / 0.453592, 1)


