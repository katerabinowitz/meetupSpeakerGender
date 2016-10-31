import pandas as pd
import numpy as np

meetup = pd.read_csv('techMeetupsNotated.csv')
print meetup.info()


meetup=meetup[meetup['applicable'] == 1]

meetup=meetup.drop(['applicable','desc','name','time'],axis=1)

meetup['singleSpeaker'] = np.where(meetup['male'] + meetup['female'] == 1, 'yes', 'no')

meetupSum=meetup.groupby(['group','singleSpeaker']).sum().add_prefix('sum_')
print meetupSum

meetupSum.to_csv('meetupGenderSum.csv')
