import pdb
from models.player import Player
from models.match import Match

import repositories.player_repository as player_repository
import repositories.match_repostitory as match_repository

# player1 = match_repository.get_player_details_1(19)
# print(player1)

# player_repository.delete_all()

# player1 = Player('Christopher', 'Mario')
# player_repository.save(player1)

# player2 = Player('Stephen', 'Luigi')
# player_repository.save(player2)

# match1 = Match(player1.id, player2.id)
# match_repository.create_match(match1)

# match2 = Match(player1.id, player2.id)
# match_repository.create_match(match2)

# match_repository.delete_all()
# player_repository.delete(36)

# print(match_repository.select(7))
# match_repository.delete_all()
# player_repository.delete_all()

match_repository.play_match(2, 19)
