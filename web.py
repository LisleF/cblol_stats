from mwrogue.esports_client import EsportsClient
site = EsportsClient("lol")

date = "'2023-01-01 00:00:00'"
player = "Disamis"


site = EsportsClient("lol")
'''
response = site.cargo_client.query(
    tables="ScoreboardGames=SG, ScoreboardPlayers=SP",
    join_on="SG.GameId=SP.GameId",
    fields="SG.DateTime_UTC, SG.Team1, SG.Team2, SG.Winner, SG.Patch, SP.Link, SP.Team, SP.Champion, SP.SummonerSpells, SP.KeystoneMastery, SP.KeystoneRune, SP.Role, SP.GameId, SP.Side",
    where="SP.Name='%s' " % (player)
)'''

response = site.cargo_client.query(
    tables="MatchScheduleGame=MSG, MatchSchedule=MS",
    join_on="MSG.MatchId=MS.MatchId",
    fields="MS.DateTime_UTC, MSG.Team1, MSG.Team2, MSG.Winner, MSG.Patch, MSG.Team1Score, MSG.Team2Score",
    where="MS.CastersPBP=Schaeppi"
)

print(response)