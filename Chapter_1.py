word_list = ['cat', 'dog', 'rabbit']
letter_set = set([])
for a_word in word_list:
    for a_letter in a_word:
        letter_set.add(a_letter)
letter_list = list(letter_set)
print(letter_list)

letter_list = [a_letter for a_word in word_list for a_letter in a_word]
print(list(set(letter_list)))
