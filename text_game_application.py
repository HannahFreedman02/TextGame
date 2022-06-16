from text_game_definitions import Game, Character, CharacterType, Location, LocationType, Commands


class Application:

    '''
    '''
    def chooseACharacter(self):
        print('Please choose a character: ')
        print('1 Hungry Hannah')
        print('2 Nifty Nicholas')
        print('-1 Quit Game')

        userInput = input()

        if userInput == '-1':
            exit()
        
        elif userInput == '1':
            print('You have chosen Hungry Hannah!')
            return CharacterType.HUNGRY_HANNAH
        

        elif userInput == '2':
            print('You have chosen Nifty Nicholas!')
            return CharacterType.NIFTY_NICHOLAS


    '''
    '''
    def executeMoveCharacter(self, p_command):
        if self.game.moveCharacter(p_command) == True:
            print('\nThe character moves ' + str(p_command.value))
        else:
            print('\nThe character cannot move there.')


    '''
    '''
    def __init__(self):
        self.game = Game()

        print('\nWelcome to Adventure Friends!\n')
        
        self.character = Character(self.chooseACharacter())
        self.game.setCharacter(self.character)
        


        while True:
            print('\nYou are currently at ' + str(self.character.currentLocation.locationName) + '\n'\
                + 'There is ' + str(self.character.currentLocation.left.value) + ' to your left, \n'\
                + 'There is ' + str(self.character.currentLocation.right.value) + ' to your right, \n'\
                + 'There is ' + str(self.character.currentLocation.front.value) + ' in front of you, \n'\
                + 'There is ' + str(self.character.currentLocation.back.value) + ' behind you. \n')

            print('Please choose an action:')
            commandList = Commands.getCommands()
            for i in range(len(commandList)):
                print(str(i-1) + ' ' + commandList[i].name)

            userInput = input()

            if userInput == str(Commands.QUIT_GAME.value):
                exit()

            elif userInput == str(Commands.STAY_HERE.value):
                self.executeMoveCharacter(Commands.STAY_HERE)
            
            elif userInput == str(Commands.WALK_FORWARD.value):
                self.executeMoveCharacter(Commands.WALK_FORWARD)
            
            elif userInput == str(Commands.WALK_BACKWARD.value):
                self.executeMoveCharacter(Commands.WALK_BACKWARD)

            elif userInput == str(Commands.WALK_LEFT.value):
                self.executeMoveCharacter(Commands.WALK_LEFT)

            elif userInput == str(Commands.WALK_RIGHT.value):
                self.executeMoveCharacter(Commands.WALK_RIGHT)

            else:
                print('Command not recognized.')

        







