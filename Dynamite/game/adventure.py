input_name = input ('What is your name? ')
print (f'Hi {input_name}, do you want to play a game?')
input_start = input ('y/n : ')
if input_start == 'y':
    print (f'We are going to go on an adventure!')
    print (f'Which path would you like to take today?')
    print (f'To go to the woods press A')
    print (f'To go to the haunted house press B')
    game_choice = 'z'
    while game_choice != 'A' or 'B':
        game_choice = input ('Choose you path... or type quit to exit ')
        if game_choice == 'A':
            print (f'It was a cold and misty night as we set off into the woods')
        if game_choice == 'B':
            print (f'The door creaked loudly as we pushe dit open')
        if game_choice == 'quit':
            quit()
        else:
            print (f'Try again')
else: 
    quit()

