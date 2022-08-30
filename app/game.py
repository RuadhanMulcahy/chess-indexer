import copy
import enum

class Game:
    def __init__(self, moves = None, game_start=None):
        if moves:
            self.moves = moves
        else:
            self.moves = []
        if game_start:
            self.game_start = game_start
        else:
            self.game_start = game_start
        self.reverse_moves = []
        self.overflow_move = None

    """
    Method for adding move to game
    """
    def add_move(self, move):
        move.taken_piece = self._set_taken_piece(move)
        if self._is_new_move(move):
            if self._is_reverse_move(move):
                print("Reverse Move")
                move.show_pgn_time()
                print()
                reverse_move = self.moves[-1]
                self.reverse_moves.insert(0, reverse_move)
                self.moves.pop()
            elif self._is_catch_up_move(move):
                print("Catch Up")
                move.show_pgn_time()
                print()
                self.moves.append(move)
                self.reverse_moves.pop()   
            elif self._is_catch_up_move(move) == False and len(self.reverse_moves) >= 1:
                print("Game End")
                move.show_pgn_time()
                print()
                self.overflow_move = move
                return False
            else:
                move.show_pgn_time()
                print()
                self.moves.append(move)

        # self.show()
        # input()

    def _set_taken_piece(self, curr_move):
        if len(self.moves) >= 1:
            prev_move = self.moves[-1] 
            taken_piece = prev_move.board.squares[curr_move.new_square.y][curr_move.new_square.x].piece_pgn
            if taken_piece == '':
                return None
            return taken_piece
        return None

    """
    Method for checking if move is a reverse move
    """
    def _is_reverse_move(self, curr_move):
        if len(self.moves) == 0:
            return False
        prev_move = self.moves[-1]
        if curr_move.board.squares[prev_move.prev_square.y][prev_move.prev_square.x].piece_short == prev_move.new_square.piece_short:
            # print("Reverse Move Below")
            # prev_move.board.show()
            # curr_move.board.show()
            return True
        return False
    
    """
    Method for checking if move is a catch up move
    """
    def _is_catch_up_move(self, curr_move):
        if len(self.reverse_moves) == 0:
            return False

        if curr_move.is_match(self.reverse_moves[-1]):
            return True
        else:
            return False

    """
    Method for checking if move is different from previous move
    """
    def _is_new_move(self, move):
        if len(self.moves) < 1:
            return True
        if move.is_match(self.moves[-1]) == False:
            return True
        return False

    """
    Method that returns all moves in game
    """
    def get_game(self):
        return list(self.moves + self.reverse_moves)

    def get_pgn(self):
        moves = self.get_game()
        pgn = ''
        for index, move in enumerate(moves[:-1]):
            pgn += (f"{index+1}. {move.pgn} ")
        pgn += (f"{index+2}. {moves[-1].pgn}")
        return pgn

    def get_time_stamps(self):
        moves = self.get_game()
        time_stamps = ''

        for index, move in enumerate(moves[:-1]):
            time_stamps += f"{index+1}. {str(move.time_stamp)} "
        time_stamps += f"{index+2}. {str(moves[-1].time_stamp)}"
        return time_stamps

    """
    Method that returns moves for next game
    """
    def get_moves_for_next_game(self):
        if self.overflow_move is None:
            return list(self.moves)
        return list(self.moves + [self.overflow_move])

    """
    Method for displaying all moves in game
    """
    def show(self):
        moves = self.get_game()
        for index, move in enumerate(moves):
            print(f" {str(index + 1)}. ", end='')
            move.show_pgn()
        print("")


        
    