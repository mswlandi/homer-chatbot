import pandas as pd
import numpy as np

database = pd.read_csv('simpsons_script_lines.csv').replace(np.nan, '', regex=True)
database = database.values.tolist()
newDatabase = open('new_simpsons_script_lines.csv', 'w', encoding = 'utf-8')
for i in database:
    buffer = []
    for j in i:
        buffer.append(str(j).replace(';','#'))
    newDatabase.write(';'.join(buffer)+'\n')
newDatabase.close()
