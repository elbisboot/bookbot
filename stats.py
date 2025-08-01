def get_num_of_words(text):
     num_of_words = 0
     for words in text.split():
          num_of_words += 1
     return num_of_words

def count_characters(text):
    character_count = {}
    for character in text:
        lowercase_char = character.lower()
        if lowercase_char in character_count:
            character_count[lowercase_char] += 1
        else:
            character_count[lowercase_char] = 1
    return character_count
def sorted_list_of_dictionaries(character_count):
     def sort_on(item):
          return item["num"]
     for key in character_count:
          character_count[key] = {"char": key, "num": character_count[key]}
     character_count = list(character_count.values())
     character_count.sort(reverse=True, key=sort_on)
     return character_count
