#You and your spouse decided to let the internet name your next child. 
#You’ve asked the great people of the web to submit their favorite names, 
#and you’ve compiled their submissions into a Series called babynames.

import numpy as np
import pandas as pd

df = pd.read_csv("bitcoin_origin.csv", parse_dates=['Timestamp'])

df1 = df[(df['Timestamp'] >= '2020-01-01 00:00:00+00:00') & (df['Timestamp'] <= '2020-01-31 23:59:00+00:00')]

df1.to_csv("bitcoin.csv", index= False, date_format='%Y-%m-%d %H:%M:%S')