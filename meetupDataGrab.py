import requests
import pandas as pd

meetups = pd.read_csv('groupList.csv')

desc, time, name, group = [], [], [], []
key = 'KEYGOESGERE'
offset = 0

for i, m in meetups.iterrows():
    done = False
    while not done:
        url = 'https://api.meetup.com/2/events?key=' + key + '&offset=' + str(offset) + '&format=json&limited_events=False&group_urlname=' + \
            m['group_url'] + '&photo-host=public&time=1451610000000%2C&page=200&fields=&order=time&status=past&desc=false'
        print('Scraping', m['group_url'])
        response = requests.get(url, timeout=120)
        data = response.json()
        for result in data['results']:
            try:
                desc.append(result['description'])
                time.append(result['time'])
                name.append(result['name'])
                group.append(result['group']['name'])
            except:
                pass
        print('Found', len(data['results']))
        if len(data['results']) == 200:
            offset = offset + 1
        else:
            offset = 0
            done = True

columns = {'desc': desc, 'time': time, 'name': name, 'group': group}
meetupDF = pd.DataFrame(columns)
meetupDF.to_csv('techMeetups.csv', encoding='utf-8', index=False)

# prints a template of the notated csv file
meetupDF = pd.concat([pd.DataFrame(columns=['applicable', 'male', 'female', 'nonBinary']),
                      meetupDF], axis=1)
meetupDF.to_csv('techMeetupsNotated.csv', encoding='utf-8', index=False)
print('Done!')
