import os

def clear_terminal():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For Linux and macOS
    else:
        os.system('clear')

# Start player class

class Player:

    def __init__(self) -> None:
        self.name = ""
        self.symbol = ""

    def set_name(self):
        while True:
            name = input("Enter your name (letters only): ")
            if name.isalpha():
                break
            print("Invalid name, please use letters only")
        self.name = name

    def set_symbol(self):
        while True:
            symbol = input(f"{self.name}, Enter your symbol (one letter only): ")
            if symbol.isalpha() and len(symbol) == 1:
                break
            print("Invalid symbol, please enter one letter")
        self.symbol = symbol.upper()

# End player class

# Start menu class

class Menu:
    
    def display_main_menu(self):
        print("Welcome to X/O game!")
        print("1. Start game")
        print("2. Quit game")

        choice = input("Enter your choice (1 or 2): ")
        while choice != "1" and choice != "2":
            print("Invalid selection, please enter a correct choice")
            choice = input("Enter your choice (1 or 2): ")
        return choice
    
    def display_endgame_menu(self):
        print("Game over!")
        print("1. Restart game")
        print("2. Quit game")
        
        choice = input("Enter your choice (1 or 2): ")
        while choice != "1" and choice != "2":
            print("Invalid selection, please enter a correct choice")
            choice = input("Enter your choice (1 or 2): ")
        return choice

# End menu class

# Start board class

class Board:
    
    def __init__(self) -> None:
        self.board = [str(i) for i in range(1, 10)]
    
    def display_board(self):
        for i in range(0, len(self.board), 3):
            print("|".join(self.board[i:i+3]))
            if i < 6:
                print("-" * 5)
    
    def update_board(self, symbol, cell):
        if self.board[int(cell)-1].isnumeric: 
            self.board[int(cell)-1] = symbol
            return True
        return False
    
    def reset_board(self):
        self.__init__()

# End board class

# Start game class

class Game:
    
    def __init__(self) -> None:
        self.board = Board()
        self.players = [Player(), Player()]
        self.menu = Menu()
        self.who_wins = Player()
    
    def start_game(self):
        choice = self.menu.display_main_menu()
        if choice == "1":
            self.setup_players()
            self.play_game()
        else:
            self.quit_game()
    
    def setup_players(self):
        for num, player in enumerate(self.players, start=1):
            clear_terminal()
            print(f"Player {num}, Enter your details:")
            player.set_name()
            player.set_symbol()
    
    def play_game(self):
        clear_terminal()

        self.board.display_board()
        self.player_turn()
        clear_terminal()

        self.board.display_board()
        
        if self.check_win():
            print(f"{self.who_wins.name} ({self.who_wins.symbol}) wins!!") # print out who wins
        else:
            print("Draw") # print draw
        
        restart = self.menu.display_endgame_menu()
        if restart == "1":
            self.restart_game()
        else:
            self.quit_game()
    
    def enter_cell(self):
        for i in self.players:
            print("#" * 40)
            print(f"{i.name}'s turn ({i.symbol})")
            
            while True:
                cell = input(f"Choose a cell (1-9): ")
                if cell.isdigit() and len(cell) == 1 and cell != "0":
                    break
                print("Enter a valid cell")

            self.board.update_board(i.symbol, cell)
            if self.check_draw() or self.check_win():
                break
            self.board.display_board()
    
    def player_turn(self):
        while not self.check_win() and not self.check_draw():
            self.enter_cell()
    
    def check_win(self):
        # check horizontally
        for i in range(0, len(self.board.board), 3):
            if self.board.board[i] == self.board.board[i+1] == self.board.board[i+2]:
                if self.board.board[i] == self.players[0].symbol:
                    self.who_wins = self.players[0]
                else:
                    self.who_wins = self.players[1]
                return True
        
        # check vertically
        for i in range(3):
            if self.board.board[i] == self.board.board[i+3] == self.board.board[i+6]:
                if self.board.board[i] == self.players[0].symbol:
                    self.who_wins = self.players[0]
                else:
                    self.who_wins = self.players[1]
                return True
        
        # check diagonally
        # 1st diagonal
        if self.board.board[0] == self.board.board[4] == self.board.board[8]:
            if self.board.board[0] == self.players[0].symbol:
                self.who_wins = self.players[0]
            else:
                self.who_wins = self.players[1]
            return True
        # 2nd diagonal
        if self.board.board[2] == self.board.board[4] == self.board.board[6]:
            if self.board.board[2] == self.players[0].symbol:
                self.who_wins = self.players[0]
            else:
                self.who_wins = self.players[1]
            return True
        
        # otherwise
        return False
    
    def check_draw(self):
        return all(not i.isdigit() for i in self.board.board)
    
    def restart_game(self):
        self.board.reset_board()
        self.play_game()
    
    def quit_game(self):
        print("\nGame Finished")

# End game class

# Start driver code

game = Game()
game.start_game()

# End driver code
