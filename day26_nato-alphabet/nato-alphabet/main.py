# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import logging as l

l.basicConfig(format='[%(asctime)s.%(msecs)03d] %(message)s', level=l.INFO, datefmt='%I:%M:%S')

import pandas

#우선 데이타프레임을 만든다
data = pandas.read_csv("nato_phonetic_alphabet.csv")

#데이타프레임에서 딕셔너리를 만든다
phonetic_dict = {row.letter: row.code for index, row in data.iterrows()}
l.info(phonetic_dict)

#스트링 한 문자씩 딕셔너리에서 찾아 리스트를 생성한다
word = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
l.info(output_list)
