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

team1 = Team("Aberdeen Roughnecks")
team_repository.save(team1)
team2 = Team("Dumfries Hunters")
team_repository.save(team2)
team3 = Team("Clyde Valley Blackhawks")
team_repository.save(team3)
team4 = Team("West Coast Trojans")
team_repository.save(team4)
# above code will create each team and save to the DB

team_repository.select_all()
# above method will display the teams

game1 = Game(team1, team2, "NFC Division 1")
game_repository.save(game1)
game2 = Game(team3, team4, "NFC Division 1")
game_repository.save(game2)
# above will create two games, and enter the four teams into fixtures 

game_repository.select_all()
# above will display the games



# need to do the same for the league and league repository now 
# may need to revisit the league class again.