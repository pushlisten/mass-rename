import os, shutil

#Set to 1 to enable custom naming, 0 to disable
custom = 1

if custom != 1:
    showName = input('Show Name?: ')
    season = input('Season?: ')
    ext = input('EXT?: ')
    if len(str(season)) == 1:
        season = '0' + str(season)
    else:
        season = season
counter = 1
renameList = []

print('')

for file in os.listdir('.'):
    if file == 'massRename.py':
        continue

    if len(str(counter)) == 1:
        episode = '0' + str(counter)
    else:
        episode = counter

    if custom != 1:
        newFile = showName + ' S' + season + 'E' + str(episode) + '.' + ext
    else:
        #Enter new name for files if using custom naming
        newFile = ''
        

    print(file + ' >> ' + newFile)
    renameList.append([file] + [newFile])
    counter += 1

if input('\nType Y to accept: ') != 'Y':
    exit()

for item in renameList:
    shutil.move(item[0], item[1])

input('Done!')
