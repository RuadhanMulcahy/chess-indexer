class Validate:
    def __init__(self):
        self.same_position_count = 0
        self.move_is_valid = False
        self.last_board = None

    def validate_all(self, board):
        if self.validate_highlight_squares(board):
            if self.not_anomaly(board):
                return True
        return False

    def not_anomaly(self, board):
        anomaly_threshold = 5
        if self.last_board is None:
            self.last_board = board
        elif board.is_match(self.last_board, True):
            self.same_position_count += 1
            self.last_board = board
        else:
            self.same_position_count = 0
            self.last_board = board

        if self.same_position_count == anomaly_threshold:
            return True
        return False

    def for_new_position(self, board):
        if self.last_board is None and board is not None:
            self.last_board = board
            return True
        if board.is_match(self.last_board, True) == False:
            self.last_board = board
            return True
        self.last_board = board
        return False

    def validate_highlight_squares(self, board):
        highlighted_piece_count = 0
        highlighted_empty_count = 0
        for row in board.squares:
            for square in row:
                if square.highlighted == True and square.piece_short != '':
                    highlighted_piece_count += 1
                elif square.highlighted == True and square.piece_short == '':
                    highlighted_empty_count += 1
                if highlighted_piece_count > 1 or highlighted_empty_count > 1:
                    return False
        if highlighted_empty_count == 1 and highlighted_piece_count == 1:
            return True
        return False

    
