import pandas as pd
import numpy as np

#read in annotated tech meetup descriptions with speaker info
meetup = pd.read_csv('techMeetupsSampleNotated.csv')

#filter to necessary columns (nonBinary was removed because it's zero throughout and will be noted in graphs) and only applicable meetups (i.e., not hacknights, etc.)
meetup=meetup[meetup['applicable'] == 1]
meetup=meetup.drop(['applicable','desc','name','time','nonBinary'],axis=1)

# #shorten names for viz
meetup['g']=meetup['group']
meetup['g']=meetup['group'].str.replace('Austin Texas','ATX').str.replace('Austin ', '')
meetup['g']=meetup['g'].str.replace(' Group','').str.replace('(WebDesign&Developer)','').str.replace('Meetup','').str.replace('The Austin','').str.replace('The ', '')
# meetup['g']=meetup['g'].replace('[^a-zA-Z\d\s]+','',regex=True)

#identify multi vs. single speaker events and sum gender for each meetup type and group
meetup['singleSpeaker'] = np.where(meetup['male'] + meetup['female'] == 1, 'yes', 'no')

meetupSum=meetup.groupby(['g','singleSpeaker']).sum().add_prefix('sum_')
meetupSum=meetupSum.rename(columns = {'sum_male':'Male','sum_female':'Female'})

meetupSingle= meetupSum.loc[(meetupSum.index.get_level_values('singleSpeaker') == 'yes')]
meetupSingle.index = meetupSingle.index.droplevel(1)

meetupMulti= meetupSum.loc[(meetupSum.index.get_level_values('singleSpeaker') == 'no')]
meetupMulti.index = meetupMulti.index.droplevel(1)

#output
meetupSingle.to_csv('meetupSingleSum.csv')
meetupMulti.to_csv('meetupSingleMulti.csv')