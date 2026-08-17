from api.mlb import getSchedule, getBoxscore, parseBatting, parsePitching, parseFielding, getPlayerGameLog, parseGameLogBatting, getGame, parseGameLogPitching
from database.db import insertRows
from database.tables import createTables

def loadGame(game_pk):
    gameData = getGame(game_pk)
    officialDate = gameData['officialDate']
    box = getBoxscore(game_pk)
    game = {
        "batting": insertRows("batting_stats", parseBatting(box, game_pk, officialDate)),
        "pitching": insertRows("pitching_stats", parsePitching(box, game_pk, officialDate)),
        "fielding": insertRows("fielding_stats", parseFielding(box,game_pk, officialDate))
    }
    return game
if __name__ == "__main__":
    createTables()
