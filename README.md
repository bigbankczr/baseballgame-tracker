# baseballgame-tracker
Personal project to track all the baseball games I've attended or watched in my life, with related milestones and stats pulled from MLB's Stats API. 

I've wanted a record of the games I've been to personally for a while, especially one with personal interactivity and substantial data, so I can see who played, what happened, and which milestone I witnessed.

## stack
- Python
- SQLite
- MLB Stats API

## structure
api/mlb.py - fetches and parses from MLB Stats API
database/tables.py defines schema
database/db.py connection handling and inserts
main.py entry point

## data model
### four tables
- game_log - one row per game with API data and personal fields (how it was watched, notes)

stats all keyed on game_pk(MLB API's game key) and player_id(Unique ID MLB creates each player)
- batting_stats - one row batting stats per player per game 
- pitching_stats - one row pitching stats per player per game
- fielding stats - one row fielding stats per player per game
season stats aren't stored, opted to calculate from individual games for data accuracy

## setup 
```bash
pip install -r requirements.txt
python database/tables.py
python main.py
```
