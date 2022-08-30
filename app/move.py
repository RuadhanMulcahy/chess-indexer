from piece_id_lookups import id_to_pgn
from misc import num_dif

class Move:
    def __init__(self, board, time_stamp, flipped):
        self.taken_piece = None
        self.pgn = ''
        self.create(board, time_stamp, flipped)

    def create(self, board, time_stamp, flipped):
        self.time_stamp = time_stamp
        self.board = board
        for row in board.squares:
            for square in row:
                if square.highlighted and square.piece_short != '':
                    self.new_square = square
                    self.new_square.set_pgn(flipped)
                    self.color = square.color
                elif square.highlighted and square.piece_short == '':
                    self.prev_square = square
                    self.prev_square.set_pgn(flipped)
        self.set_pgn()

    def is_match(self, move):
        if self.prev_square.compare(move.prev_square) and self.new_square.compare(move.new_square):
            return True
        return False

    def set_pgn(self):
        if self.new_square is not None:
            if self.castle_setter(self.prev_square, self.new_square) is not None:
                self.pgn = str(self.castle_setter(self.prev_square, self.new_square))
                return 
            elif self.taken_piece is None and self.new_square.piece_pgn != 'p':
                self.pgn = str(self.new_square.piece_pgn)
            elif self.taken_piece is not None and self.new_square.piece_pgn == 'p':
                self.pgn = str(f"{self.prev_square.pgn_x}x")
            elif self.taken_piece is not None:
                self.pgn = str(f"{self.new_square.piece_pgn}x")
            self.pgn += str(f"{self.new_square.pgn_x}{self.new_square.pgn_y}")
        else:
            self.pgn = ''

    def castle_setter(self, prev_square, new_square):
        def check_square(square, castle_x, castle_y):
            if square.x == castle_x and square.y == castle_y:
                return True
            return False

        if new_square.piece_pgn == 'K':
            if check_square(prev_square, 3, 0) and check_square(new_square, 1, 0):
                return 'O-O '
            if check_square(prev_square, 3, 0) and check_square(new_square, 5, 0):
                return 'O-O-O '
            if check_square(prev_square, 3, 7) and check_square(new_square, 1, 7):
                return 'O-O '
            if check_square(prev_square, 3, 7) and check_square(new_square, 5, 7):
                return 'O-O-O '

    def show_pgn(self):
        # print(f"{self.pgn} {self.time_stamp}", end='')
        print(self.pgn, end='')

    def show_pgn_time(self):
        print(f"{self.pgn} {self.time_stamp}", end='')