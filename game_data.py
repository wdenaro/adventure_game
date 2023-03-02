
# This will help translate a directional command into an index in map_data[X]['travel']
travel_directions = {'N': 0, 'E': 1, 'S': 2, 'W': 3, 'U': 4, 'D': 5, 'X': 6}

directions = {
    0: ['N', 'NORTH', 'GO NORTH', 'TO THE NORTH'],
    1: ['E', 'EAST', 'GO EAST', 'TO THE EAST'],
    2: ['S', 'SOUTH', 'GO SOUTH', 'TO THE SOUTH'],
    3: ['W', 'WEST', 'GO WEST', 'TO THE WEST'],
    4: ['U', 'UP', 'GO UP', 'ABOVE YOU', 'CLIMB UP'],
    5: ['D', 'DOWN', 'GO DOWN', 'BELOW YOU', 'CLIMB DOWN']
}

directional_moves = [
    'N', 'E', 'S', 'W', 'U', 'D',
    'NORTH', 'EAST', 'SOUTH', 'WEST', 'UP', 'DOWN',
    'GO NORTH', 'GO EAST', 'GO SOUTH', 'GO WEST', 'GO UP', 'GO DOWN',
    'CLIMB UP', 'CLIMB DOWN'
]

special_commands = [
    'RING BELL', 'RING THE BELL', 'SLEEP', 'TAKE A NAP', 'LIE DOWN', 'LAY DOWN'
]

