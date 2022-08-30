from board import Board

class GameStart:
    def __init__(self):
        self.create()
        self.game_start_count = 0
        self.flipped = None
        self.on_game_start = False

    def create(self):
        self.board_normal = Board()
        self.board_flipped = Board()
        self.board_normal.create_game_start(False)
        self.board_flipped.create_game_start(True)

    def check(self, board):
        if board.is_match(self.board_normal, False):
            self.flipped = False
            if self.on_game_start == False:
                self.on_game_start = True
                self.game_start_count += 1
                return True
        elif board.is_match(self.board_flipped, False):
            self.flipped = True
            if self.on_game_start == False:
                self.game_start_count += 1
                self.on_game_start = True
                return True
        else:
            self.on_game_start = False
            return False