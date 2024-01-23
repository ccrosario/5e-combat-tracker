import pandas
import pyfiglet
import random

#declare global values
registeringCombatant = {}
initiativeOrder = []
initiativeRoll = int
registration = True

#styled name heading
trackerHeading1 = pyfiglet.figlet_format('   Combat', font="cyberlarge")
trackerHeading2 = pyfiglet.figlet_format('  Tracker', font="cyberlarge")

#add combatant to order
def addToOrder():
    userInput = input('Enter a combatant: ')
    registeringCombatant[0, 0] = userInput
    userInput = input('How many hit points do they currently have: ')
    registeringCombatant[0, 1] = userInput
    userInput = int(input('What is their Dexterity modifier: '))
    registeringCombatant[0, 2] = userInput
    userInput = int(input('Enter the sum of any other bonuses: '))
    registeringCombatant[0, 3] = userInput
    initiativeRoll = (random.randint(1, 20) + registeringCombatant[0, 2] + registeringCombatant[0, 3])
    initiativeOrder.append(
        [registeringCombatant[0, 0],
         registeringCombatant[0, 1],
         registeringCombatant[0, 2],
         registeringCombatant[0, 3],
         initiativeRoll
         ])
    initiativeOrder.sort(key=lambda x: x[4], reverse=True)
    printInitiative()


#[WIP]remove combatant from order
def removeFromOrder():
    result = None
    combatantToRemove = input('Enter the name of the combatant you would like to remove: ')
    for i in range(len(initiativeOrder)):
        if combatantToRemove in initiativeOrder[i]:
            result = i
            initiativeOrder.pop(result)
            print(result)


#print the current iniative order to the console
def printInitiative():
    initiativeTable = pandas.DataFrame(initiativeOrder,
        columns=['Name', 'Hit Points', 'DEX Modifier', 'Bonuses', 'Initiative'])
    print(initiativeTable)
    print('\n')


#loading image/intro screen/ascii art
print('                                      /|\n                                     |\\|\n                                     |||\n                                     |||\n                                     |||\n                                     |||\n                                     |||\n                                     |||\n                                  ~-[{o}]-~\n                                     |/|\n                                     |/|\n             ///~`     |\\\\_          `0\'         =\\\\\\\\         . .\n            ,  |=\'  ,))\\_| ~-_                    _)  \\      _/_/|\n           / ,\' ,;((((((    ~ \\                  `~~~\\-~-_ /~ (_/\\\n         /\' -~/~)))))))\'\\_   _/\'                      \\_  /\'  D   |\n        (       (((((( ~-/ ~-/                          ~-;  /    \\--_\n         ~~--|   ))\'\'    \')  `                            `~~\\_    \\   )\n             :        (_  ~\\           ,                    /~~-     ./\n              \\        \\_   )--__  /(_/)                   |    )    )|\n    ___       |_     \\__/~-__    ~~   ,\'      /,_;,   __--(   _/      |\n  //~~\\`\\    /\' ~~~----|     ~~~~~~~~\'        \\-  ((~~    __-~        |\n((()   `\\`\\_(_     _-~~-\\                      ``~~ ~~~~~~   \\_      /\n )))     ~----\'   /      \\                                   )       )\n  (         ;`~--\'        :                                _-    ,;;(\n            |    `\\       |                             _-~    ,;;;;)\n            |    /\'`\\     ;                          _-~          _/\n           /~   /    |    )                         /;;;\'\'  ,;;:-~\n          |    /     / | /                         |;;\'   ,\'\'\n          /   /     |  \\\\|                         |   ,;(    -Tua Xiong\n        _/  /\'       \\  \\_)                   .---__\\_    \\,--._______\n       ( )|\'         (~-_|                   (;;\'  ;;;~~~/\' `;;|  `;;;\\\n        ) `\\_         |-_;;--__               ~~~----__/\'    /\'_______/\n        `----\'       (   `~--_ ~~~;;------------~~~~~ ;;;\'_/\'\n                     `~~~~~~~~\'~~~-----....___;;;____---~~\n')
print(trackerHeading1, trackerHeading2)
print('                 You have found yourself in combat once again...\n')
print('    ╰ ─┉─¡! • !¡─┉─ ╯╰ ─┉─¡! • !¡─┉─ ╯╰ ─┉─¡! • !¡─┉─ ╯╰ ─┉─¡! • !¡─┉─ ╯')
print('                     ╰ ─┉─¡! • !¡─┉─ ╯╰ ─┉─¡! • !¡─┉─ ╯\n')


#initiate registration on load
while registration:
    addToOrder()
    moreCombatants = input('Are there any other combatants? (y/n): ')
    if moreCombatants == 'n':
        registration = False

#main menu
while not registration:
    print('And combat begins...\n---------------------')
    printInitiative()
    print(
        'You may enter any of the following commands:\nShow Order\nAdd Combatant\nRemove Combatant\n')
    commandSelection = input('What would you like to do?: ')

    if commandSelection == 'Show Order':
        printInitiative()

    if commandSelection == 'Add Combatant':
        addToOrder()

    if commandSelection == 'Remove Combatant':
        removeFromOrder()
