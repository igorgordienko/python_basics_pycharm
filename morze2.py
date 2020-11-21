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

    for word in list_of_words:
        decoded_word = ""

        list_of_chars = word.split(' ')

        for letter in list_of_chars:
            decoded_word += get_key(letter)
            print(decoded_word)
        final_list.append(decoded_word)

    return ' '.join(final_list)


decode_morse('.... . -.--   .--- ..- -.. .')