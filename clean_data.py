import pandas as pd
import numpy as np

database = pd.read_csv('simpsons_script_lines.csv').replace(np.nan, '', regex=True)
database = database.drop('id', 1)
database = database.drop('number', 1)
database = database.drop('raw_text', 1)
database = database.drop('timestamp_in_ms', 1)
database = database.drop('raw_character_text', 1)
database = database.drop('raw_location_text', 1)
database = database.drop('normalized_text', 1)
database = database.drop('word_count', 1)
database = database.values.tolist()


fileA = open('homer_train.a', 'w', encoding='utf-8')
fileB = open('homer_train.b', 'w', encoding='utf-8')
fileAt = open('homer_test.a', 'w', encoding='utf-8')
fileBt = open('homer_test.b', 'w', encoding='utf-8')
homer = 2
counter = 0
for i in range(len(database)):
    if database[i][1] == True:
        if database[i][2] == 2:
            j = i-1
            episode = database[j][0]
            character = database[j][2]
            location = database[j][3]
            if episode != database[i][0]:
                continue
            if character == '':
                continue
            if character == homer:
                continue
            if location != database[i][3]:
                continue
            falaA = database[j][4]
            while True:
                j -= 1
                if database[j][0] != episode:
                    break
                if database[j][1] != True:
                    break
                if database[j][2] != character:
                    break
                if database[j][3] != location:
                    break
                falaA = database[j][4] + ' ' + falaA
            j = i
            falaB = database[j][4]
            while True:
                j += 1
                if database[j][0] != episode:
                    break
                if database[j][1] != True:
                    break
                if database[j][2] != homer:
                    break
                if database[j][3] != location:
                    break
                falaB = falaB + ' ' + database[j][4]
            if len(falaA.strip()) == 0:
                continue
            if len(falaB.strip()) == 0:
                continue
            counter += 1
            if counter % 5 == 0:
                fileAt.write(falaA.lower() + '\n')
                fileBt.write(falaB.lower() + '\n')
            else:
                fileA.write(falaA.lower() + '\n')
                fileB.write(falaB.lower() + '\n')
fileA.close()
fileB.close()
fileAt.close()
fileBt.close()
