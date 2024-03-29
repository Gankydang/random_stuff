import re

morse_dict = {
    ' ': '/',
    'a': '.-',
    'b': '-...',
    'c': '-.-.', 
    'd': '-..', 
    'e': '.', 
    'f': '..-.', 
    'g': '--.',
    'h': '....', 
    'i': '..', 
    'j': '.---',
    'k': '-.-',
    'l': '.-..', 
    'm': '--', 
    'n': '-.',
    'o': '---',
    'p': '.--.',
    'q': '--.-',
    'r': '.-.',
    's': '...',
    't': '-',
    'u': '..-',
    'v': '...-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': '--..',
    'one': '.----', '1': '.----',
    'two': '..---', '2': '..---',
    'three': '...--', '3': '...--',
    'four': '....-', '4': '....-',
    'five': '.....', '5': '.....',
    'six': '-....', '6': '-....',
    'seven': '--...', '7': '--...',
    'eight': '---..', '8': '---..',
    'nine': '----.', '9': '----.',
    'zero': '-----', '0': '-----'}

print('--MORSE CODE ENCODER/DECODER--')
mode = ''
while mode not in ('decode', 'encode'):
    mode = input('mode (encode/decode): ')

sequence = input(f'Enter a sequence to {mode}: ').lower().strip()

if mode == 'encode':
    encoded_seq = []
    sequence = re.sub("[.,?!:'\"]", '', sequence)
    for char in sequence:
        encoded_seq.append(morse_dict[char])

    print(' '.join(encoded_seq))


else:
    decoded_seq = []
    flipped_morse_dict = {value: key for key, value in morse_dict.items()}
    sequence = sequence.split()

    for morse_code in sequence:
        decoded_seq.append(flipped_morse_dict[morse_code])

    print(''.join(decoded_seq))


