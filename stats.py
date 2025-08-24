import sys
def get_book_text(filepath):
        with open(filepath) as f:
                file_value=f.read()
        return file_value
def get_word_count():
        text = get_book_text(sys.argv[1])
        text_list = text.split()
        return f"Found {len(text_list)} total words"
def get_character_count():
	character_dictionary = {}
	text = get_book_text(sys.argv[1])
	text_lower = text.lower()
	for text in text_lower:
		if text not in character_dictionary:
			character_dictionary[text] = 1
		else:
			character_dictionary[text] += 1
	return character_dictionary
def sort_on(items):
	return items["num"]
def character_order():
	character_list = []
	character_count = get_character_count()
	for character in character_count:
		if character.isalpha() == True:
			character_list.append({"char": character , "num" : character_count[character]})
	character_list.sort(reverse=True, key=sort_on)
	return character_list
