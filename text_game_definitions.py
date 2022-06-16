from enum import Enum, auto

'''
'''
class Game:


    '''
    '''
    def moveCharacter(self, p_command) -> bool:
        if p_command == Commands.WALK_FORWARD:
            if self.playerCharacter.currentLocation.front == LocationType.NOTHING:
                return False

            else:
                self.playerCharacter.currentLocation = self.findLocation(self.playerCharacter.currentLocation.front)
                return True
                
        elif p_command == Commands.WALK_BACKWARD:
            if self.playerCharacter.currentLocation.back == LocationType.NOTHING:
                return False

            else:
                self.playerCharacter.currentLocation = self.findLocation(self.playerCharacter.currentLocation.back)
                return True

        elif p_command == Commands.WALK_LEFT:
            if self.playerCharacter.currentLocation.left == LocationType.NOTHING:
                return False

            else:
                self.playerCharacter.currentLocation = self.findLocation(self.playerCharacter.currentLocation.left)
                return True

        elif p_command == Commands.WALK_RIGHT:
            if self.playerCharacter.currentLocation.right == LocationType.NOTHING:
                return False

            else:
                self.playerCharacter.currentLocation = self.findLocation(self.playerCharacter.currentLocation.right)
                return True

        elif p_command == Commands.STAY_HERE:
            return False

    '''
    '''
    def findLocation(self, p_locationType):
        for location in self.listOfLocations:
            if location.locationType == p_locationType:
                return location
        return None
        

    '''
    '''
    def __init__(self):

        self.playerCharacter = None
        self.listOfLocations = [Location(LocationType.BLACKSMITH), 
                                Location(LocationType.CASTLE),
                                Location(LocationType.CAVE),
                                Location(LocationType.DUNGEON),
                                Location(LocationType.ENCHANTED_FOREST),
                                Location(LocationType.FARM),
                                Location(LocationType.HOUSE),
                                Location(LocationType.LIBRARY),
                                Location(LocationType.MINE),
                                Location(LocationType.PUB),
                                Location(LocationType.STABLES),
                                Location(LocationType.THRONE_ROOM),
                                Location(LocationType.TOWN),
                                Location(LocationType.WITCHES_HUT)]

        
        self.listOfCommands = []


    '''
    '''
    def setCharacter(self, p_character):
        self.playerCharacter = p_character
        self.playerCharacter.currentLocation = self.findLocation(LocationType.HOUSE)



'''
'''
class CharacterType(Enum):
    HUNGRY_HANNAH = 'Hungry Hannah'
    NIFTY_NICHOLAS = 'Nifty Nicholas'


'''
'''
class Character:

    '''
    '''
    def __init__(self, p_characterType):
        self.characterType = p_characterType
        self.characterName = p_characterType.value
        self.currentLocation = Location(LocationType.HOUSE)
        

'''
'''
class LocationType(Enum):

    BLACKSMITH = 'Blacksmith'
    TOWN = 'Town'
    PUB = 'Pub'
    LIBRARY = 'Library'
    STABLES = 'Stables'
    FARM = 'Farm'
    ENCHANTED_FOREST = 'Enchanted Forest'
    WITCHES_HUT = 'Witches Hut'
    CASTLE = 'Castle'
    DUNGEON = 'Dungeon'
    THRONE_ROOM = 'Throne Room'
    CAVE = 'Cave'
    MINE = 'Mine'
    HOUSE = 'House'
    NOTHING = 'Nothing'

