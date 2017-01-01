import pandas as pd
import numpy as np
import re

meetup = pd.read_csv('techMeetupsNotated.csv')

for i, m in meetup.iterrows():
    meetup.ix[i, 'applicable'] = 0
    meetup.ix[i, 'female'] = 0
    meetup.ix[i, 'male'] = 0
    # females
    if re.search(r'(\bshe\b | \bher\b)', m['desc'], flags=re.I) is not None:
        meetup.ix[i, 'applicable'] = 1
        meetup.ix[i, 'female'] = 1
    # males
    if re.search(r'\bhe\b | \bhim\b | \bhis\b', m['desc'], flags=re.I) is not None:
        meetup.ix[i, 'applicable'] = 1
        meetup.ix[i, 'male'] = 1

meetup.to_csv('techMeetupsNotated.csv', encoding='utf-8', index=False)
print('Done!')