# Map Data is indexed by Room Number and has stuff within
game_map = {
    1: {
        'name': 'BRIDGE',
        'short_desc': 'YOU ARE ON A BRIDGE',
        'long_desc': 'YOU ARE STANDING ON A LONG BRIDGE THAT LEADS NORTH TO A CASTLE.',
        'travel': [2, 0, 7, 0, 0, 0, 0],
        'is_lit': True,
        'points': 0
    },
    2: {
        'name': 'GREAT HALL',
        'short_desc': 'YOU ARE IN THE GREAT HALL',
        'long_desc': 'YOU ARE STANDING IN A GREAT HALL, THERE IS MUSIC COMING FROM THE WEST. TO THE EAST, YOU CAN SEE A ROOM WITH WHAT LOOKS LIKE A BEAR INSIDE.',
        'travel': [0, 3, 1, 6, 4, 0, 0],
        'is_lit': True,
        'points': 5
    },
    3: {
        'name': 'TROPHY ROOM',
        'short_desc': 'YOU ARE IN THE TROPHY ROOM',
        'long_desc': 'YOU ARE STANDING IN THE TROPHY ROOM, THERE IS 9-FOOT GRIZZLY BEAR STANDING ON IT\'S HIND LEGS LOOKING RIGHT AT YOU. LUCKILY YOU QUICKLY REALIZE IT\'S STUFFED.',
        'travel': [0, 0, 0, 2, 0, 5, 0],
        'is_lit': True,
        'points': 5
    },
    4: {
        'name': 'BELL TOWER',
        'short_desc': 'YOU ARE IN THE BELL TOWER',
        'long_desc': 'YOU ARE IN THE BELL TOWER, ABOVE THE GREAT HALL. THERE IS FAINT MUSIC COMING FROM THE WEST.',
        'travel': [0, 0, 0, 10, 15, 2, 0],
        'is_lit': True,
        'points': 10
    },
    5: {
        'name': 'DUNGEON',
        'short_desc': 'YOU ARE IN THE DUNGEON',
        'long_desc': 'YOU ARE IN A DIMLY LIT DUNGEON. YOU ARE SURROUNDED BY DOZENS OF BROKEN PINBALL MACHINES.',
        'travel': [0, 0, 0, 0, 3, 0, 0],
        'is_lit': True,
        'points': 5
    },
    6: {
        'name': 'LOUNGE',
        'short_desc': 'YOU ARE IN THE GLOBE LOUNGE',
        'long_desc': 'YOU ARE IN A LOUNGE THAT FEATURES A LARGE GOLDEN GLOBE IN THE CENTER. YOU HEAR A SITAR PLAYING.',
        'travel': [0, 2, 0, 0, 10, 0, 0],
        'is_lit': True,
        'points': 5
    },
    7: {
        'name': 'GRAVEL ROAD',
        'short_desc': 'YOU ARE ON A LONG GRAVEL ROAD',
        'long_desc': 'YOU ARE STANDING ALONGSIDE A LONG, GRAVEL ROAD. YOU CAN SEE A CASTLE TO THE NORTH.',
        'travel': [1, 0, 8, 0, 0, 0, 0],
        'is_lit': True,
        'points': 0
    },
    8: {
        'name': 'GRAVELY ROAD',
        'short_desc': 'YOU ARE ON A GRAVELY ROAD',
        'long_desc': 'YOU ARE STANDING ON A LONG, GRAVELY ROAD. THERE IS A DRAINAGE DITCH TO THE EAST.',
        'travel': [7, 9, 0, 0, 0, 9, 0],
        'is_lit': True,
        'points': 0
    },
    9: {
        'name': 'DRAINAGE DITCH',
        'short_desc': 'YOU ARE IN A DRAINAGE DITCH',
        'long_desc': 'YOU HAVE SLID DOWN TO THE BOTTOM OF THE DRAINAGE DITCH, WATER MUST FLOW DOWN AND THROUGH HERE, WHAT A MESS!',
        'travel': [0, 0, 0, 0, 8, 11, 0],
        'is_lit': True,
        'points': 10
    },
    10: {
        'name': 'BELL TOWER',
        'short_desc': 'YOU ARE IN THE WEST END OF THE BELL TOWER',
        'long_desc': 'YOU ARE IN THE BELL TOWER AND CAN SEE THERE IS MORE BELL TOWER TO THE EAST. YOU HEAR MUSIC COMING FROM BELOW.',
        'travel': [0, 4, 0, 0, 0, 6, 0],
        'is_lit': True,
        'points': 5
    },
    11: {
        'name': 'DRAIN PIPE',
        'short_desc': 'YOU ARE IN A RATHER SMALL DRAIN PIPE',
        'long_desc': 'YOU ARE IN A RATHER SMALL DRAIN PIPE, LOOKS LIKE THERE IS A DRAINAGE DITCH TO THE WEST AND VERY DARK PIPE LEADING EAST.',
        'travel': [0, 12, 0, 9, 0, 0, 0],
        'is_lit': True,
        'points': 10
    },
    12: {
        'name': 'DRAINAGE PIPE',
        'short_desc': 'YOU ARE IN A RATHER SMALL DARK DRAINAGE PIPE',
        'long_desc': 'YOU ARE IN A RATHER SMALL DRAINAGE PIPE, OTHER DARK PIPES LEAD OFF IN ALL DIRECTIONS.',
        'travel': [14, 12, 11, 12, 14, 12, 0],
        'is_lit': False,
        'points': 10
    },
    14: {
        'name': 'DRAINAGE PIPE MAZE',
        'short_desc': 'YOU ARE IN A MAZE OF DARK DRAINAGE PIPES',
        'long_desc': 'YOU ARE IN A MAZE OF DARK DRAINAGE PIPES, DIFFICULT TO DETERMINE WHICH WAY IS WHICH.',
        'travel': [14, 12, 14, 12, 14, 12, 0],
        'is_lit': False,
        'points': 15
    },
    15: {
        'name': 'UPPER TOWER',
        'short_desc': 'YOU ARE IN THE UPPER BELL TOWER',
        'long_desc': 'YOU ARE AT THE VERY TOP OF THE BELL TOWER, THERE IS A LARGE BRONZE BELL HOOKED TO A SYSTEM OF ROPES AND PULLEYS.',
        'travel': [0, 0, 0, 0, 0, 4, 0],
        'is_lit': True,
        'points': 10
    }
}


