import pandas as pd
import numpy as np

#read in annotated tech meetup descriptions with speaker info
meetup = pd.read_csv('techMeetupsNotated.csv')

#filter to necessary columns (nonBinary was removed because it's zero throughout and will be noted in graphs) and only applicable meetups (i.e., not hacknights, etc.)
meetup=meetup[meetup['applicable'] == 1]
meetup=meetup.drop(['applicable','desc','name','time','nonBinary'],axis=1)

#shorten names for viz
meetup['g']=meetup['group'].str.rstrip(' DC')
meetup['g']=meetup['group'].str.replace('Washington DC Area ','').str.replace(' DC', '').str.replace('DC ', '').str.replace('D.C. ','')
meetup['g']=meetup['g'].str.replace(' etc','').str.replace(' Professionals','').str.replace(' Community','')
meetup['g']=meetup['g'].replace('[^a-zA-Z\d\s]+','',regex=True)

meetup['g']=np.where(meetup['g']=="Apache Spark Interactive","Apache Spark",
	np.where(meetup['g']=="Natural Language Processing","NLP",
		np.where(meetup['g']=="Social Data and Analytics ","Social Data Analytics",
			 np.where(meetup['g']=="nodedc","NodeDC",
			 	np.where(meetup['g']=="Statistical Programming","Stats Programming",meetup['g'])))))

#identify multi vs. single speaker events and sum gender for each meetup type and group
meetup['singleSpeaker'] = np.where(meetup['male'] + meetup['female'] == 1, 'yes', 'no')

meetupSum=meetup.groupby(['g','singleSpeaker']).sum().add_prefix('sum_')
meetupSum=meetupSum.rename(columns = {'sum_male':'Male','sum_female':'Female'})

meetupSingle= meetupSum.loc[(meetupSum.index.get_level_values('singleSpeaker') == 'yes')]
meetupSingle.index = meetupSingle.index.droplevel(1)
meetupSingle.index = np.where(meetupSingle.index =="NodeDC","node.dc",meetupSingle.index)
meetupSingle.index.name = 'g'

meetupMulti= meetupSum.loc[(meetupSum.index.get_level_values('singleSpeaker') == 'no')]
meetupMulti.index = meetupMulti.index.droplevel(1)

#output
meetupSingle.to_csv('meetupSingleSum.csv')
meetupMulti.to_csv('meetupSingleMulti.csv')
