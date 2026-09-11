class Player:
    def __init__(self):
        self.name=""
        self.symbol=""
    def choose_name(self):
        while True:
            name=input("enter your name")
            if name.isalpha():
                self.name=name
                break
            else:
                print("only letters")
    def choose_symbol(self):
        while True:
            symbol=input("enter symbol")
            if symbol.isalpha() and len(symbol)==1:
                self.symbol=symbol
                break
            else:
                print("only letters and one character")
class Menu:
    def display_main_menu(self):
        print("welcome")
        print("1. start game")
        print("2. quit the game")
        choice = int(input("choose"))
        while True:
            if choice==1 or choice==2:
                break
            else:
                print("only 1 or 2")
                choice= int(input())
        return choice
    def endgame_menu(self):
        menuText="""
Game over!
1. Restart game
2. end game
        """
        choice = int(input(menuText))
        while True:
            if choice==1 or choice==2:
                break
            else:
                print("only 1 or 2")
                choice = int(input(menuText))
        return choice
class Board:
    def __init__(self):
        self.board=["1","2","3","4","5","6","7","8","9"]
    def display_board(self):
        for i in range(0,9,3):
            print("|".join(self.board[i:i+3]))
            print("-"*6)
    def update_board(self,symbol):
        while True:
            choice=input("enter the number of the block")
            if choice not in self.board or not choice.isdigit():
                print("please choose number from the board")
            else:
                break
        self.board[int(choice) - 1] = symbol
    def reset_board(self):
        self.board=["1","2","3","4","5","6","7","8","9"]
class Game:
    def __init__(self):
        self.board=Board()
        self.players=[Player(),Player()]
        self.menu=Menu()
        self.playerIndex=1
    def start_game(self):
        choice=self.menu.display_main_menu()
        if choice==1:
            self.setup_player()
            self.play_game()
        else:
            self.end_game()
    def setup_player(self):
        for player in self.players:
            player.choose_name()
            player.choose_symbol()
    def play_game(self):
        while True:
            self.board.display_board()
            turn=self.play_turn()
            self.board.update_board(self.players[turn].symbol)
            win=self.check_win_draw()
            if win==1:
                print("")
                print("==================")
                print(f"congratulations {self.players[0].name} wins!!")
                print("==================")
                break
            elif win==2:
                print("")
                print("==================")
                print(f"congratulations {self.players[1].name} wins!!")
                print("==================")
                break
            elif win==0:
                print("")
                print("==================")
                print("sadly :( it is a draw")
                print("==================")
                break
        choice=self.restart_game()
        if choice==1:
            self.start_game()
        else:
            self.end_game()
    def play_turn(self):
        if self.playerIndex==1:
            self.playerIndex=0
        else:
            self.playerIndex=1
        return self.playerIndex
    def check_win_draw(self):
        win=-1
        if self.board.board[0]==self.board.board[1]==self.board.board[2]:
            win=self.playerIndex+1
        elif self.board.board[3]==self.board.board[4]==self.board.board[5]:
            win=self.playerIndex+1
        elif self.board.board[6] == self.board.board[7] == self.board.board[8]:
            win = self.playerIndex + 1
        elif self.board.board[0] == self.board.board[4] == self.board.board[8]:
            win = self.playerIndex + 1
        elif self.board.board[2] == self.board.board[4] == self.board.board[6]:
            win = self.playerIndex + 1
        else:
            bol=0
            for i in self.board.board:
                if i.isdigit():
                    bol=1
                    break
            if bol==0:
                win=0
        return win
    def restart_game(self):
        choice= self.menu.endgame_menu()
        return choice
    def end_game(self):
        print("")
        print("""
        =====================
        Game ends!
        =====================
        """)
game=Game()
game.start_game()