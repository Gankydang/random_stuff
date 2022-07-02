import random

num_of_prisoners = 100
num_of_trials = 1000

def scramble_numbers():
    position_of_scrambled_numbers = {}
    numbers = list(range(1, num_of_prisoners + 1))

    for position in range(1, num_of_prisoners + 1):
        position_of_scrambled_numbers[position] = numbers.pop(random.randint(0, len(numbers) - 1))

    return position_of_scrambled_numbers

def all_prisoners_found_their_number(position_of_scrambled_numbers):

    for prisoner in range(1, num_of_prisoners + 1):

        boxes_opened = 0
        number_in_box = position_of_scrambled_numbers.get(prisoner)

        while (number_in_box != prisoner) and (boxes_opened < (num_of_prisoners / 2) - 1):
            number_in_box = position_of_scrambled_numbers.get(number_in_box)
            boxes_opened += 1

        if number_in_box == prisoner:
            continue
        else:
            return False

    return True

prisoner_win = 0
prisoner_lose = 0

for trial in range(num_of_trials):
    position_of_scrambled_numbers = scramble_numbers()

    if all_prisoners_found_their_number(position_of_scrambled_numbers):
        prisoner_win += 1
    else:
        prisoner_lose += 1

print(f'Number of trials: {num_of_trials}')
print(f'Number of prisoners: {num_of_prisoners}')
print(f'\nNumber of times prisoners won: {prisoner_win}')
print(f'Number of times prisoners lost: {prisoner_lose}')
print(f'\nPrisoner success rate: {round((prisoner_win / num_of_trials) * 100, 3)}%')
