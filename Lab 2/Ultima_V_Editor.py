##############
# Kevin Long #
# 014065153  #
# Lab 2      #
##############

#Saved game file location; edit according to file location
filePath = 'C:/dosbox/Ultima_5/SAVED.GAM'

#In-game characters
chars = {1: 'PLAYER', 2: 'SHAMINO', 3: 'IOLO',
         4: 'MARIAH', 5: 'GEOFFREY', 6: 'JAANA',
         7: 'JULIA', 8: 'DUPRE', 9: 'KATRINA',
         10: 'SENTRI', 11: 'GWENNO',  12: 'JOHNE',
         13: 'GORN', 14: 'MAXWELL', 15: 'TOSHI',
         16: 'SADUJ'}

#Offset (position) of characters in SAVED.GAM
charOffsets = {'PLAYER': int('0x02', 16), 'SHAMINO': int('0x22', 16), 'IOLO': int('0x42', 16),
                'MARIAH': int('0x62', 16), 'GEOFFREY': int('0x82', 16), 'JAANA': int('0xA2', 16),
                'JULIA': int('0xC2', 16), 'DUPRE': int('0xE2', 16), 'KATRINA': int('0x102', 16),
                'SENTRI': int('0x122', 16), 'GWENNO': int('0x142', 16), 'JOHNE': int('0x162', 16),
                'GORN': int('0x182', 16), 'MAXWELL': int('0x1A2', 16), 'TOSHI': int('0x1C2', 16),
                'SADUJ': int('0x1E2', 16)}

#Character stats
stats = {1: 'STRENGTH', 2: 'DEXTERITY', 3: 'INTELLIGENCE',
         4: 'MAGIC', 5: 'HP', 6: 'MAX HP',
         7: 'EXPERIENCE'}

#Offset (position) of character stats in SAVED.GAM
statOffsets = {'STRENGTH': int('0x0E', 16), 'DEXTERITY': int('0x0F', 16), 'INTELLIGENCE': int('0x10', 16),
               'MAGIC': int('0x11', 16), 'HP': int('0x12', 16), 'MAX HP': int('0x14', 16),
               'EXPERIENCE': int('0x16', 16)}

#Maximum values for statss (in decimal to be converted to hex for offsets in SAVED.GAM)
statMaxVal = {'STRENGTH': 255, 'DEXTERITY': 255, 'INTELLIGENCE': 255,
              'MAGIC': 65535, 'HP': 65535, 'MAX HP': 65535,
              'EXPERIENCE': 255}

#Inventory items
items = {1: 'GOLD', 2: 'KEYS', 3: 'GEMS',
         4: 'MAGIC CARPET', 5: 'SKULL KEYS', 6: 'BLACK BADGE',
         7: 'MAGIC AXE'}

#Offsets (position) of inventory items in SAVED.GAM
itemOffsets = {'GOLD': int('0x204', 16), 'KEYS': int('0x206', 16), 'GEMS': int('0x207', 16),
               'MAGIC CARPET': int('0x20A', 16), 'SKULL KEYS': int('0x20B', 16), 'BLACK BADGE': int('0x218', 16),
               'MAGIC AXE': int('0x240', 16)}

#Maximum values for items (in decimal to be converted to hex for offsets in SAVED.GAM)
itemMaxVal = {'GOLD': 65535, 'KEYS': 255, 'GEMS': 255,
              'MAGIC CARPET': 255, 'SKULL KEYS': 255, 'BLACK BADGE': 255,
              'MAGIC AXE': 255}

def readFile() -> list:
    """
    Reads in binary values of SAVED.GAM file
    
    @returns: list of SAVE.GAM hex offset values in decimal form
    """
    with open(filePath, 'rb') as saveFile:
        dataBytes = list(bytearray(saveFile.read()))
        saveFile.close()
    return dataBytes

def writeToFile(fileData:list):
    """
    Writes in binary values to SAVED.GAM file

    @param fileData: list of SAVE.GAM hex offset values in decimal form
    """
    with open(filePath, 'wb') as saveFile:
        saveFile.write(bytearray(fileData))
        saveFile.close()
        
