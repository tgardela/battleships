    
class ValidShip(object):
        
    def __init__(self, board, size, start_point, orientation):
        self.board = board
        self.size = size
        self.start_point = start_point
        self.orientation = orientation
        self.start_row = self.start_point[0]
        self.start_col = self.start_point[1]
        self.end_row = self.start_row + self.size - 1
        self.col = self.start_col
        self.end_col = self.start_col + self.size - 1
        self.row = self.start_row

    
    def check_if_ship_can_be_put_there(self):
        to_return = True
        if self.orientation == 'vertical':
            to_return =  self.vertical_check()
            print(to_return)
        elif self.orientation == 'horizontal':
            to_return = self.horizontal_check()
            print(to_return)
        return to_return
        
        
    def vertical_check(self):
        if self.col == 1:
            return self.vertical_check_first_column()
        elif self.col == 10:
            return self.vertical_check_last_column()
        else:
            return self.vertical_check_middle_columns()


    def vertical_check_first_column(self):
        if self.start_row == 1:
            return self.vertical_check_left_top_corner()
        elif self.end_row == 10:
            return self.vertical_check_left_bottom_corner()
        else:
            return self.vertical_check_left_boundary()
            
    def vertical_check_last_column(self):
        if self.start_row == 1:
            return self.vertical_check_right_top_corner()
        elif self.end_row == 10:
            return self.vertical_check_right_bottom_corner()
        else:
            return self.vertical_check_right_boundary()
            
    def vertical_check_middle_columns(self):
        if self.start_row == 1:
            return self.vertical_check_top_boundary()
        elif self.end_row == 10:
            return self.vertical_check_bottom_boundary()
        else:
            return self.vertical_check_away_from_boundaries()
            
    def vertical_check_left_top_corner(self):
        for i in range(self.size + 1):
            if self.board[self.start_row + i][self.col] != '*' or self.board[self.start_row + i][self.col + 1] != '*':
                return False
        return True
                
    def vertical_check_left_bottom_corner(self):
        for i in range(self.size + 1):
            if self.board[self.end_row - i][self.col] != '*' or self.board[self.end_row - i][self.col + 1] != '*':
                return False
        return True
        
    def vertical_check_left_boundary(self):
        for i in range(-1, self.size + 1):
            if self.board[self.start_row + i][self.col] != '*' or self.board[self.start_row + i][self.col + 1] != '*':
                return False
        return True
        
    def vertical_check_right_top_corner(self):
        for i in range(self.size + 1):
            if self.board[self.start_row + i][self.col] != '*' or self.board[self.start_row + i][self.col - 1] != '*':
                return False
        return True
        
    def vertical_check_right_bottom_corner(self):
        for i in range(self.size + 1):
            if self.board[self.end_row - i][self.col] != '*' or self.board[self.end_row - i][self.col - 1] != '*':
                return False
        return True
        
    def vertical_check_right_boundary(self):
        for i in range(-1, self.size + 1):
            if self.board[self.start_row + i][self.col - 1] != '*' or self.board[self.start_row + i][self.col] != '*':
                return False
        return True
        
    def vertical_check_top_boundary(self):
        for i in range(self.size + 1):
            if self.board[self.start_row + i][self.col - 1] != '*' or self.board[self.start_row + i][self.col] != '*' or self.board[self.start_row + i][self.col + 1] != '*':
                return False
        return True
        
    def vertical_check_bottom_boundary(self):
        for i in range(self.size + 1):
            if self.board[self.end_row - i][self.col - 1] != '*' or self.board[self.end_row - i][self.col] != '*' or self.board[self.end_row - i][self.col + 1] != '*':
                return False
        return True
        
    def vertical_check_away_from_boundaries(self):
        for i in range(-1, self.size + 1):
            if self.board[self.start_row + i][self.col - 1] != '*' or self.board[self.start_row + i][self.col] != '*' or self.board[self.start_row + i][self.col + 1] != '*':
                return False
        if self.board[self.start_row - 1][self.col] != '*' or self.board[self.start_row + self.size][self.col] != '*':
            return False
        return True
    
        
            
    def horizontal_check(self):
        if self.row == 1:
            return self.horizontal_check_first_row()
        elif self.row == 10:
            return self.horizontal_check_last_row()
        else:
            return self.horizontal_check_middle_rows()

    def horizontal_check_first_row(self):
        if self.start_col == 1:
            return self.horizontal_check_left_top_corner()
        elif self.end_col == 10:
            return self.horizontal_check_right_top_corner()
        else:
            return self.horizontal_check_top_boundary()

    def horizontal_check_last_row(self):
        if self.start_col == 1:
            return self.horizontal_check_left_bottom_corner()
        elif self.end_col == 10:
            return self.horizontal_check_right_bottom_corner()
        else:
            return self.horizontal_check_bottom_boundary()

    def horizontal_check_middle_rows(self):
        if self.start_col == 1:
            return self.horizontal_check_left_boundary()
        elif self.end_col == 10:
            return self.horizontal_check_right_boundary()
        else:
            return self.horizontal_check_away_from_boundaries()

    def horizontal_check_left_top_corner(self):
        for i in range(self.size + 1):
            if self.board[self.row][self.start_col + i] != '*' or self.board[self.row + 1][self.start_col + 1] != '*':
                return False
        return True

    def horizontal_check_right_top_corner(self):
        for i in range(self.size + 1):
            if self.board[self.row][self.end_col - i] != '*' or self.board[self.row + 1][self.end_col - i] != '*':
                return False
        return True

    def horizontal_check_top_boundary(self):
        for i in range(-1, self.size + 1):
            if self.board[self.row][self.start_col + i] != '*' or self.board[self.row + 1][self.start_col + i] != '*':
                return False
        return True

    def horizontal_check_left_bottom_corner(self):
        for i in range(self.size + 1):
            if self.board[self.row][self.start_col + i] != '*' or self.board[self.row - 1][self.start_col + i] != '*':
                return False
        return True

    def horizontal_check_right_bottom_corner(self):
        for i in range(self.size + 1):
            if self.board[self.row][self.end_col - i] != '*' or self.board[self.row - 1][self.end_col - i] != '*':
                return False
        return True

    def horizontal_check_bottom_boundary(self):
        for i in range(-1, self.size + 1):
            if self.board[self.row - 1][self.start_col + i] != '*' or self.board[self.row][self.start_col + i] != '*':
                return False
        return True

    def horizontal_check_left_boundary(self):
        for i in range(self.size + 1):
            if self.board[self.row - 1][self.start_col + i] != '*' or self.board[self.row][self.start_col + i] != '*' or \
                        self.board[self.row + 1][self.start_col + i] != '*':
                return False
        return True

    def horizontal_check_right_boundary(self):
        for i in range(self.size + 1):
            if self.board[self.row - 1][self.end_col - i] != '*' or self.board[self.row][self.end_col - i] != '*' or \
                            self.board[self.row + 1][self.end_col - i] != '*':
                return False
        return True

    def horizontal_check_away_from_boundaries(self):
        for i in range(-1, self.size + 1):
            if self.board[self.row - 1][self.start_col + i] != '*' or self.board[self.row][self.start_col + i] != '*' or \
                            self.board[self.row + 1][self.start_col + i] != '*':
                return False
        if self.board[self.row][self.start_col - 1] != '*' or self.board[self.row][self.start_col + self.size] != '*':
            return False
        return True