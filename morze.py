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


def decodeMorse(morse_code):
    list_of__coded_words = []
    coded_chars = ""
    coded_word = []
    final_result = ""
    # ToDo: Accept dots, dashes and spaces, return human-readable message
    for el in range(len(morse_code)):

        if morse_code[el] != ' ':
            coded_chars += morse_code[el]
        elif morse_code[el] == ' ' and len(morse_code) - el > 2:
            coded_word.append(coded_chars)
            coded_chars = ""
            if len(morse_code) - el > 2:
                if morse_code[el] == ' ' and morse_code[el + 1] == ' ':
                    list_of__coded_words.append(coded_word)
                    coded_word = []
    print(list_of__coded_words)

    for w in list_of__coded_words:

        word = ""
        for el in list_of__coded_words[0]:
            if el in MORSE_CODE_DICT.values():
                word += get_key(el)

    return word


decodeMorse('.... . -.--   .--- ..- -.. .')

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


def decodeMorse(morse_code):
    list_of__coded_words = []
    coded_chars = ""
    coded_word = []
    final_result = ""
    # ToDo: Accept dots, dashes and spaces, return human-readable message
    for el in range(len(morse_code)):

        if morse_code[el] != ' ':
            coded_chars += morse_code[el]
        elif morse_code[el] == ' ' and morse_code[el + 1] != ' ':
            coded_word.append(coded_chars)
            coded_chars = ""
        elif morse_code[el] == ' ' and len(morse_code) - el > 2:
            coded_word.append(coded_chars)
            if len(morse_code) - el > 2:
                if morse_code[el] == ' ' and morse_code[el + 1] == ' ':
                    list_of__coded_words.append(coded_word)
                    coded_word = []
    print(list_of__coded_words)

    for w in list_of__coded_words:

        print("this is w {}".format(w))
        print("this is w[0] {}".format(w[0]))
        word = ""
        for el in list_of__coded_words[0]:
            if el in MORSE_CODE_DICT.values():
                word += get_key(el)

    return word


decodeMorse('.... . -.--   .--- ..- -.. .')