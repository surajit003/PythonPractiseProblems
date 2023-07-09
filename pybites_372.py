import string
from collections import Counter


def validate_pangram(sentence: str) -> bool:
    input_data = sentence.lower().strip().replace(" ","")
    alphabet = string.ascii_lowercase
    c_input_data = Counter(input_data)
    a_alphabet = Counter(alphabet)
    return c_input_data.keys() == a_alphabet.keys()

sentence = "The quick brown fox jumps over a lazy dog"
print(validate_pangram(sentence))