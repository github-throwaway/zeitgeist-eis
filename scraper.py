from facebook_scraper import get_posts
#from datetime import date, datetime, time
import datetime
from babel.dates import format_date, format_datetime, format_time
import locale

locale.setlocale(locale.LC_TIME, "de_DE")
pagename = 'eismanufakturzeitgeist'

# get latest facebook post by grabbing the first item of the generator returned
# by get_posts
post = next(get_posts(pagename, pages=1))

# handle date of post
# assumption: ice cream flavour are posted the same day
date = post['time']  # grab date
date = date.strftime('%A, %d.%m.%Y')  # format datetime object

# handle post text
post_text = post['text']
