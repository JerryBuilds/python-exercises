class Wordle:
	def __init__(self):
		self.hidden_word = "board"
		self.remaining_life = 5
		self.current_guess = "-----"

	def guess_letter(self, letter):
		pass

	def print_turn(self):
		print("Welcome to Wordle. You have " + str(self.remaining_life) + " guesses left.")
		print("So far, your guess is: " + str(self.current_guess))
		# fill in with more details

	def still_alive(self):
		return self.remaining_life > 0

# initialize and make loop

