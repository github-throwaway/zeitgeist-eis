from facebook_scraper import get_posts
import datetime
import locale
import re
import csv

locale.setlocale(locale.LC_TIME, "de_DE")
pagename = 'eismanufakturzeitgeist'

# get latest facebook post by grabbing the first item of the generator returned
# by get_posts
post = next(get_posts(pagename, pages=1))

# handle date of post
# assumption: ice cream flavour are posted the same day
date = post['time']  # grab date
date = date.strftime('%A, %d.%m.%Y')  # format datetime object

# get post text (String)
post_text = post['text']

# assumption: vanilla and chocolate are always on offer
# so if the post does not contain vanilla and chocolate it is not about ice
# cream

if "Vanille" and "Schokolade" not in post_text:
    print("No ice cream update.")
else:
    # remove everything before Lindenhof and after up until the :
    # TODO: This breaks if Limburgerhof is posted first
    regex = re.compile(r'.*?Lindenhof.*?:', re.DOTALL)
    post_text = re.sub(regex, 'Lindenhof', post_text)

    # split on linebreaks
    post_text = re.split('[ ]*\n+[ ]*', post_text.strip())

    # remove last sentence
    if "schmecken" in post_text[-1]:
        del post_text[-1]

    regex = re.compile(r'.*?Limburgerhof.*?:', re.DOTALL)

    for i, x in enumerate(post_text):
        if 'Limburgerhof' in x:
            # remove everything before Limburgerhof and after up until the :
            post_text[i] = re.sub(regex, 'Limburgerhof', x)

    # split on , & 'und'
    for i, x in enumerate(post_text):
        post_text[i] = re.split('und|[,]', x)

    with open(date+'.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=',',)
        # write header and remove entries from list
        writer.writerow([*post_text.pop(0), *post_text.pop(1), ])

        zipped_list = zip(*post_text)
        for x in zipped_list:
            writer.writerow(x)