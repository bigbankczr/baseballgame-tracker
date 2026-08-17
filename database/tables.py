import sqlite3

connection = sqlite3.connect('baseball.db')
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS game_log(
    game_pk INTEGER PRIMARY KEY,
    official_date TEXT NOT NULL,
    season INTEGER,
    game_type TEXT,
    home_team TEXT,
    away_team TEXT,
    home_score INTEGER,
    away_score INTEGER,
    venue_name TEXT,
    day_night TEXT,
    game_number INTEGER,
    attendance_type TEXT
    CHECK (attendance_type IN('in_person', 'television', 'radio', 'other')),
    tracked_game_number INTEGER,
    game_notes TEXT,
    milestone TEXT,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
    )
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS batting_stats (
    game_pk INTEGER NOT NULL,
    player_id INTEGER NOT NULL,
    official_date TEXT NOT NULL,
    season INTEGER,
    player_name TEXT,
    team TEXT,
    batting_order INTEGER,
    at_bats INTEGER,
    plate_appearances INTEGER,
    runs INTEGER,
    hits INTEGER,
    doubles INTEGER,
    triples INTEGER,
    home_runs INTEGER,
    rbi INTEGER,
    total_bases INTEGER,
    strike_outs INTEGER,
    base_on_balls INTEGER,
    intentional_walks INTEGER,
    hit_by_pitch INTEGER,
    stolen_bases INTEGER,
    caught_stealing INTEGER,
    left_on_base INTEGER,
    sac_bunts INTEGER,
    sac_flies INTEGER,
    ground_into_double_play INTEGER,
    ground_into_triple_play INTEGER,
    catchers_interference INTEGER,
    pickoffs INTEGER,
    fly_outs INTEGER,
    ground_outs INTEGER,
    air_outs INTEGER,
    pop_outs INTEGER,
    line_outs INTEGER,
    PRIMARY KEY (game_pk, player_id)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS pitching_stats (
    game_pk INTEGER NOT NULL,
    player_id INTEGER NOT NULL,
    official_date TEXT NOT NULL,
    season INTEGER,
    player_name TEXT,
    team TEXT,
    games_started INTEGER,
    games_finished INTEGER,
    complete_games INTEGER,
    shutouts INTEGER,
    wins INTEGER,
    losses INTEGER,
    saves INTEGER,
    save_opportunities INTEGER,
    holds INTEGER,
    blown_saves INTEGER,
    innings_pitched TEXT,
    outs INTEGER,
    batters_faced INTEGER,
    number_of_pitches INTEGER,
    balls INTEGER,
    strikes INTEGER,
    runs INTEGER,
    earned_runs INTEGER,
    hits INTEGER,
    doubles INTEGER,
    triples INTEGER,
    home_runs INTEGER,
    strike_outs INTEGER,
    base_on_balls INTEGER,
    intentional_walks INTEGER,
    hit_batsmen INTEGER,
    balks INTEGER,
    wild_pitches INTEGER,
    pickoffs INTEGER,
    stolen_bases INTEGER,
    caught_stealing INTEGER,
    inherited_runners INTEGER,
    inherited_runners_scored INTEGER,
    sac_bunts INTEGER,
    sac_flies INTEGER,
    passed_ball INTEGER,
    catchers_interference INTEGER,
    fly_outs INTEGER,
    ground_outs INTEGER,
    air_outs INTEGER,
    pop_outs INTEGER,
    line_outs INTEGER,
    PRIMARY KEY (game_pk, player_id)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS fielding_stats (
    game_pk INTEGER NOT NULL,
    player_id INTEGER NOT NULL,
    official_date TEXT NOT NULL,
    season INTEGER,
    player_name TEXT,
    team TEXT,
    position TEXT,
    games_started INTEGER,
    assists INTEGER,
    put_outs INTEGER,
    errors INTEGER,
    chances INTEGER,
    passed_ball INTEGER,
    pickoffs INTEGER,
    stolen_bases INTEGER,
    caught_stealing INTEGER,
    PRIMARY KEY (game_pk, player_id)
)
""")

connection.commit()
connection.close()

