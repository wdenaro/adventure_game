import game_data
import random

current_room = 1
inventory = []
turn_total = 1
score = 50
dark_moves = 0


def get_room_info(room):
    '''
    Pass this function a room number (INT) and you will get back a full DICTIONARY that contains room details along
    with two additional LISTS that describe Obstacles and Objects in the room.

    :param room:
    :return:
    '''

    _room_info = {
        'room_number': room,
        'name': game_data.game_map[room]['name'],
        'short_desc': game_data.game_map[room]['short_desc'],
        'long_desc': game_data.game_map[room]['long_desc'],
        'obstacles': get_obstacles_in_room(room),
        'objects': get_objects_in_room(room)
    }

    return _room_info


def get_obstacles_in_room(room):
    '''
    Pass this function a room number (INT) and you will get back a LIST of dictionaries (0 or more)
    Each describing an Obstacle in the room.

    :param room:
    :return:
    '''

    _obstacles_info = []

    for _o in game_data.obst_placement:
        if _o[0] == room:
            _dict = {
                'obstacle_number': _o[1],
                'direction': _o[2],
                'name': game_data.obstacles[_o[1]]['name'],
                'short_desc': game_data.obstacles[_o[1]]['short_desc'],
                'long_desc': game_data.obstacles[_o[1]]['long_desc']
            }
            _obstacles_info.append(_dict)
    return _obstacles_info


def get_objects_in_room(room):
    '''
    Pass this function a room number (INT) and you will get back a LIST of dictionaries (0 or more)
    Each describing an Object in the room.

    :param room:
    :return:
    '''

    _objects_info = []

    for _o in game_data.object_placement:
        if _o[0] == room:
            _dict = {
                'object_number': _o[1],
                'name': game_data.objects[_o[1]]['name'],
                'description': game_data.objects[_o[1]]['description']
            }
            _objects_info.append(_dict)
    return _objects_info


def display_room_text(room, version):
    '''
    Pass this function a room number (INT) and a version (STR) to Display information to the player.

    :param room:
    :param version:
    :return:
    '''

    _room_info = get_room_info(room)

    if version == 'name':
        _key = 'name'
    elif version == 'short':
        _key = 'short_desc'
    else:
        _key = 'long_desc'

    print('')
    print(_room_info[_key])


def convert_dir_num_to_readable(direction):
    return game_data.directions[direction][3]


def display_room_obstacles(room):
    '''
    Pass this function a room number (INT) to Display information to the player.

    :param room:
    :return:
    '''

    _obstacle_info = get_obstacles_in_room(room)

    for _o in _obstacle_info:
        _dir = convert_dir_num_to_readable(int(_o['direction']))

        if random.choice([True, False]):  # Randomly give short or long description
            print(f"{_dir} IS {_o['short_desc']}")
        else:
            print(f"{_dir} IS {_o['long_desc']}")


def display_room_objects(room):
    '''
    Pass this function a room number (INT) to Display information to the player.

    :param room:
    :return:
    '''

    _objects_info = get_objects_in_room(room)

    for _o in _objects_info:
        print(f"THERE IS A {_o['name']} HERE")


def initiate_move(command):
    '''
    Pass this function a Directional Move (STR) to determine if the player can move or if blocked

    :param command:
    :return:
    '''

    global current_room, score, dark_moves

    _blocked = False

    for key, value in game_data.directions.items():
        if command in value:
            _dir = key
            break

    # test for blocking obstacle in requested direction
    for _obst in game_data.obst_placement:
        if _obst[0] == current_room and _obst[2] == _dir and _blocked is False:
            if game_data.obstacles[_obst[1]]['defeated_by'][0] != 0:
                _blocked = True
                _blocking_obj = game_data.obstacles[_obst[1]]['short_desc']
                _blocked_dir = game_data.directions[_dir][3]
            break

    if _blocked:
        print('')
        print(f'PASSAGE {_blocked_dir} IS BLOCKED BY {_blocking_obj}')
        score -= 10

    else:
        # test for passage to requested direction
        _val = game_data.game_map[current_room]['travel'][_dir]

        if _val == 0:
            print(f'\nTHERE IS NO PASSAGE {game_data.directions[_dir][3]}')
            score -= 5
        else:
            current_room = _val
            score += game_data.game_map[current_room]['points']  # Award points (when applicable)
            game_data.game_map[current_room]['points'] = 0  # Reduce points (awarded only once)

            if game_data.game_map[current_room]['is_lit'] or 6 in inventory:
                dark_moves = 0
                display_room_text(current_room, 'long')
                display_room_obstacles(current_room)
                display_room_objects(current_room)

            else:
                dark_moves += 1
                if dark_moves == 1:
                    print('\nYOU ARE IN COMPLETE DARKNESS. BETTER TO NAVIGATE DARK PLACES WITH A LAMP.')
                elif dark_moves == 2:
                    print('\nIT IS PITCH BLACK. BE CAREFUL, NAVIGATING DARK SPACES CAN BE DEADLY.')
                elif dark_moves == 3:
                    death_scenario('DARK')