'''
'''
class Location:

    def setNeighborLocations(self):
        if self.locationType == LocationType.HOUSE:
            self.front = LocationType.ENCHANTED_FOREST
            self.back = LocationType.NOTHING
            self.left = LocationType.STABLES
            self.right = LocationType.NOTHING
        
        elif self.locationType == LocationType.STABLES:
            self.front = LocationType.FARM
            self.back = LocationType.NOTHING
            self.left = LocationType.NOTHING
            self.right = LocationType.HOUSE

        elif self.locationType == LocationType.FARM:
            self.front = LocationType.NOTHING
            self.back = LocationType.STABLES
            self.left = LocationType.NOTHING
            self.right = LocationType.NOTHING
        
        elif self.locationType == LocationType.ENCHANTED_FOREST:
            self.front = LocationType.CASTLE
            self.back = LocationType.HOUSE
            self.left = LocationType.WITCHES_HUT
            self.right = LocationType.TOWN

        elif self.locationType == LocationType.WITCHES_HUT:
            self.front = LocationType.CAVE
            self.back = LocationType.NOTHING
            self.left = LocationType.NOTHING
            self.right = LocationType.ENCHANTED_FOREST

        elif self.locationType == LocationType.TOWN:
            self.front = LocationType.LIBRARY
            self.back = LocationType.BLACKSMITH
            self.left = LocationType.ENCHANTED_FOREST
            self.right = LocationType.PUB

        elif self.locationType == LocationType.BLACKSMITH:
            self.front = LocationType.TOWN
            self.back = LocationType.NOTHING
            self.left = LocationType.NOTHING
            self.right = LocationType.NOTHING

        elif self.locationType == LocationType.PUB:
            self.front = LocationType.NOTHING
            self.back = LocationType.NOTHING
            self.left = LocationType.TOWN
            self.right = LocationType.NOTHING

        elif self.locationType == LocationType.LIBRARY:
            self.front = LocationType.NOTHING
            self.back = LocationType.TOWN
            self.left = LocationType.CASTLE
            self.right = LocationType.NOTHING

        elif self.locationType == LocationType.CASTLE:
            self.front = LocationType.THRONE_ROOM
            self.back = LocationType.ENCHANTED_FOREST
            self.left = LocationType.DUNGEON
            self.right = LocationType.LIBRARY

        elif self.locationType == LocationType.THRONE_ROOM:
            self.front = LocationType.NOTHING
            self.back = LocationType.CASTLE
            self.left = LocationType.NOTHING
            self.right = LocationType.NOTHING
        
        elif self.locationType == LocationType.DUNGEON:
            self.front = LocationType.NOTHING
            self.back = LocationType.NOTHING
            self.left = LocationType.CAVE
            self.right = LocationType.CASTLE

        elif self.locationType == LocationType.CAVE:
            self.front = LocationType.MINE
            self.back = LocationType.WITCHES_HUT
            self.left = LocationType.NOTHING
            self.right = LocationType.DUNGEON

        elif self.locationType == LocationType.MINE:
            self.front = LocationType.NOTHING
            self.back = LocationType.CAVE
            self.left = LocationType.NOTHING
            self.right = LocationType.NOTHING




    '''
    '''
    def __init__(self, p_locationType):
        self.locationType = p_locationType
        self.locationName = p_locationType.value

        self.front = LocationType.NOTHING
        self.back = LocationType.NOTHING
        self.left = LocationType.NOTHING
        self.right = LocationType.NOTHING

        self.setNeighborLocations()



class Commands(Enum):

    QUIT_GAME = -1
    WALK_FORWARD = 0
    WALK_BACKWARD = 1
    WALK_LEFT = 2
    WALK_RIGHT = 3
    STAY_HERE = 4

    '''
    Return a list of allCommands<Commands>, no matter the size
    '''
    def getCommands():
        originalCommand = Commands(len(Commands) - len(Commands) - 1) # Start at the first command
        allCommands = [originalCommand] # Create the list of all commands; append our starting command
        currentCommand = originalCommand.next() # Create the currentCommand which will be our iterator
        while currentCommand.value != originalCommand.value: # Check to make sure we havent returned to our original (first) command
            allCommands.append(currentCommand) # Continue to append to our list otherwise
            currentCommand = currentCommand.next() # Iterate to the next command
        return allCommands # Return our list of commands


    def next(self):
        currentEnumValue = Commands(self.value)
        if currentEnumValue == Commands(len(Commands) - 2):
            return Commands(len(Commands) - len(Commands) - 1) # Return to bottom of enum
        return Commands(self.value + 1) # Otherwise, get the next enum value

    def prev(self):
        currentEnumValue = Commands(self.value)
        if currentEnumValue == Commands(len(Commands) - len(Commands) - 1):
            return Commands(len(Commands) - (len(Commands) - len(Commands) - 1)) # Return to top of enum
        return Commands(self.value - 1) # Otherwise, get the previous enum value
