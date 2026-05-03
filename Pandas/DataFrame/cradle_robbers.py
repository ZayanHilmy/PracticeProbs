import numpy as np
import pandas as pd

couples = pd.DataFrame({
    'person1': ['Cody', 'Dustin', 'Peter', 'Adam', 'Ryan', 'Brian', 'Jordan', 'Gregory'],
    'person2': ['Sarah', 'Amber', 'Brianna', 'Caitlin', 'Rachel', 'Kristen', 'Alyssa', 'Morgan']
}).convert_dtypes()

ages = pd.DataFrame({
    'person': ['Adam', 'Alyssa', 'Amber', 'Brian', 'Brianna', 'Caitlin', 'Cody', 'Dustin', 'Gregory', 'Jordan',
               'Kristen', 'Rachel', 'Morgan', 'Peter', 'Ryan', 'Sarah'],
    'age': [62, 40, 41, 50, 65, 29, 27, 39, 42, 39, 33, 61, 43, 55, 28, 36]
}).convert_dtypes()



i= 0
while(i < len(couples['person1'])):
    man = couples.person1[i]
    woman = couples.person2[i]

    man_age = ages[ages['person'] == man]['age'].to_numpy()
  

    woman_age = ages[ages['person'] == woman]['age'].to_numpy()

    if (np.abs(man_age - woman_age)) > 20:
        if woman_age < 30 or man_age < 30:
            print(man, woman)



    i += 1