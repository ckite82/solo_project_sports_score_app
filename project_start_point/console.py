import pdb 
from models.league import League
from models.game import Game
from models.team import Team

import repositories.league_repository as league_repository
import repositories.game_repository as game_repository
import repositories.team_repository as team_repository

league_repository.delete_all()
game_repository.delete_all()
team_repository.delete_all()
# above methods will empty the DB's before they are populated with below info/methods

team1 = Team("Aberdeen Roughnecks", 8)
team_repository.save(team1)
team2 = Team("Dumfries Hunters", 5)
team_repository.save(team2)
team3 = Team("Clyde Valley Blackhawks", 1)
team_repository.save(team3)
team4 = Team("West Coast Trojans", 2)
team_repository.save(team4)
# above code will create each team and save to the DB

team_repository.select_all()
# above method will display the teams

game1 = Game(team1, team2, "game week 1", "NFC Division 1")
game_repository.save(game1)
game2 = Game(team3, team4, "game week 1", "NFC Division 1")
game_repository.save(game2)

game3 = Game(team1, team3, "game week 2", "NFC Division 1")
game_repository.save(game3)
game4 = Game(team2, team4, "game week 2", "NFC Division 1")
game_repository.save(game4)

game4 = Game(team1, team4, "game week 3", "NFC Division 1")
game_repository.save(game4)
game5 = Game(team3, team2, "game week 3", "NFC Division 1")
game_repository.save(game5)

game6 = Game(team2, team1, "game week 4", "NFC Division 1")
game_repository.save(game6)
game7 = Game(team4, team3, "game week 4", "NFC Division 1")
game_repository.save(game7)

game8 = Game(team3, team1, "game week 5", "NFC Division 1")
game_repository.save(game8)
game9 = Game(team4, team2, "game week 5", "NFC Division 1")
game_repository.save(game9)

game10 = Game(team4, team1, "game week 6", "NFC Division 1")
game_repository.save(game10)
game11 = Game(team2, team3, "game week 6", "NFC Division 1")
game_repository.save(game11)

game12 = Game(team1, team2, "game week 7", "NFC Division 1")
game_repository.save(game12)
game13 = Game(team3, team4, "game week 7", "NFC Division 1")
game_repository.save(game13)

game14 = Game(team1, team3, "game week 8", "NFC Division 1")
game_repository.save(game14)
game15 = Game(team2, team4, "game week 8", "NFC Division 1")
game_repository.save(game15)

game16 = Game(team1, team4, "game week 9", "NFC Division 1")
game_repository.save(game16)
game17 = Game(team3, team2, "game week 9", "NFC Division 1")
game_repository.save(game17)

game17 = Game(team2, team1, "game week 10", "NFC Division 1")
game_repository.save(game17)
game18 = Game(team4, team3, "game week 10", "NFC Division 1")
game_repository.save(game18)

game19 = Game(team3, team1, "game week 11", "NFC Division 1")
game_repository.save(game19)
game20 = Game(team4, team2, "game week 11", "NFC Division 1")
game_repository.save(game20)

game21 = Game(team4, team1, "game week 12", "NFC Division 1")
game_repository.save(game21)
game22 = Game(team2, team3, "game week 12", "NFC Division 1")
game_repository.save(game22)
# above will create games for each team to play each other 4 
# times in the season, and enter the four teams into fixtures 

game_repository.select_all()
# above will display the games

# need to input data for the league to be able to populate it with game_wins