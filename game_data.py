
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

death_scenario = [
    'ARRRRGGGGHHHH... YOU FELL INTO A BOTTOMLESS PIT.',
    'YOU TRIPPED OVER WHAT SEEMED LIKE A DEAD BODY.',
    'OUT OF THE DARKNESS, A R.O.U.S. (RODENT OF UNUSUAL SIZE) ATTACKS YOU',
    'ALL OF A SUDDEN, A LARGE OBJECT FELL FROM ABOVE AND HIT YOU IN THE HEAD.'
]

# Map Data is indexed by Room Number and has stuff within
game_map = {
    1: {
        'name': 'BRIDGE',
        'short_desc': 'YOU ARE ON A BRIDGE',
        'long_desc': 'YOU ARE STANDING ON A LONG, LOW BRIDGE THAT LEADS NORTH TO A CASTLE.',
        'travel': [16, 0, 7, 0, 0, 0, 0],
        'is_lit': True,
        'points': 0
    },
    2: {
        'name': 'GREAT HALL',
        'short_desc': 'YOU ARE IN THE GREAT HALL',
        'long_desc': 'YOU ARE STANDING IN A GREAT HALL, THERE IS MUSIC COMING FROM THE WEST. TO THE EAST, YOU CAN SEE A ROOM WITH WHAT LOOKS LIKE A BEAR INSIDE.',
        'travel': [0, 3, 16, 6, 4, 0, 0],
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
        'long_desc': 'YOU ARE IN THE BELL TOWER ABOVE THE GREAT HALL. SEVERAL ROPES HANG ABOVE AND THERE IS FAINT MUSIC COMING FROM THE WEST.',
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
        'long_desc': 'YOU ARE STANDING ON A LONG, GRAVELY ROAD.',
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
    },
    16: {
        'name': 'CASTLE GATE',
        'short_desc': 'YOU ARE AT THE CASTLE ENTRANCE',
        'long_desc': 'YOU ARE STANDING AT THE CASTLE ENTRANCE, A LARGE STONE ARCHWAY LEADS NORTH INTO THE CASTLE. THE CASTLE IS HUGE!',
        'travel': [2, 0, 1, 17, 19, 0, 0],
        'is_lit': True,
        'points': 0
    },
    17: {
        'name': 'DIRT PATH',
        'short_desc': 'YOU ARE ON A DIRT PATH',
        'long_desc': 'YOU ARE WALKING ALONGSIDE THE TOWERING CASTLE WALL, THE PATH CONTINUES TO THE WEST AND EAST. THE WALL ON ONE SIDE OF YOU AND A MOAT ON THE OTHER.',
        'travel': [0, 16, 0, 18, 0, 0, 0],
        'is_lit': True,
        'points': 0
    },
    18: {
        'name': 'DIRT PATH',
        'short_desc': 'YOU ARE ON A DIRT PATH',
        'long_desc': 'YOU ARE CONTINUING ALONGSIDE THE TOWERING CASTLE WALL, THE PATH CONTINUES TO THE WEST AND EAST. THE WALL ON ONE SIDE OF YOU AND A MOAT ON THE OTHER.',
        'travel': [0, 17, 0, 0, 0, 0, 0],
        'is_lit': True,
        'points': 0
    },
    19: {
        'name': 'PORTCULLIS',
        'short_desc': 'YOU ARE AT THE PORTCULLIS TOP',
        'long_desc': 'YOU HAVE CLIMBED TO THE TOP OF THE PORTCULLIS. FROM HERE, YOU GET A NICE VIEW OF THE BRIDGE AND SPOT A DIRT PATH LEADING WEST ALONG THE CASTLE WALL.',
        'travel': [0, 0, 0, 0, 0, 16, 0],
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
    },
    7: {
        'name': 'PORTCULLIS',
        'short_desc': 'A FORMIDABLE IRON PORTCULLIS',
        'long_desc': 'AN INTIMIDATING AND FORMIDABLE IRON PORTCULLIS, IT IS DOWN AND THE ENTRANCE IS BLOCKED.',
        'defeated_by': [999],
        'points': 15,
        'replaced_by': [8]
    },
    8: {
        'name': 'PORTCULLIS',
        'short_desc': 'THE PORTCULLIS IS UP',
        'long_desc': 'THE IRON PORTCULLIS IS IN THE UP POSITION, YOU MAY TRAVEL THROUGH FREELY.',
        'defeated_by': [0],
        'points': 0,
        'replaced_by': [-1]
    },
    9: {
        'name': 'SIGN',
        'short_desc': 'A SMALL PAINTED SIGN',
        'long_desc': 'A SMALL SIGN IS ATTACHED TO THE CASTLE WALL.',
        'text': 'IT READS \'DO NOT CLIMB WALL - THANK YOU, CASTLE MANAGEMENT\'',
        'defeated_by': [0],
        'points': 0,
        'replaced_by': [-1]
    },
    10: {
        'name': 'SIGN',
        'short_desc': 'A SMALL PAINTED SIGN',
        'long_desc': 'A SMALL SIGN IS MORTARED INTO THE CASTLE WALL.',
        'text': 'IT READS \'QUALITY STONEWORK BY DUNSTAN THE CASTLE-BUILDER, 1353 AD\'',
        'defeated_by': [0],
        'points': 0,
        'replaced_by': [-1]
    },
    11: {
        'name': 'SIGN',
        'short_desc': 'A SMALL METAL SIGN',
        'long_desc': 'A SMALL SIGN IS BOLTED TO A POST.',
        'text': 'IT READS \'CAUTION: DRAINAGE DITCH BELOW\'',
        'defeated_by': [0],
        'points': 0,
        'replaced_by': [-1]
    }
}


obst_placement = [
    # Room, Obstacle, Position, ID
    # (ID makes the obstacle uniquely identifiable, allowing use of more than one and can
    # define a placement between rooms - unlock door between rooms 2 & 6 for example)
    [16, 7, 0, 4],  # Castle Gate: Portcullis, North
    [2, 2, 3, 1],  # Great Hall: Wooden Door, West
    [6, 2, 1, 1],  # Lounge: Wooden Door, East
    [9, 6, 5, 3],  # Ditch: Debris, Down
    [17, 9, 0, 5],  # Path: Sign, North
    [18, 10, 0, 6],  # Path: Sign, North
    [8, 11, 1, 7]  # Road: Sign, East
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
    },
    6: {
        'name': 'BRASS LAMP',
        'short_name': 'LAMP',
        'description': 'A SHINY BRASS LAMP. KEEP THIS IN YOUR INVENTORY TO LIGHT YOUR WAY THROUGH DARK PLACES',
        'useful_on': [999],  # -1 Represents the player? Maybe?
        'reusable': True
    }
}


object_placement = [
    # Room, Object
    [6, 2],  # Lounge, Skeleton Key
    [9, 3],  # Drainage Ditch, Sword
    [14, 1],  # Pipe Maze, Coin
    [19, 6]  # Portcullis, Lamp
]


special_commands = [
    'RING BELL', 'RING THE BELL', 'SLEEP', 'TAKE A NAP', 'LIE DOWN', 'LAY DOWN', 'LIFT PORTCULLIS', 'OPEN PORTCULLIS',
    'READ SIGN', 'USE LAMP', 'LIGHT LAMP', 'LIGHT THE LAMP', 'RUB LAMP', 'RUB THE LAMP'
]
