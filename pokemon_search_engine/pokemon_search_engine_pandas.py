from sys import exit
import pandas as pd
import os
from numpy import nan
import matplotlib.pyplot as plt

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

def get_option():
    '''
    Displays options and asks user to choose an option from 0 to 6.
    Returns the chosen option
    '''

    print()
    print('Pokemon Super Search Engine')
    print('1. Display Pokemon with their types and statistics')
    print('2. Display the first Pokemon of the Type of your choice')
    print('3. Display all Pokemons with Total Base stat of your choice')
    print('4. Display all Pokemons with a minimum set of stats')
    print('5. Display all legendary Pokemons of specific Type1 and Type2')
    print('6. Find out the best Type of pokemon')
    print('0. Quit\n')

    option = input('Enter option: ').strip()
    print()
    # ensure option is either 0, 1, 2, 3, 4, 5, or 6
    if option not in '0 1 2 3 4 5 6'.split():
        print('Not implemented yet? Please choose a valid option.\n')
        return get_option()
    option = int(option)
    if option == 0:
        # exit the program
        exit('Thank you for using the Pokemon Super Search Engine!')
    return option

def option_1():
    '''
    Returns the selected number of Pokemons with their types and statistics
    '''

    # get number of pokemons to display
    num_of_pokemons = ''
    len_all_pokemon_info = len(pokemon_df)
    while (not num_of_pokemons.isdigit()) or not (int(num_of_pokemons) > 0 and int(num_of_pokemons) < len_all_pokemon_info):
        num_of_pokemons = input('Enter number of Pokemons to be displayed: ').strip()
        print()
    num_of_pokemons = int(num_of_pokemons)
    
    return pokemon_df.loc[pokemon_df['No'] <= num_of_pokemons]

def option_2():
    '''
    Returns the first Pokemon of a Type of the trainder's choice
    '''

    print(f'Available types: {", ".join(list_of_all_types)}')
    type = input('Enter Type: ').strip().capitalize()
    print()
    
    # if type exists, return the first pokemon of that type
    if not type in list_of_all_types:
        print('No pokemon of this type.')
    else:
        for row in pokemon_df.iterrows():
            if row[1]['Type 1'] == type or row[1]['Type 2'] == type:
                return pokemon_df.loc[[row[1]['No'] - 1]]
  

def option_3():
    '''
    Returns all Pokemons with Total Base stat of the trainer's choice
    '''

    try:
        # get total base stat
        total_base_stat = int(input('Enter Total Base stat: ').strip())
        print()
        to_print = pokemon_df.loc[pokemon_df['Total'] == total_base_stat]

        # if no pokemon with the specified total base stat, raise error
        if to_print.empty:
            raise Exception()
        return to_print
    except:
        print('No pokemon with this Total Base stat.')

def option_4():
    '''
    Returns all Pokemons with a minimum set of stats
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
        highest_stats['Sp. Atk'] = pokemon_df['Sp. Atk'].max()
        highest_stats['Sp. Def'] = pokemon_df['Sp. Def'].max()
        highest_stats['Speed'] = pokemon_df['Speed'].max()

        # check whether the minimum stats entered by the user is greater than the highest possible stats
        if highest_stats['Sp. Atk'] < min_stats['Sp. Atk'] or highest_stats['Sp. Def'] < min_stats['Sp. Def'] or highest_stats['Speed'] < min_stats['Speed']:
            print('No pokmeon has such powerful stats.\n')
        else:
            return pokemon_df.loc[(pokemon_df['Sp. Atk'] >= min_stats['Sp. Atk']) & (pokemon_df['Sp. Def'] >= min_stats['Sp. Def']) & (pokemon_df['Speed'] >= min_stats['Speed'])]

def option_5():
    '''
    Returns all legendary Pokemons of Types of the trainer's choice
    '''

    # get type 1 and type 2
    print(f'Available types: {", ".join(list_of_all_types)}')
    type1 = input('Enter Type 1: ').strip().capitalize()
    type2 = input('Enter Type 2: ').strip().capitalize()
    to_print = pokemon_df.loc[(pokemon_df['Legendary'] == True) & (pokemon_df['Type 1'] == type1) & (pokemon_df['Type 2'] == type2)]

    if to_print.empty:
        print('No such legenary Pokemon')
    else:
        return to_print
    
def option_6():
    '''
    Plots bar chart of the mean Total Stats of each Type of Pokemon
    '''

    # populates the dictionary with - type: mean total stats of all of the pokemon of that type
    type_to_total_mapping = {}
    for t in list_of_all_types:
        type_to_total_mapping[t] = 0
        num_of_pokemon = 0
        for total in pokemon_df.loc[(pokemon_df['Type 1'] == t) | (pokemon_df['Type 2'] == t)]['Total']:
            type_to_total_mapping[t] += total
            num_of_pokemon += 1
        type_to_total_mapping[t] = type_to_total_mapping[t] / num_of_pokemon
    
    reversed_type_to_total_mapping = {round(value): key for key, value in type_to_total_mapping.items()}
    sorted_types = []
    sorted_values = []
    for val in sorted(list(reversed_type_to_total_mapping.keys()), reverse=True):
        sorted_types.append(reversed_type_to_total_mapping[val])
        sorted_values.append(val)     
    
    # plot bar chart
    plt.bar(x=sorted_types, height=sorted_values, color='green')
    plt.title('Mean Total Stats of each Type of Pokemon')
    plt.xlabel('Type of Pokemon')
    plt.ylabel('Mean Total Stats')
    plt.ylim(350)

    # displays the values on top of each bar
    for i in range(len(sorted_types)):
        plt.text(i, sorted_values[i], sorted_values[i], ha='center', color='blue', fontweight='bold')

    print('Expand the graph to full screen.')
    print(f'As we can see, {sorted_types[0]} is the strongest type.')
    print('To continue, close the graph window.')
    plt.show()

def main():

    # read Pokemon.csv into a data frame
    global pokemon_df
    pokemon_df = pd.read_csv(os.path.join(ROOT_DIR, 'Pokemon.csv')).replace(nan, '')

    # get all possible types of pokemon
    global list_of_all_types
    list_of_all_types = []
    for type1 in pokemon_df['Type 1']:
        if type1 != '' and type1 not in list_of_all_types:
            list_of_all_types.append(type1)
    for type2 in pokemon_df['Type 2']:
        if type2 != '' and type2 not in list_of_all_types:
            list_of_all_types.append(type2)

    option = get_option()
    options = {1: option_1, 2: option_2, 3: option_3, 4: option_4, 5: option_5, 6: option_6}
    to_print = options[option]()

    if to_print is not None: # check whether to_print is empty
        print(to_print.to_string(index=False))

    return main()

if __name__ == '__main__':
    main()