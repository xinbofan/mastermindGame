'''
    CS5001
    Final Project
    Xinbo Fan
'''

from Marble import Marble
from Point import Point
import random
import turtle
import datetime

class Mastermindgame:
    '''
    Attributes:
        curr_guess (list): The current color guess list of the player
        row_num (int): The current round number, indicating the progress of the game
        secret_code (list): The randomly generated secret color code
        name (str): The name of the player
        content (list): A list to store leaderboard records

    Methods:
        get_user_name: Get the player's name by text input
        draw_tables: Use turtle graphics to draw the game interface
        create_base_marbles: Creates base marbles for representing the player's guesses
        create_result_marbles: Create marbles to display the results of each guess
        create_choice_marbles: Creates marbles that the player can choose for guessing
        create_checkbutton: Creates a button for submitting the guess
        create_xbutton: Create a button to clear the current guess
        create_quit: Create a button to quit the game
        create_winner: Display a winner graphic
        create_lose: Display a lose graphic
        show_secret_code: Reveal the secret code at the end of the game if the player loses
        create_leader_error: Display an error message if the leaderboard file can not be found
        leader_error_disappear: Make the leaderboard error message disappear
        create_quitmsg: Display a quit message graphic
        close_screen: Close the turtle window
        create_secret_code: Generate a random secret code
        clear_curr_guess: Clears the current guess and reset the related marbles
        check_bulls_and_cows: Compare the current guess with the secret code
        draw_bulls_and_cows: Draw the result of the comparison on the game board
        check_win_or_lose: Check if the player has won or lost the game
        one_click_guess: Handle a click event on the game screen
        search_leaderboard: Search for the game record file or creates one if it doesn't exist
        write_leaderboard: Update the leaderboard with the current game record
        write_canvas_leader: Display the game records on the canvas
        record_error: Record any error to an error file
        end: End the turtle graphics main loop
    '''
    
    def __init__(self):
        '''
        Constructor -- create a new instance of a mastermind game
        Parameters:
            name -- the player's name
            secret_code -- a list of four colors generated randomly
            row_num -- the round number, also the index of basic marbles to fill in
            curr_guess -- a list of current round's guess
            content -- initial blank list for content of leaderboard record
        '''
        self.name = self.get_user_name()
        self.secret_code = self.create_secret_code()
        self.row_num = 0
        self.curr_guess = []
        self.content = []
    
    def get_user_name(self):
        '''
        Method -- get the player's name using a text input dialog and return it
        Parameters:
            self -- the current object
        Return the name entered by the player (string)
        '''
        self.screen = turtle.Screen()
        self.screen.title("CS5001 MasterMind Code Game")
        self.name = self.screen.textinput("CS5001 MasterMind", "Your name: ")
        return self.name

    def draw_tables(self):
        '''
        Method -- use turtle graphics to draw the interface
        Parameters:
            self -- the current object
        '''
        self.t = turtle.Turtle()
        self.screen = turtle.Screen()
        self.t.speed(0)
        self.t.hideturtle()
        self.t.up()
        self.t.goto(-345, 325)
        self.t.down()
        self.t.pensize(5)
        self.t.seth(0)
        self.t.color('black')
        self.t.forward(400)
        self.t.right(90)
        self.t.forward(500)
        self.t.right(90)
        self.t.forward(400)
        self.t.right(90)
        self.t.forward(500)

        self.t.up()
        self.t.goto(-345, -190)
        self.t.seth(0)
        self.t.down()
        self.t.forward(680)
        self.t.right(90)
        self.t.forward(120)
        self.t.right(90)
        self.t.forward(680)
        self.t.right(90)
        self.t.forward(120)

        self.t.up()
        self.t.goto(85, 325)
        self.t.color('blue')
        self.t.down()
        self.t.seth(0)
        self.t.forward(250)
        self.t.right(90)
        self.t.forward(500)
        self.t.right(90)
        self.t.forward(250)
        self.t.right(90)
        self.t.forward(500)

    def create_base_marbles(self):
        '''
        Method -- create base marbles for the game
        Parameters:
            self -- the current object
        Returns a dictionary of Marble objects representing the guesses
        ''' 
        self.base_marbles = {}
        start_y = 260
        
        for i in range(10):
            start_x = - 290
            for j in range(4):
                self.base_marbles[f'bm_{i}_{j}'] = Marble(Point(start_x + j * 40, start_y), 'white')
                # Then the marble of row 2, column 3 can be called by self.base_marbles['bm_2_3']
                self.base_marbles[f'bm_{i}_{j}'].draw_empty()
            start_y -= 45
            
        return self.base_marbles

    def create_result_marbles(self):
        '''
        Method -- create result marbles for displaying bulls and cows
        Parameters:
            self -- the current object
        Return a dictionary of Marble objects representing the comparison results
        '''
        self.result_marbles = {}
        res_start_y = 280
        
        for i in range(10):
            self.result_marbles[f'rm_{i}_0'] = Marble(Point(-60, res_start_y), 'white', 5)
            self.result_marbles[f'rm_{i}_1'] = Marble(Point(-45, res_start_y), 'white', 5)
            self.result_marbles[f'rm_{i}_2'] = Marble(Point(-60, res_start_y -15), 'white', 5)
            self.result_marbles[f'rm_{i}_3'] = Marble(Point(-45, res_start_y - 15), 'white', 5)
            # Name setting is similar to basic marbles
            self.result_marbles[f'rm_{i}_0'].draw_empty()
            self.result_marbles[f'rm_{i}_1'].draw_empty()
            self.result_marbles[f'rm_{i}_2'].draw_empty()
            self.result_marbles[f'rm_{i}_3'].draw_empty()
            res_start_y -= 45

        return self.result_marbles

    def create_choice_marbles(self):
        '''
        Method -- create and display choice marbles for player selection
        Parameters:
            self -- the current object
        '''
        self.blue_marble = Marble(Point(-250, -265), 'blue')
        self.red_marble = Marble(Point(-210, -265), 'red')
        self.green_marble = Marble(Point(-170, -265), 'green')
        self.yellow_marble = Marble(Point(-130, -265), 'yellow')
        self.purple_marble = Marble(Point(-90, -265), 'purple')
        self.black_marble = Marble(Point(-50, -265), 'black')
        self.blue_marble.draw()
        self.red_marble.draw()
        self.green_marble.draw()
        self.yellow_marble.draw()
        self.purple_marble.draw()
        self.black_marble.draw()

    def create_checkbutton(self):
        '''
        Method -- create a check button for guess submission
        Parameters:
            self -- the current object
        '''
        try:
            self.screen.register_shape('checkbutton.gif')
            self.ckbt_turtle = turtle.Turtle()
            self.ckbt_turtle.up()
            self.ckbt_turtle.hideturtle()
            self.ckbt_turtle.goto(10, -255)
            self.ckbt_turtle.shape('checkbutton.gif')
            self.ckbt_turtle.showturtle()
        except Exception as err:
            self.record_error(err)

    def create_xbutton(self):
        '''
        Method -- create an X button to clear the current guess
        Parameters:
            self -- the current object
        '''
        try:
            self.screen.register_shape('xbutton.gif')
            self.xbt_turtle = turtle.Turtle()
            self.xbt_turtle.up()
            self.xbt_turtle.hideturtle()
            self.xbt_turtle.goto(80, -255)
            self.xbt_turtle.shape('xbutton.gif')
            self.xbt_turtle.showturtle()
        except Exception as err:
            self.record_error(err)

    def create_quit(self):
        '''
        Method -- create a quit button to exit the game
        Parameters:
            self -- the current object
        '''
        try:
            self.screen.register_shape('quit.gif')
            self.quit_turtle = turtle.Turtle()
            self.quit_turtle.up()
            self.quit_turtle.hideturtle()
            self.quit_turtle.goto(230, -250)
            self.quit_turtle.shape('quit.gif')
            self.quit_turtle.showturtle()
        except Exception as err:
            self.record_error(err)

    def create_winner(self):
        '''
        Method -- create winner graphic
        Parameters:
            self -- the current object
        '''
        try:
            self.write_leaderboard()
            self.screen.register_shape('winner.gif')
            self.winner_turtle = turtle.Turtle()
            self.winner_turtle.shape('winner.gif')
            self.screen.ontimer(self.close_screen, 3000)
        except Exception as err:
            self.record_error(err)

    def create_lose(self):
        '''
        Method -- create lose graphic
        Parameters:
            self -- the current object
        '''
        try:
            self.screen.register_shape('lose.gif')
            self.lose_turtle = turtle.Turtle()
            self.lose_turtle.shape('lose.gif')
            self.screen.ontimer(self.show_secret_code, 3000)
        except Exception as err:
            self.record_error(err)

    def show_secret_code(self):
        '''
        Method -- show the secret code at the end of the game if lose
        Parameters:
            self -- the current object
        '''
        string_secret_code = ' '.join(self.secret_code)
        self.screen.textinput('Secret Code was', f'{string_secret_code}')
        self.close_screen()

    def create_leader_error(self):
        '''
        Method -- create a leaderfile not found error graphic
        Parameters:
            self -- the current object
        '''
        try:
            self.screen.register_shape('leaderboard_error.gif')
            self.lberr_turtle = turtle.Turtle()
            self.lberr_turtle.shape('leaderboard_error.gif')
            self.screen.ontimer(self.leader_error_disappear, 3000)
        except Exception as err:
            self.record_error(err)

    def leader_error_disappear(self):
        '''
        Method -- hide the leaderboard error message
        Parameters:
            self -- the current object
        '''
        self.lberr_turtle.hideturtle()
        
    def create_quitmsg(self):
        '''
        Method -- create a quit message graphic
        Parameters:
            self -- the current object
        '''
        try:
            self.screen.register_shape('quitmsg.gif')
            self.quitmsg_turtle = turtle.Turtle()
            self.quitmsg_turtle.shape('quitmsg.gif')
            self.screen.ontimer(self.close_screen, 3000)
        except Exception as err:
            self.record_error(err)

    def close_screen(self):
        '''
        Method -- close the turtle window
        Parameters:
            self -- the current object
        '''
        self.screen.bye()
        
    def create_secret_code(self):
        '''
        Method -- generate a random secret code
        Parameters:
            self -- the current object
        Return a list containing the colors of the secret code
        '''
        colors = ["red", "blue", "green", "yellow", "purple", "black"]
        self.secret_code = []
        
        for i in range(4):
            self.secret_code.append(colors.pop(random.randint(0,len(colors)-1)))

        return self.secret_code

    def clear_curr_guess(self):
        '''
        Method -- clear the current guess and reset the related marbles
        Parameters:
            self -- the current object
        '''
        guess_num = len(self.curr_guess)
        self.curr_guess = []
        for i in range(guess_num):
            self.base_marbles[f'bm_{self.row_num}_{i}'].draw_empty()
            
    def check_bulls_and_cows(self):
        '''
        Method -- Compare the current guess with the secret code
        Parameters:
            self -- the current object
        Returns a list containing the number of bulls and cows
        '''
        self.bulls_and_cows = [0, 0]
        # Index 0 is bull, index 1 is cow
        for color in self.curr_guess:
            if color in self.secret_code:
                if self.curr_guess.index(color) == self.secret_code.index(color):
                    self.bulls_and_cows[0] += 1
                else:
                    self.bulls_and_cows[1] +=1
                    
        return self.bulls_and_cows

    def draw_bulls_and_cows(self):
        '''
        Method -- draw the compare result on the game board
        Parameters:
            self -- the current object
        '''
        result = self.check_bulls_and_cows()
        i = 0
        for j in range(result[0]):
            self.result_marbles[f'rm_{self.row_num}_{i}'].set_color('black')
            self.result_marbles[f'rm_{self.row_num}_{i}'].draw()
            i += 1
        for j in range(result[1]):
            self.result_marbles[f'rm_{self.row_num}_{i}'].set_color('red')
            self.result_marbles[f'rm_{self.row_num}_{i}'].draw()
            i += 1

    def check_win_or_lose(self):
        '''
        Method -- check if the player has won or lost
        Parameters:
            self -- the current object
        '''
        result = self.check_bulls_and_cows()
        if self.row_num < 10: # Total rounds is less than 10
            if result[0] == 4:
                self.create_winner()
        elif self.row_num == 10: # Win at the 10th round
            if result[0] == 4:
                self.create_winner()
            else: # Lose
                self.create_lose()

    def one_click_guess(self, x, y):
        '''
        Method -- handle one click on the game screen
        Parameters:
            self -- the current object
            x -- the x-coordinate of the click
            y -- the y-coordinate of the click
        '''
        if self.blue_marble.clicked_in_region(x, y):
            # All the not in is checking whether this color has been selected
            if 'blue' not in self.curr_guess:
                self.base_marbles[f'bm_{self.row_num}_{len(self.curr_guess)}'].set_color('blue')
                self.base_marbles[f'bm_{self.row_num}_{len(self.curr_guess)}'].draw()
                self.curr_guess.append('blue')
        elif self.red_marble.clicked_in_region(x, y):
            if 'red' not in self.curr_guess:
                self.base_marbles[f'bm_{self.row_num}_{len(self.curr_guess)}'].set_color('red')
                self.base_marbles[f'bm_{self.row_num}_{len(self.curr_guess)}'].draw()
                self.curr_guess.append('red')
        elif self.green_marble.clicked_in_region(x, y):
            if 'green' not in self.curr_guess:
                self.base_marbles[f'bm_{self.row_num}_{len(self.curr_guess)}'].set_color('green')
                self.base_marbles[f'bm_{self.row_num}_{len(self.curr_guess)}'].draw()
                self.curr_guess.append('green')
        elif self.yellow_marble.clicked_in_region(x, y):
            if 'yellow' not in self.curr_guess:
                self.base_marbles[f'bm_{self.row_num}_{len(self.curr_guess)}'].set_color('yellow')
                self.base_marbles[f'bm_{self.row_num}_{len(self.curr_guess)}'].draw()
                self.curr_guess.append('yellow')
        elif self.purple_marble.clicked_in_region(x, y):
            if 'purple' not in self.curr_guess:
                self.base_marbles[f'bm_{self.row_num}_{len(self.curr_guess)}'].set_color('purple')
                self.base_marbles[f'bm_{self.row_num}_{len(self.curr_guess)}'].draw()
                self.curr_guess.append('purple')
        elif self.black_marble.clicked_in_region(x, y):
            if 'black' not in self.curr_guess:
                self.base_marbles[f'bm_{self.row_num}_{len(self.curr_guess)}'].set_color('black')
                self.base_marbles[f'bm_{self.row_num}_{len(self.curr_guess)}'].draw()
                self.curr_guess.append('black')
        elif abs(x - 80) <= 30 and abs(y + 255) <= 30: # click the xbutton
            self.clear_curr_guess()
        elif abs(x - 230) <= 50 and abs (y + 250)<= 30: # click the quit button
            self.create_quitmsg()
        elif abs(x - 10) <= 30 and abs(y + 255) <= 30 and len(self.curr_guess) == 4: # click the checkbutton
            self.draw_bulls_and_cows()
            self.row_num += 1
            self.check_win_or_lose()
            self.curr_guess = []
            
    def search_leaderboard(self):
        '''
        Method -- search the game record file, if can't find the file, create one
        Parameters:
             self -- the current object
        '''
        try:
            with open('leaderboard.txt','r') as infile: # Found
                self.content = infile.readlines()
        except FileNotFoundError:
            with open('leaderboard.txt','w+') as infile: # Not found, then create
                infile.write('')
                self.content = infile.readlines()
        except Exception as err:
            self.record_error(err)
            
    def write_leaderboard(self):
        '''
        Method -- update record to the leaderboard file
        Parameters:
            self -- the current object
        '''
        try:
            with open('leaderboard.txt','w') as outfile:
                if len(self.content) == 0: # Just created by the search_leaderboard
                    outfile.write('Leaders:\n')
                    outfile.write(f'{self.row_num} : {self.name}')
                elif len(self.content) == 2: # There was one record
                    previous_user = self.content[1].split()
                    outfile.write('Leaders:\n')
                    if self.row_num <= int(previous_user[0]):
                        outfile.write(f'{self.row_num} : {self.name}\n')
                        outfile.write(f'{previous_user[0]} : {previous_user[2]}')
                    else:
                        outfile.write(f'{previous_user[0]} : {previous_user[2]}')
                        outfile.write(f'{self.row_num} : {self.name}\n')
                elif len(self.content) == 3: # Two records
                    pre_user_1 = self.content[1].split()
                    pre_user_2 = self.content[2].split()
                    cur_user = [f'{self.row_num}',' : ', f'{self.name}']
                    all_players = [pre_user_1, pre_user_2, cur_user]
                    all_players.sort()
                    outfile.write('Leaders:\n')
                    outfile.write(f'{all_players[0][0]} : {all_players[0][2]}\n')
                    outfile.write(f'{all_players[1][0]} : {all_players[1][2]}')
        except Exception as err:
            self.record_error(err)

    def write_canvas_leader(self):
        '''
        Method -- display the game records on the game canvas using turtle graphics
        Parameters:
            self -- the current object
        '''
        try:
            with open('leaderboard.txt', 'r') as file:
                writer_turtle = turtle.Turtle()
                writer_turtle.hideturtle()
                writer_turtle.up()
                start_x = 120
                start_y = 260
                writer_turtle.color('blue')
                for line in file:
                    writer_turtle.goto(start_x, start_y)
                    writer_turtle.write(line.strip(), font = ("Arial", 20, "normal"))
                    start_y -= 30
        except FileNotFoundError:
            self.create_leader_error()
        except Exception as err:
            self.record_error(err)

    def record_error(self, err):
        '''
        Method -- record an error message to an error file
        Parameters:
            self -- the current object
            err -- the error to be recorded
        '''
        with open("mastermind_errors.err", "a") as outfile:
            error_record = f"{datetime.datetime.now()}: {type(err).__name__}, {err}\n"
            outfile.write(error_record)

    def end(self):
        '''
        Method -- ends the turtle graphics main loop
        Parameters:
            self -- the current object
        '''
        self.screen.mainloop()
                    
def main():
    screen = turtle.Screen()
    
    game = Mastermindgame()
    game.draw_tables()
    game.create_base_marbles()
    game.create_result_marbles()
    game.create_choice_marbles()
    game.create_checkbutton()
    game.create_xbutton()
    game.create_quit()
    game.search_leaderboard()
    game.write_canvas_leader()
    
    screen.onscreenclick(game.one_click_guess)

    game.end()

if __name__ == "__main__":
    main()