def display_inventory(long=False):
    '''
    Pass this function a Directional long (BOOL) to Display information to the player.

    :param long:
    :return:
    '''

    if len(inventory) > 0:
        word = 'ITEM' if len(inventory) == 1 else 'ITEMS'
        print(f'\nINSIDE YOUR BACKPACK YOU FIND THE FOLLOWING {word}:')
        for i in inventory:
            if long:
                item = game_data.objects[i]['description']
            else:
                item = 'A ' + game_data.objects[i]['name']
            print(f'  {item}')

    else:
        print('\nYOU HAVE A BACKPACK, BUT A QUICK INSPECTION REVEALS IT IS EMPTY')


def drop_object(command):
    '''
    Pass this function a Drop Command (STR), ignore the "drop " portion of the command and check for trailing string
    to match Object short name. If the object is identified and the player holds it, transfer it from inventory into
    the room. Display result to the player.

    :param command:
    :return:
    '''

    _object = command[5:]

    drop_success = False

    for key, value in game_data.objects.items():
        if _object == value['short_name'] and key in inventory:
            inventory.remove(key)
            game_data.object_placement.append([current_room, key])
            drop_success = True
            break

    if drop_success:
        print(f'\nYOU HAVE DROPPED THE {_object}')
    else:
        print(f'\nYOU DON\'T SEEM TO HAVE A {_object} TO DROP')


def take_object(command):
    '''
    Pass this function a Take Command (STR), ignore the "take " portion of the command and check for trailing string
    to match Object short name. If the object is identified and the object is in the room, transfer it to inventory from
    the room. Display result to the player.

    :param command:
    :return:
    '''

    _object = command[5:]

    take_success = False

    for _o in game_data.object_placement:
        if _o[0] == current_room and game_data.objects[_o[1]]['short_name'] == _object:
            inventory.append(_o[1])
            game_data.object_placement.remove(_o)
            take_success = True
            break

    if take_success:
        print(f'\nYOU HAVE ADDED THE {_object} TO YOUR INVENTORY')
    else:
        print(f'\nTHERE DOES NOT SEEM TO BE A {_object} HERE TO TAKE')


def display_empty_request():
    print(f'\nSUBMITTING AN EMPTY REQUEST DOES NOTHING BUT COST YOU A TURN.')


def special_commands(command):
    global turn_total

    if command[:4] == 'RING' and command[-4:] == 'BELL':
        if current_room == 15:  # Only works in the Upper Bell Tower
            print('\nYOU STRIKE THE BELL WITH YOUR CLOSED FIST, THE BELL RESPONDS WITH A VERY LOW AND QUIET HUM... AND YOUR HAND THROBS.')
        else:
            print('\nSORRY, THERE IS NO BELL TO RING')

    elif command == 'LIFT PORTCULLIS' or command == 'OPEN PORTCULLIS':
        if current_room == 16:  # Only works at the castle gate
            for _obj in game_data.obst_placement:
                if _obj[0] == 16:
                    if _obj[1] == 7:
                        print('\nYOU APPROACH THE MASSIVE IRON PORTCULLIS AND ATTEMPT TO RAISE IT. THERE IS NO USE, IT IS FAR TOO HEAVY TO LIFT.')
                    else:
                        print('\nTHE PORTCULLIS ALREADY IN THE UP POSITION, A STRONG ADVENTURER CAME BY AND LIFTED IT EARLIER.')
                    break
        else:
            print(f'\nSORRY, THERE IS NO {command[5:]} HERE TO LIFT')

    elif command == 'USE LAMP' or command == 'LIGHT LAMP' or command == 'LIGHT THE LAMP':
        if 6 in inventory:
            print('\nTHE LAMP IS ALREADY LIT AND HANGS ON THE OUTSIDE OF YOUR BACKPACK, SO JUST HAVING IT IN YOUR INVENTORY WILL DO THE TRICK.')
        else:
            print('\nSORRY, YOU DON\'T HAVE A LAMP')

    elif command == 'READ SIGN':
        if current_room == 17:
            sign_text = game_data.obstacles[9]['text']
            print(f'\n{sign_text}')

        elif current_room == 18:
            sign_text = game_data.obstacles[10]['text']
            print(f'\n{sign_text}')

        elif current_room == 8:
            sign_text = game_data.obstacles[11]['text']
            print(f'\n{sign_text}')

        else:
            print('\nTHERE IS NO SIGN TO READ HERE')

    elif command == 'SLEEP' or command == 'TAKE A NAP' or command == 'LIE DOWN' or command == 'LAY DOWN':
        print(f'\nSUDDENLY, FEELING VERY TIRED, YOU LIE DOWN ON THE VERY SPOT YOU WERE STANDING AND FALL FAST ASLEEP.')
        turn_total += 1
        command = input('> ZZZZZZZZZZZZZZZ ')
        turn_total += 1
        print(f'\nZZZZ HRMMMM PFZZZZZZ... HUH, WHA? YOU WAKE UP IN A BIT OF A DAZE.')
        turn_total += 1


