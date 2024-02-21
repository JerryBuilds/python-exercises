class Hangman:
    def __init__(self):
        self.hidden_word = "apple"
        self.remaining_life = 7
        self.current_guess = "-----"

    def guess_letter(self, letter):
        pass

    def print_turn(self):
        print("Welcome to hangman. You have " + str(self.remaining_life) + " lives left.")
        print("So far, your guess is: " + str(self.current_guess))
        # fill in with more details
 
    def still_alive(self):
        return self.remaining_life > 0

# initialize and make loop

