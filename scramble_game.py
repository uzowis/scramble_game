import random
import time

print("")
print("🧘‍♂️ WELCOME TO WORD SCRAMBLER \n🧘‍♂️ Happy scrambling 🤓 \nHow to Play: Enter correct word or the scrambled word, \nType 'end' to exit the game, type 'next' to try another word\n")
word_bank = []

words = open("words.txt", 'r')
new_words = words.read()
new_wordz = new_words.split("\n")


# create a list from the file content
for word in new_wordz:
	if len(word) > 5:
		word_bank.append(word)

def start_game():
	# extract a random word from the list
	random_word = random.choice(word_bank)

	# Shuffle the random word
	scrambled_word = "".join(random.sample(random_word, len(random_word)))

	trial_count = 1
	while trial_count < 4:
		# Recieve answer from user
		answer = input(f"Which word is this /{scrambled_word}/ --Hint {random_word[0]}{int((len(random_word)-2)) *'*'}{random_word[-1]} > ")

		if answer == random_word :
			print("🤩🤩 Congrats! You're a Scramble Lord😎 \n\n")
			print("#" * 70)
			start_game()
		elif answer == "end":
			exit()
		elif answer == "next":
			print("#" * 70)
			start_game()
		else:
			print("😌😌 Incorrect! Sorry Mate, don't loose hope, try again💪🏿\n")
		trial_count += 1

	else:
		print(f"Time Up, The Correct word is {random_word}\n\n")
		print("#" * 70)
		start_game()

start_game()