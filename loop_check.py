#!/usr/bin/env python
# -*- coding: utf-8 -*-

from instapy import InstaPy

insta_username = 'angelina___666_01'
insta_password = 'asdfasdf'

# set headless_browser=True if you want to run InstaPy on a server
try:
    session = InstaPy(username=insta_username,
                      password=insta_password,
                      nogui=True,
                      multi_logs=True)
    session.login()

    # settings
    session.set_upper_follower_count(limit=2500)
    session.set_do_comment(True, percentage=10)
    session.set_comments(['aMEIzing!', 'So much fun!!', 'Nicey!'])
    session.set_dont_include(['friend1', 'friend2', 'friend3'])
    session.set_dont_like(['pizza', 'girl'])

    # actions
    session.like_by_tags(['natgeo'], amount=1)

finally:
    # end the bot session
    session.end()
