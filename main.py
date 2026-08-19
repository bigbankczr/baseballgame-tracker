from api.mlb import getSchedule, getBoxscore, parseBatting, parsePitching, parseFielding, getPlayerGameLog, parseGameLogBatting, getGame, parseGameLogPitching
from database.db import insertRows, hasGamelog
from database.tables import createTables

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

if __name__ == "__main__":
    createTables()
    print(loadGame(746170))
