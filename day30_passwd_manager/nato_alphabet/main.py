import pandas
import logging as l

l.basicConfig(format='[%(asctime)s.%(msecs)03d] %(message)s', 
              level=l.INFO, 
              datefmt='%I:%M:%S')

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
l.info(phonetic_dict)

def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        l.info("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        l.info(output_list)

generate_phonetic()