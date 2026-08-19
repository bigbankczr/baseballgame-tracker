import requests
from datetime import datetime
baseURL = "https://statsapi.mlb.com/api/v1"

def getGame(game_pk):
    url = f"{baseURL}/schedule?sportId=1&gamePks={game_pk}"
    response = requests.get(url)
    data= response.json()
    return data["dates"][0]["games"][0]


def getSchedule(teamID, startDate, endDate):
    url = f"{baseURL}/schedule?sportId=1&teamId={teamID}&startDate={startDate}&endDate={endDate}"
    response = requests.get(url)
    data = response.json()
    return data

def getBoxscore(game_pk):
    url = f"{baseURL}/game/{game_pk}/boxscore"
    return requests.get(url).json()

def parseFielding(boxscore, game_pk, official_date):
    rows = []
    for side in ["home", "away"]:
        teamData = boxscore["teams"][side]
        for playerKey, player in teamData["players"].items():
            fielding = player.get("stats", {}).get("fielding", {})
            if not fielding:
                continue
            player_id = int(playerKey[2:])
            player_name = player["person"]["fullName"]
            team_name = teamData["team"]["name"]
            rows.append({
                "game_pk": game_pk,
                "player_id": player_id,
                "official_date": official_date,
                "player_name": player_name,
                "team": team_name,
                "season": int(official_date[:4]),
                "position": player.get("position", {}).get("abbreviation"),
                "games_started": fielding.get("gamesStarted", 0),
                "assists": fielding.get("assists", 0),
                "put_outs": fielding.get("putOuts", 0),
                "errors": fielding.get("errors", 0),
                "chances": fielding.get("chances", 0),
                "passed_ball": fielding.get("passedBall", 0),
                "pickoffs": fielding.get("pickoffs", 0),
                "stolen_bases": fielding.get("stolenBases", 0),
                "caught_stealing": fielding.get("caughtStealing", 0),
            })
    return rows


def parsePitching(boxscore, game_pk, official_date):
    rows = []
    for side in ["home", "away"]:
        teamData = boxscore["teams"][side]
        for playerKey, player in teamData["players"].items():
            pitching = player.get("stats", {}).get("pitching", {})
            if not pitching:
                continue
            player_id = int(playerKey[2:])
            player_name = player["person"]["fullName"]
            team_name = teamData["team"]["name"]
            rows.append({
                "game_pk": game_pk,
                "player_id": player_id,
                "official_date": official_date,
                "player_name": player_name,
                "team" : team_name,
                "season": int(official_date[:4]),
                "games_started": pitching.get("gamesStarted", 0),
                "games_finished": pitching.get("gamesFinished", 0),
                "complete_games": pitching.get("completeGames", 0),
                "shutouts": pitching.get("shutouts", 0),
                "wins": pitching.get("wins", 0),
                "losses": pitching.get("losses", 0),
                "saves": pitching.get("saves", 0),
                "save_opportunities": pitching.get("saveOpportunities", 0),
                "holds": pitching.get("holds", 0),
                "blown_saves": pitching.get("blownSaves", 0),
                "innings_pitched": pitching.get("inningsPitched", "0.0"),
                "outs": pitching.get("outs", 0),
                "batters_faced": pitching.get("battersFaced", 0),
                "number_of_pitches": pitching.get("numberOfPitches", 0),
                "balls": pitching.get("balls", 0),
                "strikes": pitching.get("strikes", 0),
                "runs": pitching.get("runs", 0),
                "earned_runs": pitching.get("earnedRuns", 0),
                "hits": pitching.get("hits", 0),
                "doubles": pitching.get("doubles", 0),
                "triples": pitching.get("triples", 0),
                "home_runs": pitching.get("homeRuns", 0),
                "strike_outs": pitching.get("strikeOuts", 0),
                "base_on_balls": pitching.get("baseOnBalls", 0),
                "intentional_walks": pitching.get("intentionalWalks", 0),
                "hit_batsmen": pitching.get("hitBatsmen", 0),
                "balks": pitching.get("balks", 0),
                "wild_pitches": pitching.get("wildPitches", 0),
                "pickoffs": pitching.get("pickoffs", 0),
                "stolen_bases": pitching.get("stolenBases", 0),
                "caught_stealing": pitching.get("caughtStealing", 0),
                "inherited_runners": pitching.get("inheritedRunners", 0),
                "inherited_runners_scored": pitching.get("inheritedRunnersScored", 0),
                "sac_bunts": pitching.get("sacBunts", 0),
                "sac_flies": pitching.get("sacFlies", 0),
                "passed_ball": pitching.get("passedBall", 0),
                "catchers_interference": pitching.get("catchersInterference", 0),
                "fly_outs": pitching.get("flyOuts", 0),
                "ground_outs": pitching.get("groundOuts", 0),
                "air_outs": pitching.get("airOuts", 0),
                "pop_outs": pitching.get("popOuts", 0),
                "line_outs": pitching.get("lineOuts", 0),
            })
    return rows

