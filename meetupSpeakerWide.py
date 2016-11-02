import pandas as pd
import numpy as np

meetup = pd.read_csv('techMeetupsNotated.csv')

meetup=meetup[meetup['applicable'] == 1]

meetup=meetup.drop(['applicable','desc','name','time'],axis=1)

meetup['singleSpeaker'] = np.where(meetup['male'] + meetup['female'] == 1, 'yes', 'no')

meetupSum=meetup.groupby(['group','singleSpeaker']).sum().add_prefix('sum_')

meetupSingle= meetupSum.loc[(meetupSum.index.get_level_values('singleSpeaker') == 'yes')]
meetupSingle.index = meetupSingle.index.droplevel(1)

meetupMulti= meetupSum.loc[(meetupSum.index.get_level_values('singleSpeaker') == 'no')]
meetupMulti.index = meetupMulti.index.droplevel(1)

meetupSingle.to_csv('meetupSingleSum.csv')
meetupMulti.to_csv('meetupSingleMulti.csv')