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

listQuestions = list()
listAnswers = list()
homer = 2
numberHomerAnswers = 0
for i in range(len(database)):
    episode = database[i][0]
    location = database[i][3]
    characterQuestion = database[i-1][2]
    characterAnswer = database[i][2]
    if characterQuestion == '':
        continue
    if characterAnswer == '':
        continue
    if characterQuestion == characterAnswer:
        continue
    question = ''
    j = i-1
    while True:
        if database[j][0] != episode:
            break
        if database[j][1] != True:
            break
        if database[j][2] != characterQuestion:
            break
        if database[j][3] != location:
            break
        question = database[j][4] + ' ' + question
        j -= 1
    j = i
    answer = ''
    while True:
        if database[j][0] != episode:
            break
        if database[j][1] != True:
            break
        if database[j][2] != characterAnswer:
            break
        if database[j][3] != location:
            break
        answer = answer + ' ' + database[j][4]
        j += 1
        if j > len(database):
            break
    if len(question.strip()) == 0:
        continue
    if len(answer.strip()) == 0:
        continue
    if characterAnswer == homer:
        numberHomerAnswers += 1
        listQuestions = [question] + listQuestions
        listAnswers = [answer] + listAnswers
    else:
        listQuestions = listQuestions + [question]
        listAnswers = listAnswers + [answer]
        
fileQuestions = open('questions.txt', 'w', encoding='utf-8')
for question in listQuestions:
    fileQuestions.write(question.lower() + '\n')
fileQuestions.close()

fileAnswers = open('answers.txt', 'w', encoding='utf-8')
for answer in listAnswers:
    fileAnswers.write(answer.lower() + '\n')
fileAnswers.close()

print(numberHomerAnswers)
