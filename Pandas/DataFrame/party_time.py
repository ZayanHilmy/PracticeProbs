#Whenever your friends John and Judy visit you together, y’all have a party 🥳. 
#Given a DataFrame with 10 rows representing the next 10 days of your schedule and whether John and Judy are scheduled to make an appearance, 
#insert a new column called days_til_party that indicates how many days until the next party.
#days_til_party should be 0 on days when a party occurs, 1 on days when a party doesn’t occur but will occur the next day, etc.

import numpy as np
import pandas as pd

generator = np.random.default_rng(123)

df = pd.DataFrame({
    'john': generator.choice([True, False], size=10, replace=True),
    'judy': generator.choice([True, False], size=10, replace=True)
})


party = df.john & df.judy

idx = df.index.to_series()

df['days_til_party'] = idx.where(party).bfill() - idx

print(df.days_til_party)
