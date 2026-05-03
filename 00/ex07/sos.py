import sys

NESTED_MORSE = {
    " ": "/ ",
    "A": ".- ",
    "B": "-... ",
    "C": "-.-. ",
    "D": "-.. ",
    "E": ". ",
    "F": "..-. ",
    "G": "--. ",
    "H": ".... ",
    "I": ".. ",
    "J": ".--- ",
    "K": "-.- ",
    "L": ".-.. ",
    "M": "-- ",
    "N": "-. ",
    "O": "--- ",
    "P": ".--. ",
    "Q": "--.- ",
    "R": ".-. ",
    "S": "... ",
    "T": "- ",
    "U": "..- ",
    "V": "...- ",
    "W": ".-- ",
    "X": "-..- ",
    "Y": "-.-- ",
    "Z": "--.. ",
    "0": "----- ",
    "1": ".---- ",
    "2": "..--- ",
    "3": "...-- ",
    "4": "....- ",
    "5": "..... ",
    "6": "-.... ",
    "7": "--... ",
    "8": "---.. ",
    "9": "----. ",
}


def main():
    def __doc__():
        """
        This function takes a string input from the command line, converts it to uppercase, and then translates each character into Morse code using a predefined dictionary. If the input contains any characters that are not in the dictionary, it raises an AssertionError.
        """

    try:
        assert len(sys.argv) == 2
        messgae = sys.argv[1].upper()
        if not all (c in NESTED_MORSE for c in messgae):
            raise AssertionError
        print("".join(NESTED_MORSE[c] for c in messgae))
    except AssertionError:
        print("AssertionError: the arguments are bad")

if __name__ == "__main__":
    main()