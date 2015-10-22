# -*- coding: utf-8 -*-
import os
from slacker import Slacker
import sendgrid
from datetime import datetime
from pytz import timezone

sg = sendgrid.SendGridClient(os.environ['SENDGRID_USERNAME'], os.environ['SENDGRID_PASSWORD'], raise_errors=True)


def slack_cleaning_bot():
    slack = Slacker(os.environ['SLACK_KEY'])
    people = ['canzhi', 'stevensuckscock', 'neeloy', 'rohan', 'amillman', 'steven']
    day_of_year = datetime.now(tz=timezone('US/Pacific')).timetuple().tm_yday
    message = "today is @" + str(people[day_of_year%6]) + "'s day to do the dishes. Tomorow is @" + str(people[(day_of_year+1)%6])
    slack.chat.post_message('#cleaning', message)
    im_david = '👀 good shit go౦ԁ sHit👌 thats ✔ some good👌shit right👌there👌👌 rightthere ✔if i do ƽaү so my self'.decode('utf-8')
    david_message = sendgrid.Mail(to='david@dtbui.com', subject=im_david, html='<strong>' + message + '</strong>', text=message, from_email="shashank@thenothing.co")
    message = sendgrid.Mail(to='rohanpai@berkeley.edu', subject='CLEAN THE DISHWASHER TODAY', html='<strong> IT IS YOUR LUCKY DAY MOTHAFUCKA</strong>', text='IT IS YOUR LUCKY DAY MOTHAFUCKA', from_email="shashank@thenothing.co")
    try:
        d_status, d_msg = sg.send(david_message)
        if people[day_of_year%6] == 'rohan':
            status, msg = sg.send(message)
    except SendGridClientError:
        print "client messsed up"
    except SendGridServerError:
        print "server messsed up"


slack_cleaning_bot()