def editStats(charDictKey:int, fileData:list):
    """
    Prompts user to select which stat they want to edit
    
    @param charDictKey: the key associated with the character in 'chars'
    @param fileData: list of SAVE.GAM hex offset values in decimal form (from readFile())
    """
    print('\n-----------------------------------------')
    print('Choose a stat to edit for {}:'.format(chars[charDictKey]))
    print('[1] {}\n[2] {}\n[3] {}\n[4] {}\n[5] {}\n[6] {}\n[7] {}'.format(stats[1], stats[2], stats[3], stats[4],
                                                                          stats[5], stats[6], stats[7]))
    print('-----------------------------------------')
    
    #Prompt user to choose which stat to edit
    while True:
        try:
            userInp = int(input('>>>: '))
        except ValueError:
            print('Please enter a valid option (1-7).')
            continue
        if userInp < 1 or userInp > 7:
            print('Please enter a valid option (1-7).')
            continue
        else:
            break
        
    statName = stats[userInp]
    index = statOffsets[statName] + charOffsets[chars[charDictKey]]
    maxVal = statMaxVal[statName]
    if maxVal < 256:
        currVal = fileData[index]
    else:
        currVal = 0
        
    #Prompt user for stat val to change to
    while True:
        try:
            print('Current stat for {}\'S {} is {}.'.format(chars[charDictKey], statName, fileData[index]))
            print('What would you like to change it to? (0 - {})'.format(maxVal))
            statChange = int(input('>>>: '))
        except ValueError:
            print('Please enter a valid option (0 - {}).'.format(maxVal))
            continue
        if statChange < 0 or statChange > maxVal:
            print('Please enter a valid option (0 - {}).'.format(maxVal))
            continue
        else:
            break
        
    #Make changes to SAVE.GAM
    count = 0
    byteArray = list(bytearray((statChange).to_bytes(2, byteorder='little')))
    if len(byteArray) == 1:
        byteArray.insert(0, 0)
    for b in byteArray:
        fileData[index + count] = b
        count += 1
    print('{} {} changed to {}'.format(chars[charDictKey], statName, statChange))
    
    #Prompt user for additional changes
    print('\nWould you like to edit another stat? [Y or N]')
    userInp = input('>>>: ')
    while userInp.upper() != 'Y' and userInp.upper() != 'N':
        print('Please enter a valid option (Y or N).')
        userInp = input('>>>: ')
    if userInp.upper() == 'Y':
        editStats(charDictKey, fileData)
    else:
        print('Returning to character selection...\n')
        
def charSelect(fileData:list):
    """
    Prompts user to select a character they want to edit

    @param fileData: list of SAVE.GAM hex offset values in decimal form (from readFile())
    """
    print('\n-----------------------------------------')
    print('Choose a character to edit:')
    print('[1] {}\n[2] {}\n[3] {}\n[4] {}\n[5] {}\n[6] {}\n[7] {}\n[8] {}'.format(chars[1], chars[2], chars[3], chars[4],
                                                                                  chars[5], chars[6], chars[7], chars[8]))
    print('[9] {}\n[10] {}\n[11] {}\n[12] {}\n[13] {}\n[14] {}\n[15] {}\n[16] {}'.format(chars[9], chars[10], chars[11], chars[12],
                                                                                  chars[13], chars[14], chars[15], chars[16]))
    print('-----------------------------------------')
    
    #Prompt user to choose which character to edit
    while True:
        try:
            userInp = int(input('>>>: '))
        except ValueError:
            print('Please enter a valid option (1 - 16).')
            continue
        if userInp < 1 or userInp > 16:
            print('Please enter a valid option (1 - 16).')
            continue
        else:
            break
    editStats(userInp, fileData)
    
    #Prompt user for additional changes
    print('Would you like to edit another character? [Y or N]')
    userInp = input('>>>: ')
    while userInp.upper() != 'Y' and userInp.upper() != 'N':
        print('Please enter a valid option (Y or N).')
        userInp = input('>>>: ')
    if userInp.upper() == 'Y':
        charSelect(fileData)
    else:
        print('Returning to menu...\n')
        menu(fileData)

