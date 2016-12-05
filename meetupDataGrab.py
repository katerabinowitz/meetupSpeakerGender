import urllib
import json
import pandas as pd

meetup=['Austin-Web-Design','CoFounder-Austin','austinpython','Austin-Lean-Startup-Circle', 'Built-In-Austin', 'atxstartupscene']

desc,time,name,group = [],[],[],[]
dfList=[]
meetupDF=pd.DataFrame()
key='KEYGOESHERE'

for m in meetup:
	url='https://api.meetup.com/2/events?key='+key+'&offset=0&format=json&limited_events=False&group_urlname='+m+'&photo-host=public&time=1451610000000%2C&page=20&fields=&order=time&status=past&desc=false'

	response = urllib.urlopen(url)
	data = json.loads(response.read())
	for i in data['results']:
		desc.append(i['description'].encode('utf-8'))
		time.append(i['time'])
		name.append(i['name'].encode('utf-8'))
		group.append(i['group']['name'].encode('utf-8'))
	innerColumns = {'desc':desc,'time': time, 'name': name, 'group': group}
	df = pd.DataFrame(innerColumns)
dfList.append(df)
print dfList
meetupDF = pd.concat(dfList)
meetupDF.to_csv('techMeetups.csv')


	