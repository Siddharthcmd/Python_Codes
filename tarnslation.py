'''
Represent a small bilingual(English-Swedish) glossary given below as a Python dictionary

{"merry": "god", "christmas": "jul", "and": "och",
    "happy": "gott", "new": "nytt", "year": "ar"}

and use it to translate your Christmas wishes from English into Swedish.

That is , writeapythonfunctiontranslate()thatacceptsthebilingualdictionary and alistof
English words (your Christmas wish) and returns a list of equivalent Swedish words.
'''


def translate(bilingual_dict, english_words_list):
    return [value for key, value in bilingual_dict.items()
            for keyword in english_words_list if (key == keyword)]


bilingual_dict = {"merry": "god", "christmas": "jul",
                  "and": "och", "happy": "gott", "new": "nytt", "year": "ar"}
english_words_list = ["merry", "christmas"]
print("The bilingual dict is:", bilingual_dict)
print("The english words are:", english_words_list)

swedish_words_list = translate(bilingual_dict, english_words_list)
print("The equivalent swedish words are:", swedish_words_list)
