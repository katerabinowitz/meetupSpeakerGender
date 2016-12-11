import pandas as pd
import numpy as np

meetup = pd.read_csv('techMeetupsSampleNotated.csv')
print meetup.info()

meetup=meetup[meetup['applicable'] == 1]

meetup=meetup.drop(['applicable','desc','name','time'],axis=1)

meetup['singleSpeaker'] = np.where(meetup['male'] + meetup['female'] == 1, 'yes', 'no')

meetupT=pd.melt(meetup, id_vars=['group','singleSpeaker'], value_vars=['male','female','nonBinary'])

meetupSum=meetupT.groupby(['group','singleSpeaker','variable']).sum().add_prefix('sum_')

meetupSingle= meetupSum.loc[(meetupSum.index.get_level_values('singleSpeaker') == 'yes')]
meetupMulti= meetupSum.loc[(meetupSum.index.get_level_values('singleSpeaker') == 'no')]

meetupSingle.to_csv('meetupSingleSum.csv')
meetupMulti.to_csv('meetupSingleMulti.csv')