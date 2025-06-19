
import copyreg,pickle
class GameState:
	def __init__(self,level=0,lives=4,points=0):
		self.level=level
		self.lives=lives
		self.points=points

def pickle_game_state(game_state):
	kwargs=game_state.__dict__
	return unpickle_game_state,(kwargs,)

def unpickle_game_state(kwargs):
	return GameState(kwargs)

copyreg.pickle(GameState,pickle_game_state)
state=GameState()
state.points+=1000
serialized=pickle.dumps(state)
state_after=pickle.loads(serialized)
print(state_after.__dict__)