def death_scenario(killed_by):

    if killed_by == 'DARK':
        r = random.choice(game_data.death_scenario)
        print(f'\n{r}')
        print('UNFORTUNATELY, YOU HAVE DIED FROM YOUR INJURIES. YOU SHOULD NOT NAVIGATE DARK SPACES WITHOUT A LAMP.')
        print('**TODO**NEED GRACEFUL ENDING/RESTART HERE')
        exit()


def display_room_help_text():
    print('\n---------------------------------')
    print('YOU ARE IN A TEXT ADVENTURE GAME.')
    print('USE SHORT COMMANDS LIKE \'GO NORTH\', \'LOOK\' OR \'CLIMB DOWN\'. MANY COMMANDS CAN BE SHORTENED, LIKE \'NORTH\' OR SIMPLY \'N\'')
    print('\'SHOW INVENTORY\' OR \'INVENTORY\' TO SEE WHAT YOU ARE CARRYING IN YOUR BACKPACK OR \'INVENTORY DETAIL\' TO GET DETAILED DESCRIPTIONS OF EACH ITEM')
    print('TO EXIT THE GAME AND SEE YOUR SCORE, TYPE \'QUIT\'')
    print('------------------------------------------------\n')


def quit_game():
    print('')
    confirm = input('Are you sure you want to QUIT? [y/n]')

    if confirm.upper() == 'Y' or confirm.upper()[0:1] == 'Y':
        print(f'You scored {score} points in {turn_total} turns.')
        quit()
    else:
        display_room_text(current_room, 'long')


def player_input(room=current_room):
    global turn_total, score

    command = input('> What would you like to do? ')
    command = command.upper().strip()

    turn_total += 1

    if command in game_data.directional_moves:
        initiate_move(command)

    elif command == 'LOOK':
        if game_data.game_map[current_room]['is_lit'] or 6 in inventory:
            display_room_text(current_room, 'long')
            display_room_obstacles(current_room)
            display_room_objects(current_room)
            score -= 1
        else:
            print('\nYOU SEE NOTHING, IT IS COMPLETELY DARK. CARRY A LAMP IN YOUR INVENTORY TO FIX THIS PROBLEM.')

    elif command[0:4] == 'DROP':
        drop_object(command)

    elif command[0:4] == 'TAKE':
        take_object(command)

    elif command == 'INV DETAIL' or command == 'INVENTORY DETAIL':
        display_inventory(True)

    elif command == 'INV' or command == 'INVENTORY' or command == 'SHOW INVENTORY':
        display_inventory(False)

    elif command in game_data.special_commands:
        special_commands(command)

    elif command == '':
        display_empty_request()
        score -= 1

    elif command == 'HELP':
        display_room_help_text()

    elif command == 'Q' or command == 'QUIT':
        quit_game()

    else:
        print('\nSORRY, I DO NOT UNDERSTAND YOUR REQUEST')
        display_room_text(current_room, 'short')
        score -= 1


if __name__ == '__main__':

    # Game Start
    display_room_text(current_room, 'long')
    display_room_obstacles(current_room)

    while True:
        player_input()