def parseBatting(boxscore, game_pk, official_date):
    rows = []
    for side in ["home", "away"]:
        teamData = boxscore["teams"][side]
        for playerKey, player in teamData["players"].items():
            batting = player.get("stats", {}).get("batting", {})
            if not batting:
                continue
            player_id = int(playerKey[2:])
            player_name = player["person"]["fullName"]
            team_name = teamData["team"]["name"]
            rows.append({
                "game_pk": game_pk,
                "player_id": player_id,
                "official_date": official_date,
                "player_name": player_name,
                "team" : team_name,
                "at_bats" : batting.get("atBats", 0),
                "runs" : batting.get("runs", 0),
                "hits" : batting.get("hits", 0),
                "home_runs" : batting.get("homeRuns", 0),
                "plate_appearances": batting.get("plateAppearances", 0),
                "doubles": batting.get("doubles", 0),
                "triples": batting.get("triples", 0),
                "rbi": batting.get("rbi", 0),
                "total_bases": batting.get("totalBases", 0),
                "strike_outs": batting.get("strikeOuts", 0),
                "base_on_balls": batting.get("baseOnBalls", 0),
                "intentional_walks": batting.get("intentionalWalks", 0),
                "hit_by_pitch": batting.get("hitByPitch", 0),
                "stolen_bases": batting.get("stolenBases", 0),
                "caught_stealing": batting.get("caughtStealing", 0),
                "left_on_base": batting.get("leftOnBase", 0),
                "sac_bunts": batting.get("sacBunts", 0),
                "sac_flies": batting.get("sacFlies", 0),
                "ground_into_double_play": batting.get("groundIntoDoublePlay", 0),
                "ground_into_triple_play": batting.get("groundIntoTriplePlay", 0),
                "catchers_interference": batting.get("catchersInterference", 0),
                "pickoffs": batting.get("pickoffs", 0),
                "fly_outs": batting.get("flyOuts", 0),
                "ground_outs": batting.get("groundOuts", 0),
                "air_outs": batting.get("airOuts", 0),
                "pop_outs": batting.get("popOuts", 0),
                "line_outs": batting.get("lineOuts", 0),
                "season": int(official_date[:4]),
            })
    return rows

def getPlayerGameLog(player_id, season, group):
    url = f"{baseURL}/people/{player_id}/stats?stats=gameLog&season={season}&group={group}"
    data = requests.get(url).json()
    stats = data.get("stats", [])
    if not stats:
        return []
    return stats[0].get("splits", [])

