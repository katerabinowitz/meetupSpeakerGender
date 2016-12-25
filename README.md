# The Gender Divide of Austin Tech Meetup Speakers

An Austin fork of [this project](http://www.datalensdc.com/meetupSpeakers.html), started in DC by [Kate Rabinowitz](https://github.com/katerabinowitz/meetupSpeakerGender)

#### The Austin Writeup:

*Work in progress:*
(http://amaliebarras.github.io/meetupSpeakerVizs)


#### Help close the gap:
*Coming soon:*
http://wespeaktoo.org/austin

#### Data Source:
[Meetup API](https://www.meetup.com/meetup_api/)

#### Methodology:

In meetup's [api console](https://secure.meetup.com/meetup_api/console/?path=/find/groups) I grabbed Austin's top 50 meetup groups in the 'tech' category, sorted by members. In order to grab the individual events for these meetups, I know I'd need just the `url-group-name` for each. I converted the output json into a CSV using an [online tool](https://konklone.io/json/), and deduplicated on `url-group-name`. Then, I went through and deleted groups that I knew were not speaker events (such as OpenHack Austin). Because there were still over 45 groups meeting this criteria, I chose a sample of these groups to visualize, sorting the groups by total member count, and keeping every third group.

I made this into a narrowed-down [meetup group list](https://github.com/amaliebarras/meetupSpeakerGender/blob/sample/groupList.csv), so that with a [Meetup API key](https://secure.meetup.com/meetup_api/key/), and thanks to [Dash's commit on 11/30](https://github.com/amaliebarras/meetupSpeakerGender/commit/22e7a92d17b9972cec55ee968e3144fc43d06657) on I could use python to run  [meetupdatagrab.py](https://github.com/amaliebarras/meetupSpeakerGender/blob/sample/meetupDataGrab.py) and to create a doc with all the events, as well as a [template](https://github.com/amaliebarras/meetupSpeakerGender/blob/master/techMeetupsNotated.csv) to notate the events with the speaker gender.

** Note: ** Before you run python, you'll need to get setup.

* Grab your API Key from [meetup.com](https://secure.meetup.com/meetup_api/key/)
* Paste API key into meetupDataGrab.py
* Make sure you've got python install `brew install python`
* This also installs pip. Use pip to install virtualenv, which will let you create a virtual environment `pip install virtualenv`
* Inside of project directory, initialize a python environment `virtualenv meetup`
* Now activate the virtual environment  `source venv/bin/activate`
* This script uses pandas, so install that using pip `pip install pandas`
* Run script using `python ./meetupDataGrab.py`
* Lastly, deactivate the virtual environment  `deactivate`

Everyone I've talked to about this project has asked why I chose to manually encode this data, and the honest answer is that I thought that I could do it faster and more accurately. For what it's worth, Dash did experiment with creating [notationbot.py](https://github.com/amaliebarras/meetupSpeakerGender/blob/austin/notationBot.py), but it wasn't able to account for multi-speaker events.

Although in most cases the gender of the speaker was identifiable by the pronoun used in the event description, where a pronoun was not given, I searched for other online resources that did provide a pronoun. And in a few rare cases I used name to indicate gender. PLEASE let me know if you spot an issue, I'd love to have the most accurate data possible.

I ended up opening the [template](https://github.com/amaliebarras/meetupSpeakerGender/blob/master/techMeetupsNotated.csv) in google sheets and notating there.

When done, I saved a copy into the repository as [techMeetupsNotatedDone.csv](https://github.com/amaliebarras/meetupSpeakerGender/blob/austin/techMeetupsNotatedDone.csv).

This is absolutely the most painful part of this exercise. Another developer is working on a [tool](https://github.com/flexyford/WeSpeakTooDashboard) for future local champions who want to replicate this analysis.

In order to transform this data into a format that is ingestible by [kate's d3 charts](https://github.com/katerabinowitz/DataLensDCsite/blob/gh-pages/iframes/meetupMultiBig.html), I ran my notated data through [meetupspeakerwide.py](https://github.com/amaliebarras/meetupSpeakerGender/blob/master/meetupSpeakerWide.py)

#### Visualizations

I used gh-pages to create a [writeup site](https://github.com/amaliebarras/MeetupSpeakerVizs/tree/master), including Kate's d3 visualizations as iFrames, changing only the data URL within each of them.
