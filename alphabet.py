import string


def alphabet_position(text):

    outcome = ""

    lower_text = text.lower()
    alpha_list = list(string.ascii_lowercase)
    for el in lower_text:
        if el in alpha_list:
            outcome += "{} ".format(str(alpha_list.index(el) + 1))

    return outcome[:-1]


print(alphabet_position("The sunset sets at twelve o' clock."))