def editItems(itemDictKey:int, fileData:list):
    """
    Prompts user to enter a value they want to edit to

    @param itemDictKey: the key associated with the item in 'items'
    @param fileData: list of SAVE.GAM hex offset values in decimal form (from readFile())
    """
    itemName = items[itemDictKey]
    index = itemOffsets[itemName] 
    maxVal = itemMaxVal[itemName]
    if maxVal > 255 and fileData[index] > 0:
        currVal = int(hex(fileData[index])[2:] + hex(fileData[index + 1])[2:], 16)
    elif maxVal > 255 and fileData[index] == 0:
        currVal = fileData[index + 1]
    else:
        currVal = fileData[index]
        
    #Prompt user for stat val to change to
    while True:
        try:
            print('Current amount of {} in inventory is {}.'.format(items[itemDictKey], fileData[index]))
            print('What would you like to change it to? (0 - {})'.format(maxVal))
            itemChange = int(input('>>>: '))
        except ValueError:
            print('Please enter a valid option (0 - {}).'.format(maxVal))
            continue
        if itemChange < 0 or itemChange > maxVal:
            print('Please enter a valid option (0 - {}).'.format(maxVal))
            continue
        else:
            break
        
    #Make changes to SAVE.GAM
    count = 0
    byteArray = list(bytearray((itemChange).to_bytes(2, byteorder='little')))
    if len(byteArray) == 1:
        byteArray.insert(0, 0)
    for b in byteArray:
        fileData[index + count] = b
        count += 1
    print('Number of {} changed to {}'.format(itemName, itemChange))
    
    #Prompt user for additional changes
    print('\nWould you like to edit another item? [Y or N]')
    userInp = input('>>>: ')
    while userInp.upper() != 'Y' and userInp.upper() != 'N':
        print('Please enter a valid option (Y or N).')
        userInp = input('>>>: ')
    if userInp.upper() == 'Y':
        itemSelect(fileData)
    else:
        print('Returning to item selection...\n')

def itemSelect(fileData:list):
    """
    Prompts user to select an item's value they want to edit
    
    @param fileData: list of SAVE.GAM hex offset values in decimal form (from readFile())
    """
    print('\n-----------------------------------------')
    print('Choose an item to edit:')
    print('[1] {}\n[2] {}\n[3] {}\n[4] {}\n[5] {}\n[6] {}\n[7] {}'.format(items[1], items[2], items[3], items[4],
                                                                                  items[5], items[6], items[7]))
    print('-----------------------------------------')

    #Prompt user to choose which item to edit
    while True:
        try:
            userInp = int(input('>>>: '))
        except ValueError:
            print('Please enter a valid option (1 - 7).')
            continue
        if userInp < 1 or userInp > 7:
            print('Please enter a valid option (1 - 7).')
            continue
        else:
            break
    editItems(userInp, fileData)

    #Prompt user for additional changes
    print('Would you like to edit another item? [Y or N]')
    userInp = input('>>>: ')
    while userInp.upper() != 'Y' and userInp.upper() != 'N':
        print('Please enter a valid option (Y or N).')
        userInp = input('>>>: ')
    if userInp.upper() == 'Y':
        itemSelect(fileData)
    else:
        print('Returning to menu...\n')
        menu(fileData)

def menu(fileData:list):
    """
    Text UI for save editor
    
    @param fileData: list of SAVE.GAM hex offset values in decimal form (from readFile())
    """
    print('########################')
    print('# ULTIMA V SAVE EDITOR #')
    print('########################')
    print('-----------------------------------------')
    print('Choose a category to edit:')
    print('[1] Character Stats (e.g. str, int, etc.)')
    print('[2] Inventory (e.g. gold, keys, etc.)')
    print('[3] Save Game File and Exit')
    print('-----------------------------------------')
    
    #Prompt user to choose a category to edit
    userInp = input('>>>: ')
    while userInp != '1' and userInp != '2' and userInp != '3':
        print('Please enter one of the three valid options (1 - 3).')
        userInp = input('>>>: ')
    if userInp == '1':
        charSelect(fileData)
    elif userInp == '2':
        itemSelect(fileData)
    else:
        print('Saving edits...')
        writeToFile(fileData) #Finalize all user changes to SAVE.GAM
        print('Game file changed. Exiting program.')
    
if __name__ == '__main__':
    menu(readFile())
