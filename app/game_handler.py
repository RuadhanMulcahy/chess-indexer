from game import Game
from game_start import GameStart
from validate import Validate
from move import Move
from board import Board

class GameHandler:
    def __init__(self):
        self.start = GameStart()
        self.validate = Validate()
        self.game = None
        self.games = []

    def read_board(self, board, time_stamp): 
        board.show()
        if self.start.check(board):
            board.show()
            print(f"GameStart: {str(time_stamp)}")
            if self.game is None:
                self.game = Game(game_start=time_stamp)
            elif self.game is not None and len(self.game.moves) > 0:
                self.validate=None
                self.validate = Validate()
                self.games.append(self.game)
                self.game = Game(game_start=time_stamp)
                self.game.show()

        if self.validate.validate_all(board):
            if self.game.add_move(Move(board, time_stamp, self.start.flipped)) == False:
                self.games.append(self.game)
                base_game_start = self.game.game_start
                base_game_moves = self.game.get_moves_for_next_game()
                self.game = Game(moves=base_game_moves, game_start=base_game_start)

    def time_format(self, timestamp):
        return str(timestamp).split('.')[0]
            
    def show_games(self):
        for index, game in enumerate(self.games):
            print(f"____________________________Game {str(index)} Start: {str(game.game_start)}___________________________")
            game.show()
    
    def get_games(self):
        response = {"games" : dict(), "time_stamps": dict()}

        for index, game in enumerate(self.games):
            response["games"][str(index)] = game.get_pgn()
            response["time_stamps"][str(index)] = game.get_time_stamps()
        
        return response
            