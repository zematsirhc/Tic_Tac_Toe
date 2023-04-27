# Define the board class
class Board:

    n_array = [[0,0,0],[0,0,0],[0,0,0]]
    
    #The board consists of a 3x3 array
    def __init__(self):
        self.example_board = [[1,2,3],[4,5,6],[7,8,9]]
        self.board_array = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

    # How do you know when the game is over? 
    def test_win(self):
        n_array = self.n_array
        win_scenarios = [n_array[0],
                        n_array[1],
                        n_array[2],
                        [n_array[0][0], n_array[1][0], n_array[2][0]],
                        [n_array[0][1], n_array[1][1], n_array[2][1]],
                        [n_array[0][2], n_array[1][2], n_array[2][2]],
                        [n_array[0][0], n_array[1][1], n_array[2][2]],
                        [n_array[0][2], n_array[1][1], n_array[2][0]]]
        for scenario in win_scenarios:
            if sum(scenario) == 3:
                return "X"
            elif sum(scenario) == 15:
                return "Y"
        return False
            
    def show_board(self):
        print("Game Board:   Example Board:")
        print(f"{tic_tac_toe.board_array[0][0]} | {tic_tac_toe.board_array[0][1]} | {tic_tac_toe.board_array[0][2]}      {tic_tac_toe.example_board[0][0]} | {tic_tac_toe.example_board[0][1]} | {tic_tac_toe.example_board[0][2]}")
        print("_________      _________")
        print(f"{tic_tac_toe.board_array[1][0]} | {tic_tac_toe.board_array[1][1]} | {tic_tac_toe.board_array[1][2]}      {tic_tac_toe.example_board[1][0]} | {tic_tac_toe.example_board[1][1]} | {tic_tac_toe.example_board[1][2]}")
        print("_________      _________")
        print(f"{tic_tac_toe.board_array[2][0]} | {tic_tac_toe.board_array[2][1]} | {tic_tac_toe.board_array[2][2]}      {tic_tac_toe.example_board[2][0]} | {tic_tac_toe.example_board[2][1]} | {tic_tac_toe.example_board[2][2]}")
    


# Instantiate the board
tic_tac_toe = Board()

# Create the player class
class Player:
    def __init__(self, name, user_name, number):
        self.name = name
        self.user_name = user_name
        self.number = number

    # This is how a turn will be conducted
    def take_turn(self):
        tic_tac_toe.show_board()
        while True:
            self.move = input(f"Which position (1-9) would you like to play, player {self.user_name}? ")
            if not self.move.isdigit():
                print("Invalid input. Please enter a number between 1 and 9.")
            elif int(self.move) < 1 or int(self.move) > 9:
                print("Invalid input. Please enter a number between 1 and 9.")
            elif tic_tac_toe.board_array[(int(self.move)-1)//3][(int(self.move)-1)%3] != ' ':
                print("This spot is taken, please choose another move.")
            else:
                break

        self.column = (int(self.move) -1) % 3
        self.row = (int(self.move) - 1) // 3
        tic_tac_toe.board_array[self.row][self.column] = self.user_name
        tic_tac_toe.n_array[self.row][self.column] = self.number

        

#instantiate players
player_one = Player("Player One", "X", 1)
player_two = Player("Player Two", "Y", 5)

#Game should stay up until a win scenario is fulfilled
while True:
    player_one.take_turn()
    winner_found = tic_tac_toe.test_win()
    if winner_found:
        print(f"The winner is {winner_found}")
        break
    else:
        pass
    player_two.take_turn()
    winner_found = tic_tac_toe.test_win()
    if winner_found:
        print(f"The winner is {winner_found}")
        break
    else:
        pass
