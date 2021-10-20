#Pre-request install python, install mozilla firefox, pip install instapy

from instapy import InstaPy 
from instapy import smart_run

your_username = ' ' #input your username here
your_password = ' ' #input your password here

session = InstaPy(username = your_username,
                  password = your_password,
                  headless_browser = False) #headless browser if set True will run without displaying mozilla firefox in background

#change the values as per your needs
with smart_run(session):
    session.set_relationship_bounds(enabled=True,
                                    delimit_by_numbers=True,
                                    max_followers=700,
                                    min_followers=30,
                                    min_following=100)
    
    session.set_do_follow(True, percentage=80)
    session.set_dont_like(['nsfw', 'tiktok'])
    
    session.like_by_tags(['jdm', 'anime', 'rocketbunny', 'sliceoflife', 'webdev', 'react', 'codingmemes', 'memes', 'sarcasm', 'cosmos'], amount=10)
    session.set_do_comment(True, percentage=60)

    session.set_comments(["Very nice!", "Good", "Cool", "Very interesting", "Nice", "Interesting", "Nice job"])
