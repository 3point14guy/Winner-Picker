import random
import os

count = 2

# Command Line program functions
def print_menu():
    answer = ''
    print('\nMenu')
    divider()
    print(' 1. List Names\n 2. Add Names\n 3. Remove Names\n 4. Pick Winner\n 5. Quit\n')
    menu_item_selected()

def menu_item_selected():
    answer = input('Please enter a number: ')
    if answer == '5':
        close_program()
    elif answer == '4':
        pick_winner_screen()
    elif answer == '3':
        remove_name_sub_menu()
    elif answer == '2':
        add_name()
    elif answer == '1':
        list_names()
    else:
        print('\n***{} is invalid.***\n'.format(answer))
        print('Only numbers 1-5 are accepted.')
        check_answer()

def divider():
    print('============================')

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def next_step():
    answer = input('Enter 0 for Menu, 5 to quit: ')
    if answer == '0':
        main()
    elif answer == '5':
        close_program()
    else:
        print('\n***{} is invalid.***\n'.format(answer))
        next_step()

def close_program():
    clear_screen()
    print('\nThank you for using Winner Picker\n')


# File manipulation functions
def read_file(file_name):
    name_list = []
    f = open(file_name, 'r')
    for line in f:
        content = line.strip()
        name_list.append(content)
    f.close()
    return name_list

def write_file(file_name, info_to_update):
    f = open(file_name, 'w')
    for elem in info_to_update:
        f.write(elem + '\n')
    f.close()


# Miscellaneous functions
def ordinal(count):
    ordinal = ''
    if count == 2:
        ordinal = '2nd'
    elif count == 3:
        ordinal = '3rd'
    else:
        ordinal = '{}th'.format(count)
    return ordinal


# Winner Picker functions
def pick_winner(name_list):
    global count
    list_length = len(name_list)
    indx = random.randrange(list_length)
    winner = name_list.pop(indx)
    if count <= 2:
        print('\n{} is the winner!\n'.format(winner))
    else:
        print('{} is {}\n'.format(winner, ordinal(count-1)))
    more_winners(name_list)

def pick_winner_screen():
    clear_screen()
    name_list = read_file('names.txt')
    if len(name_list) <= 1:
        print('Not enough names exist. Enter at least 2 names to pick a winner.')
        print_menu()
    else:
        pick_winner(name_list)

def more_winners(name_list):
    global count
    if len(name_list) > 1:
        answer = input('Would you like to pick a {} place winner? y/n: '.format(ordinal(count)))
        if answer.lower() == 'y':
            count += 1
            winner = pick_winner(name_list)
        elif answer.lower() == 'n':
            print_menu()
        else:
            more_winners(name_list)
    else:
        print('...And {} is the last name in the list.'.format(name_list[0]))
        print_menu()

def get_name(action):
    clear_screen()
    name = ""
    count = 0
    users_list_names = []
    while name.strip().lower() != 'done':
        name = input('Enter a name to {} Winner Picker. Type "done" when finished.\n'.format(action))
        if name.strip().lower() != 'done':
            users_list_names.append(name)
            count += 1
    return users_list_names, count

def file_modification_verification(count, action):
    if count == 0:
        print('No new names {}.'.format(action))
    elif count == 1:
        print('{} name {}.'.format(count, action))
    else:
        print('{} names {}.'.format(count, action))
    print_menu()

def remove_name_sub_menu():
    name_list = read_file('names.txt')
    answer = ''
    clear_screen()
    if len(name_list) < 1:
        print('No names exist. Please enter at least 2 names first.')
        print_menu()
    else:
        answer = input('1. Remove one name\n2. Remove all names: ')
    if answer == '1':
        remove_name(name_list)
    elif answer == '2':
        remove_all()
    else:
        remove_name_sub_menu()

def enter_name_again(condition, name_list):
    answer = input('Would you like to {} another name? y/n: '.format(condition))
    if answer.lower() == 'y':
        remove_name(name_list)
    elif answer.lower() == 'n':
        print_menu()
    else:
        enter_name_again(condition, name_list)

def remove_name(name_list):
    remove_name = input('Enter the name you would like to remove:\n')
    remove_indicator = False
    for name in name_list:
        if remove_name.strip().lower() == name.lower():
            name_list.remove(name)
            write_file('names.txt', name_list)
            print('{} has been removed from the list.\n'.format(remove_name))
            remove_indicator = True
            enter_name_again('remove', name_list)
    if remove_indicator == False:
        print('{} not found in list'.format(remove_name))
        enter_name_again('try', name_list)

def remove_all():
    f = open('names.txt', 'w')
    f.write('')
    f.close()
    print('All names removed\n')
    print_menu()

def add_name():
    names_to_add, count = get_name('add to')
    file_list = read_file('names.txt')
    for name in names_to_add:
        file_list.append(name)
    write_file('names.txt', file_list)
    file_modification_verification(count, 'added')

def list_names():
    clear_screen()
    print('These are all the names:\n')
    name_list = read_file('names.txt')
    for name in name_list:
        print(name)
    print('\n')
    print_menu()


def main():
    clear_screen()
    print('Welcome to Winner Picker!')
    divider()
    print('Randomly choose winners from your custom list of names.\n')
    print_menu()

if __name__ == "__main__":
    main()