def parseGameLogBatting(splits, player_id, player_name):
    rows = []
    for split in splits:
        stat = split["stat"]
        rows.append({
            "game_pk": split["game"]["gamePk"],
            "player_id": player_id,
            "official_date": split["date"],
            "season": int(split["season"]),
            "player_name": player_name,
            "team": split["team"]["name"],
            "at_bats": stat.get("atBats", 0),
            "plate_appearances": stat.get("plateAppearances", 0),
            "runs": stat.get("runs", 0),
            "hits": stat.get("hits", 0),
            "doubles": stat.get("doubles", 0),
            "triples": stat.get("triples", 0),
            "home_runs": stat.get("homeRuns", 0),
            "rbi": stat.get("rbi", 0),
            "total_bases": stat.get("totalBases", 0),
            "strike_outs": stat.get("strikeOuts", 0),
            "base_on_balls": stat.get("baseOnBalls", 0),
            "intentional_walks": stat.get("intentionalWalks", 0),
            "hit_by_pitch": stat.get("hitByPitch", 0),
            "stolen_bases": stat.get("stolenBases", 0),
            "caught_stealing": stat.get("caughtStealing", 0),
            "left_on_base": stat.get("leftOnBase", 0),
            "sac_bunts": stat.get("sacBunts", 0),
            "sac_flies": stat.get("sacFlies", 0),
            "ground_into_double_play": stat.get("groundIntoDoublePlay", 0),
            "ground_into_triple_play": stat.get("groundIntoTriplePlay", 0),
            "catchers_interference": stat.get("catchersInterference", 0),
            "pickoffs": stat.get("pickoffs", 0),
            "fly_outs": stat.get("flyOuts", 0),
            "ground_outs": stat.get("groundOuts", 0),
            "air_outs": stat.get("airOuts", 0),
            "pop_outs": stat.get("popOuts", 0),
            "line_outs": stat.get("lineOuts", 0),
            "fetched_at": datetime.now().isoformat(),
        })
    return rows

def parseGameLogPitching(splits, player_id, player_name):
    rows = []
    for split in splits:
        stat = split["stat"]
        rows.append({
            "game_pk": split["game"]["gamePk"],
            "player_id": player_id,
            "official_date": split["date"],
            "season": int(split["season"]),
            "player_name": player_name,
            "team": split["team"]["name"],
            "games_started": stat.get("gamesStarted", 0),
            "games_finished": stat.get("gamesFinished", 0),
            "complete_games": stat.get("completeGames", 0),
            "shutouts": stat.get("shutouts", 0),
            "wins": stat.get("wins", 0),
            "losses": stat.get("losses", 0),
            "saves": stat.get("saves", 0),
            "save_opportunities": stat.get("saveOpportunities", 0),
            "holds": stat.get("holds", 0),
            "blown_saves": stat.get("blownSaves", 0),
            "innings_pitched": stat.get("inningsPitched", "0.0"),
            "outs": stat.get("outs", 0),
            "batters_faced": stat.get("battersFaced", 0),
            "number_of_pitches": stat.get("numberOfPitches", 0),
            "balls": stat.get("balls", 0),
            "strikes": stat.get("strikes", 0),
            "runs": stat.get("runs", 0),
            "earned_runs": stat.get("earnedRuns", 0),
            "hits": stat.get("hits", 0),
            "doubles": stat.get("doubles", 0),
            "triples": stat.get("triples", 0),
            "home_runs": stat.get("homeRuns", 0),
            "strike_outs": stat.get("strikeOuts", 0),
            "base_on_balls": stat.get("baseOnBalls", 0),
            "intentional_walks": stat.get("intentionalWalks", 0),
            "hit_batsmen": stat.get("hitBatsmen", 0),
            "balks": stat.get("balks", 0),
            "wild_pitches": stat.get("wildPitches", 0),
            "pickoffs": stat.get("pickoffs", 0),
            "stolen_bases": stat.get("stolenBases", 0),
            "caught_stealing": stat.get("caughtStealing", 0),
            "inherited_runners": stat.get("inheritedRunners", 0),
            "inherited_runners_scored": stat.get("inheritedRunnersScored", 0),
            "sac_bunts": stat.get("sacBunts", 0),
            "sac_flies": stat.get("sacFlies", 0),
            "passed_ball": stat.get("passedBall", 0),
            "catchers_interference": stat.get("catchersInterference", 0),
            "fly_outs": stat.get("flyOuts", 0),
            "ground_outs": stat.get("groundOuts", 0),
            "air_outs": stat.get("airOuts", 0),
            "pop_outs": stat.get("popOuts", 0),
            "line_outs": stat.get("lineOuts", 0),
            "fetched_at": datetime.now().isoformat(),
        })
    return rows

