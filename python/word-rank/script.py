# coding=utf-8

# input: array with multiple strings
# expected output: rank of the 3 most often repeated words in given set of strings and number of times they occured, case insensitive

import re

to_delete = '~`.,/<>?|\\\'\"[]{}1234567890-=!@#$%^&()_+:;'

sentences = [
    'Taki mamy klimat',
    'Wszędzie dobrze ale w domu najlepiej',
    'Wyskoczył jak Filip z konopii',
    'Gdzie kucharek sześć tam nie ma co jeść',
    'Nie ma to jak w domu',
    'Konduktorze łaskawy zabierz nas do Warszawy',
    'Jeżeli nie zjesz obiadu to nie dostaniesz deseru',
    'Bez pracy nie ma kołaczy',
    'Kto sieje wiatr ten zbiera burzę',
    'Być szybkim jak wiatr',
    'Kopać pod kimś dołki',
    'Gdzie raki zimują',
    'Gdzie pieprz rośnie',
    'Swoją drogą to gdzie rośnie pieprz?',
    'Mam nadzieję, że poradzisz sobie z tym zadaniem bez problemu',
    'Nie powinno sprawić żadnego problemu, bo Google jest dozwolony',
]

sentence = " ".join(sentences)

sentence = sentence.lower()

for char in to_delete:
    sentence = sentence.replace(char, "")

print(sentence)

words_list = sentence.split()

unique_words = list(dict.fromkeys(words_list))

how_many = []
for word in unique_words:
	how_many.append(words_list.count(word))
	
for i in range(3):
	max_val = 0
	max_i = 0
	for j in range(len(how_many)):
		if how_many[j] > max_val:
			max_val = how_many[j]
			max_i = j
	word = unique_words.pop(max_i)
	val = how_many.pop(max_i)
	print(word, " - ", val)

# Example result:
# 1. "mam" - 12
# 2. "tak" - 5
# 3. "z" - 2


# Good luck! You can write all the code in this file.
