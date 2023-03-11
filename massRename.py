import os, shutil

showName = input('Show Name?: ')
season = input('Season?: ')
episode = 1
renameList = []

print('')

for file in os.listdir('.'):
    if file == 'massRename.py':
        continue

    if len(str(episode)) == 1:
        curEpisode = '0' + str(episode)
    else:
        curEpisode = episode
    if len(str(season)) == 1:
        curSeason = '0' + str(season)
    else:
        curSeason = season
    
    newFile = showName + ' S' + curSeason + 'E' + str(curEpisode) + '.mkv'

    print(file + ' >> ' + newFile)
    renameList.append([file] + [newFile])
    episode += 1

if input('\nType Y to accept: ') != 'Y':
    exit()

for item in renameList:
    shutil.move(item[0], item[1])

input('Done!')
