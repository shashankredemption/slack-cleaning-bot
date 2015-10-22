import os
from slacker import Slacker
import sendgrid
from datetime import datetime
from pytz import timezone
import pytz

sg = sendgrid.SendGridClient(os.environ['SENDGRID_USERNAME'], os.environ['SENDGRID_PASSWORD'], raise_errors=True)


def slack_cleaning_bot():
    slack = Slacker(os.environ['SLACK_KEY'])
    people = ['canzhi', 'stevensuckscock', 'neeloy', 'rohan', 'amillman', 'steven']
    date = datetime.now(tz=pytz.utc)
    date = date.astimezone(timezone('US/Pacific'))
    day_of_year = date.timetuple().tm_yday
    slack.chat.post_message('#cleaning', "today is @" + str(people[day_of_year%6]) + "'s day to do the dishes. Tomorow is @" + str(people[(day_of_year+1)%6]))
    if people[day_of_year%6] == 'rohan':
        message = sendgrid.Mail(to='rohanpai@berkeley.edu', subject='CLEAN THE DISHWASHER TODAY', html='<strong> IT IS YOUR LUCKY DAY MOTHAFUCKA</strong>', text='IT IS YOUR LUCKY DAY MOTHAFUCKA', from_email="shashank@thenothing.co")
        try:
            status, msg = sg.send(message)
        except SendGridClientError:
            print "client messsed up"
        except SendGridServerError:
            print "server messsed up"

slack_cleaning_bot()