obstacles = {
    1: {
        'name': 'STEEL DOOR',
        'short_desc': 'LOCKED STEEL DOOR',
        'long_desc': 'A HEAVY STEEL DOOR THAT IS BLOCKING YOUR PASSAGE.',
        'defeated_by': [2],  # Object ID that will overcome this obstacle
        'points': 5,
        'replaced_by': [0]  # Obstacle is not replaced, effectively disappears from gameplay
    },
    2: {
        'name': 'WOOD DOOR',
        'short_desc': 'A HEAVY WOODEN DOOR',
        'long_desc': 'A VERY HEAVY WOODEN DOOR THAT APPEARS LOCKED.',
        'defeated_by': [2],
        'points': 0,  # Object is simply present in gameplay, need not be defeated
        'replaced_by': [0]
    },
    3: {
        'name': 'DRAGON',
        'short_desc': 'A LARGE DRAGON',
        'long_desc': 'A FIRE-BREATHING DRAGON, VERY MENACING AND VERY DEADLY.',
        'defeated_by': [3, 4],   # Object IDs that will overcome this obstacle
        'points': 100,
        'replaced_by': [4]  # Obstacle that is swapped in, once obstacle is defeated
    },
    4: {
        'name': 'DEAD DRAGON',
        'short_desc': 'A LARGE DEAD DRAGON',
        'long_desc': 'THE DEAD BODY OF A LARGE DRAGON.',
        'defeated_by': [0],  # Object is simply present in gameplay, need not be defeated
        'points': 0,
        'replaced_by': [(5, 10)]  # Obstacle that is swapped in after second parameter of turns
    },
    5: {
        'name': 'ROTTING CARCASS',
        'short_desc': 'A LARGE ROTTING CARCASS',
        'long_desc': 'HERE LIES THE ROTTING CARCASS OF WHAT APPEARS TO HAVE BEEN A LARGE DRAGON.',
        'defeated_by': [0],
        'points': 0,
        'replaced_by': [-1]  # Indicates it is still in gameplay, and will remain in this state for duration
    },
    6: {
        'name': 'DEBRIS',
        'short_desc': 'LOTS OF DEBRIS',
        'long_desc': 'THE BOTTOM OF THE DRAINAGE DITCH IS LITTERED WITH VARIOUS BITS OF DEBRIS AND DETRITUS.',
        'defeated_by': [0],
        'points': 0,
        'replaced_by': [-1]
    }
}


obst_placement = [
    # Room, Obstacle, Position, ID
    # (ID makes the obstacle uniquely identifiable, allowing use of more than one and can
    # define a placement between rooms - unlock door between rooms 2 & 6 for example)
    [2, 2, 3, 1],  # Great Hall: Wooden Door, West
    [6, 2, 1, 1],  # Lounge: Wooden Door, East
    [9, 6, 5, 3]  # Ditch: Debris, Down
]


objects = {
    1: {
        'name': 'SILVER COIN',
        'short_name': 'COIN',
        'description': 'A SHINY SILVER COIN, ONE SIDE SHOWS THE PROFILE OF A NOBLE RULER, THE OTHER SIDE IS INSCRIBED WITH THE LETTERS XLII',
        'useful_on': [999],  # 999 is an unknown future obstacle
        'reusable': False
    },
    2: {
        'name': 'SKELETON KEY',
        'short_name': 'KEY',
        'description': 'A SKELETON KEY THAT LOOKS AS IF IT COULD OPEN MANY TYPES OF LOCKS (AND IT IS EVEN SHAPED LIKE A SKELETON)',
        'useful_on': [1, 2],
        'reusable': True
    },
    3: {
        'name': 'LONG SWORD',
        'short_name': 'SWORD',
        'description': 'A LONG SWORD FORGED FROM VALYRIAN STEEL AND HAS AN EXCEPTIONALLY KEEN EDGE',
        'useful_on': [3],
        'reusable': True
    },
    4: {
        'name': 'BATTLE AXE',
        'short_name': 'AXE',
        'description': 'A FORMIDABLE BATTLE AXE WITH A DOUBLE EDGED BLADE OF REGULAR STEEL (NOT THAT VALYRIAN STUFF)',
        'useful_on': [3],
        'reusable': True
    },
    5: {
        'name': 'HAM SANDWICH',
        'short_name': 'SANDWICH',
        'description': 'A HAM ON RYE WITH LETTUCE, TOMATO AND A MUSTARD-LIKE SPREAD. LOOKS DELICIOUS',
        'useful_on': [-1],  # -1 Represents the player? Maybe?
        'reusable': False
    }
}


object_placement = [
    # Room, Object
    [6, 2],  # Lounge, Skeleton Key
    [9, 3],  # Drainage Ditch, Sword
    [14, 1]  # Pipe Maze, Coin
]
