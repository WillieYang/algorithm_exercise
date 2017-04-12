import random

letters_space = 'abcdefghijklmnopqrstuvwxyz '
sentence_list = []
sentence_shoot = 'methinks it is like a weasel'

def iteration(arg):
    if arg == False:
        print("This time is failed, try again")
        string_generate()
    else:
        print("Mokey Sucessful")

def compare(arg):
    if arg == sentence_shoot:
        return iteration(True)
    else:
        iteration(False)

def string_generate():
    sentence_list[:] = []
    for ch in range(27):
        sentence_list.append(random.choice(letters_space))
    sentence_string = ''.join(sentence_list)
    compare(sentence_string)

string_generate()



# first step: generate sentence_string
# second step: compare sentence_string to the sentence_shoot
# thrid step: if True, print the sentence_shoot
#               else return False
# fourh step: iterate the above steps until the sentence_shoot is printed.
# Self Check Challenge did not finish...
