from sys import exit
import csv
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
HEADERS = 'No  Name                          Type 1    Type 2    Total  HP     Attack    Defense   Sp. Atk   Sp. Def   Speed     Generation   Legendary'

def read_csv():
    '''
    Reads Pokemon.csv and stores the information in a global variable all_pokemon_info:
    [
        {'No': 1, 'Name': 'Bulbasaur', 'Type 1': 'Grass', 'Type 2': 'Poison', 'Total': 318, 
        'HP': 45, 'Attack': 49, 'Defense': 49, 'Sp. Atk': 65, 'Sp. Def': 65, 'Speed': 45, 
        'Generation': 1, 'Legendary': 'FALSE'}, ....
    ]
    '''

    global all_pokemon_info
    with open(os.path.join(ROOT_DIR, 'Pokemon.csv')) as f:
        # stores information from csv into ls
        csv_reader = csv.reader(f)
        ls = []
        for row in csv_reader:
            row = list(map(lambda x: int(x) if x.isdigit() else x, row))
            ls.append(row) 

        # converts ls into a usable format which is stored in all_pokemon_info
        all_pokemon_info = []
        for i in range(1, len(ls)):
            row = ls[i]
            each_pokemon_info = {}
            start_from = 0

            for stat in row:
                index = row.index(stat, start_from)
                start_from = index + 1
                each_pokemon_info[ls[0][index]] = row[index]
            all_pokemon_info.append(each_pokemon_info)

def get_printable_row(row: dict):
    '''
    Accepts the row as a dictionary and returns the printable string of it
    '''

    row = list(row.values())
    len_of_portion = [4, 30, 10, 10, 7, 7, 10, 10, 10, 10, 10, 13, 9]
    row_to_print = ''
    for stat, length in zip(row, len_of_portion):
        row_to_print += str(stat).ljust(length)
    return row_to_print + '\n'

def get_option():
    '''
    Displays options and asks user to choose an option from 0 to 5.
    Returns the chosen option
    '''

    print()
    print('Pokemon Super Search Engine')
    print('1. Display Pokemon with their types and statistics')
    print('2. Display the first Pokemon of the Type of your choice')
    print('3. Display all Pokemons with Total Base stat of your choice')
    print('4. Display all Pokemons with a minimum set of stats')
    print('5. Display all legendary Pokemons of specific Type1 and Type2')
    print('0. Quit\n')

    option = input('Enter option: ').strip()
    print()
    if option not in '0 1 2 3 4 5'.split():
        print('Not implemented yet? Please choose a valid option.\n')
        return get_option()
    option = int(option)
    if option == 0:
        exit('Thank you for using the Pokemon Super Search Engine!')
    return option

def option_1():
    '''
    Display selected number of Pokemons with their types and statistics
    '''

    # get number of pokemons to display
    num_of_pokemons = ''
    len_all_pokemon_info = len(all_pokemon_info)
    while (not num_of_pokemons.isdigit()) or not (int(num_of_pokemons) > 0 and int(num_of_pokemons) < len_all_pokemon_info):
        num_of_pokemons = input('Enter number of Pokemons to be displayed: ').strip()
        print()
    num_of_pokemons = int(num_of_pokemons)
    
    # display pokemons
    to_print = ''
    for row in all_pokemon_info[: num_of_pokemons]:
        to_print += get_printable_row(row)

    return to_print

def option_2():
    '''
    Display the first Pokemon of a Type of the trainder's choice
    '''

    # get all possible types of pokemon
    list_of_all_types = []
    for row in all_pokemon_info:
        for i in range(1, 3):
            if row[f'Type {i}'] != '' and row[f'Type {i}'] not in list_of_all_types:
                list_of_all_types.append(row[f'Type {i}'])

    print(f'Available types: {", ".join(list_of_all_types)}')
    type = input('Enter Type: ').strip().capitalize()
    print()
    
    # if type exists, print the first pokemon of that type
    pokemon_found = False
    if type in list_of_all_types:
        to_print = ''
        for row in all_pokemon_info:
            for i in range(1, 3):
                if row[f'Type {i}'] == type: 
                    pokemon_found = True
                    to_print += get_printable_row(row)
            if pokemon_found:
                break
        return to_print
    else:
        print('No pokemon of this type.')    

def option_3():
    '''
    Display all Pokemons with Total Base stat of the trainer's choice
    '''

    try:
        total_base_stat = int(input('Enter Total Base stat: ').strip())
        print()
        to_print = ''
        for row in all_pokemon_info:
            if row['Total'] == total_base_stat:
                to_print += get_printable_row(row)

        # if no pokemon with the specified total base stat, raise error
        if to_print == '':
            raise Exception()
        return to_print
    except:
        print('No pokemon with this Total Base stat.')

def option_4():
    '''
    Display all Pokemons with a minimum set of stats
    '''

    # get minimum set of stats from user
    min_stats = {'Sp. Atk': '', 'Sp. Def': '', 'Speed': ''}
    min_stats['Sp. Atk'] = input('Enter min special attack stat: ').strip()
    min_stats['Sp. Def'] = input('Enter min special defense stat: ').strip()
    min_stats['Speed'] = input('Enter min speed stat: ').strip()
    for i in min_stats.values():
        if not i.isdigit():
            print('Enter a number.\n')
            break
    else:
        min_stats = {key: int(value) for key, value in min_stats.items()}

        # get highest possible stats of all pokemon
        highest_stats = {'Sp. Atk': 0, 'Sp. Def': 0, 'Speed': 0}
        for row in all_pokemon_info:
            if row['Sp. Atk'] > highest_stats['Sp. Atk']:
                highest_stats['Sp. Atk'] = row['Sp. Atk']
            if row['Sp. Def'] > highest_stats['Sp. Def']:
                highest_stats['Sp. Def'] = row['Sp. Def']
            if row['Speed'] > highest_stats['Speed']:
                highest_stats['Speed'] = row['Speed']

        to_print = ''
        for row in all_pokemon_info:
            if highest_stats['Sp. Atk'] < min_stats['Sp. Atk'] or highest_stats['Sp. Def'] < min_stats['Sp. Def'] or highest_stats['Speed'] < min_stats['Speed']:
                print('No pokmeon has such powerful stats.\n')
                break
            else:
                if row['Sp. Atk'] >= min_stats['Sp. Atk'] and row['Sp. Def'] >= min_stats['Sp. Def'] and row['Speed'] >= min_stats['Speed']:
                    to_print += get_printable_row(row)
        else:
            return to_print

def option_5():
    '''
    Display all legendary Pokemons of Types of the trainer's choice
    '''

    type1 = input('Enter Type 1: ').strip().capitalize()
    type2 = input('Enter Type 2: ').strip().capitalize()

    to_print = ''
    for row in all_pokemon_info:
        if row['Legendary'] == 'TRUE' and row['Type 1'] == type1 and row['Type 2'] == type2:
            to_print += get_printable_row(row)
    if to_print == '':
        print('No such legendary Pokemon.')
    else:
        return to_print

def main():
    read_csv()
    option = get_option()
    options = {1: option_1, 2: option_2, 3: option_3, 4: option_4, 5: option_5}
    to_print = options[option]()

    if to_print is not None:
        print(HEADERS)
        print(to_print)

    return main()

if __name__ == '__main__':
    main()