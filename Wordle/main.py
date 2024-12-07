import random

# Define class here
class Wordle:
    word_bank = ['Mandi']
    num_wins = 0
    num_losses = 0

    def __init__(self, num_guesses):
        self.num_guesses = num_guesses
        self.word = random.choice(Wordle.word_bank).lower()
        self.guesses = []
        self.guess_count = 0

    def make_guess(self, guess):
        if len(guess) != 5:
            print("Guess must be exactly 5 letters. Try again")
            return False

        if len(set(guess)) != len(guess):
            print("Guess must contain unique letters only. Try again")
            return False

        self.guesses.append(guess)
        self.guess_count += 1

        if guess.lower() == self.word:
            print("You win!")
            Wordle.num_wins += 1
            return True
        elif self.guess_count == self.num_guesses:
            print("You lose!")
            Wordle.num_losses += 1
            return True
        else:
            return False
    
    def __str__(self):
        result = ''
        word_set = set(self.word)
        for each_guess in self.guesses:
            if len(each_guess) == 5:  # Only process valid guesses
                for i in range(len(each_guess)):
                    if each_guess[i].lower() == self.word[i].lower():
                        result += each_guess[i].upper() + '(g) '
                    elif each_guess[i].lower() in word_set:
                        result += each_guess[i].upper() + '(y) '
                    else:
                        result += each_guess[i].upper() + '(r) '
                result += '\n'
        remaining_guesses = self.num_guesses - self.guess_count
        result += f"{remaining_guesses} guesses remaining"
        return result.strip()



# No need to touch code below this line unless you
# would like to play with different settings. It allows
# you to interact with an instance of your class.
def run_program():
    play_again = 'y'
    while play_again == 'y':
        wordle_game = Wordle(6)
        print(wordle_game)
        game_over = False
        while not game_over:
            guess = input('What is your guess? ')
            game_over = wordle_game.make_guess(guess)
            print(wordle_game)
        print("Wins: {}, Losses: {}".format(Wordle.num_wins, Wordle.num_losses))
        print()
        play_again = input("Play again(y/n)? ")
        print()
    print("All done!")

if __name__ == "__main__":
    run_program()

