#The Gender Divide of Tech + Data Meetup Speakers

####Background:
Women and non-binary speakers continue to be rare at area tech and data professional events, despite growing prominence in the fields. Their absence on stage perpetuates existing gender imbalances. This project examine the gender gap of speakers at area tech and data meetup events. 

It started in DC but has been generalized for other cities. The code in this folder can replicate the analysis in your own city, with instructions below. Each city's data has it's own folder with notes. 

####Data Source: 
[Meetup API](https://www.meetup.com/meetup_api/)

###Findings:
http://www.datalensdc.com/meetupSpeakers.html

###Towards a Solution:
http://wespeaktoo.org/

###How you can participate:
This project originated in DC, and was improved upon when replicated in Austin. You can do the same for your city! Reach out to me if you're interested: datalensdc@gmail.com

The process:

1. Populate groupList.csv with the url-group-name of your local major meetups that are gender neutral, tech and/or data focused, and mainly do speaker series.
2. Grab your API Key from meetup.com and paste it into meetupDataGrab.py. Run meetupDataGrab.py.
  * You should already have Python installed and the Pandas library. 
3. Notate speaker count and gender in the techMeetupsNotated.csv file that was output. 
  * Yes, we used manual notation. We've played around with automating this process but it is difficult to accurately identify the number of speakers. The output list is also not very long. We welcome improvements.
4. Save your marked up file as techMeetupsNotatedDone.csv and run meetupSpeakerWide.py for summary results. 
5. Digest and visualize! Kate used D3 [here](https://github.com/katerabinowitz/DataLensDCsite/blob/gh-pages/iframes/meetupMultiBig.html) and [here](https://github.com/katerabinowitz/DataLensDCsite/blob/gh-pages/iframes/meetupSingleBig.html), but there are lots of different ways to do it.
6. Contact Kate (datalensdc@gmail.com) about expanding wespeaktoo.org to your city!
