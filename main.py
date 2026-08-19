import sqlite3

from api.mlb import getSchedule, getBoxscore, parseBatting, parsePitching, parseFielding, getPlayerGameLog, parseGameLogBatting, getGame, parseGameLogPitching, parseGamesSeen
from database.db import insertRows, hasGamelog
from database.tables import createTables, sqlite3

def loadGame(game_pk):
    gameData = getGame(game_pk)
    print(gameData)
    officialDate = gameData['officialDate']
    box = getBoxscore(game_pk)

    battingRows = parseBatting(box, game_pk, officialDate)
    pitchingRows = parsePitching(box, game_pk, officialDate)
    fieldingRows = parseFielding(box, game_pk, officialDate)

    game = {
        "batting": insertRows("batting_stats", battingRows),
        "pitching": insertRows("pitching_stats", pitchingRows),
        "fielding": insertRows("fielding_stats", fieldingRows)
    }

    batters = {}
    for row in battingRows:
        batters[row["player_id"]] = (row["player_name"], row["season"])

    for player_id, (player_name, season) in batters.items():
        if hasGamelog("gamelogs_batting", player_id, season):
            continue
        splits = getPlayerGameLog(player_id, season, "hitting")
        insertRows("gamelogs_batting", parseGameLogBatting(splits, player_id, player_name))

    pitchers = {}
    for row in pitchingRows:
        pitchers[row["player_id"]] = (row["player_name"], row["season"])

    for player_id, (player_name, season) in pitchers.items():
        if hasGamelog("gamelogs_pitching", player_id, season):
            continue
        splits = getPlayerGameLog(player_id, season, "pitching")
        insertRows("gamelogs_pitching", parseGameLogPitching(splits, player_id, player_name))

    return game

def logGame(user_id, game_pk, attendance_type, game_notes=None, milestone=None):
    game = getGame(game_pk)
    row = parseGamesSeen(game, attendance_type, game_notes, milestone)
    row["user_id"] = user_id
    return insertRows("games_seen", [row])


if __name__ == "__main__":
    createTables()

    conn = sqlite3.connect("database/baseball.db")
    conn.execute("INSERT OR IGNORE INTO users (username) VALUES (?)", ("cesar",))
    conn.commit()
    conn.close()

    logGame(1, 746170, "in_person")
