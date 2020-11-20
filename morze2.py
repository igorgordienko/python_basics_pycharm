MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}


def get_key(val):
    for key, value in MORSE_CODE_DICT.items():
        if val == value:
            return key
    return "not exist"


def decode_morse(morse_code):

    list_of_words = morse_code.split('   ')
    final_list = []
    print("this is list_of_word: {}".format(list_of_words))

    for word in list_of_words:
        decoded_word = ""

        #   print("This is word: {}".format(word))

        list_of_chars = word.split(' ')

        #  print("This is list of chars: {}".format(list_of_chars))

        for letter in list_of_chars:
            #   print("This is char: {}".format(char))
            #  print("This is decoded: {}".format(get_key(char)))
            decoded_word += get_key(letter)
            print(decoded_word)
        final_list.append(decoded_word)

    print(' '.join(final_list))
    return ' '.join(final_list)


decode_morse('.... . -.--   .--- ..- -.. .')