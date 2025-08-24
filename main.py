from stats import get_word_count
from stats import character_order
import sys
def main():
	if len(sys.argv) > 1:
		print("============ BOOKBOT ============")
		print("Analyzing book found at books/frankenstein.txt...")
		print("----------- Word Count ----------")
		print(get_word_count())
		print("--------- Character Count -------")
		for character in character_order():
			print(f"{character["char"]}: {character["num"]}")
	else:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
main()
