#!/usr/bin/env python
# -*- coding: utf-8 -*-

from instapy import InstaPy

insta_username = 'angelina___666_01'
insta_password = 'asdfasdf'

# set headless_browser=True if you want to run InstaPy on a server
try:
    session = InstaPy(username=insta_username,
                      password=insta_password,
                      headless_browser=True,
                      nogui=True,
                      multi_logs=True)
    session.login()

    # settings
    session.set_do_comment(True, percentage=50)
    session.set_comments(['aMEIzing!', 'So much fun!!', 'Nicey!'])
    session.set_do_follow(enabled=True, percentage=50, times=2)

    # actions
    session.like_by_tags(['natgeo'], amount=4)

finally:
    # end the bot session
    session.end()
