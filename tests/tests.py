#!/usr/bin/env python3

# INSTATOOLS - TESTS
# 2021 (c) Micha Johannes Birklbauer
# https://github.com/michabirklbauer/
# micha.birklbauer@gmail.com

import InstaTools as it

def test_basic():
    assert it.version == "1.1.1"

# ##############################################################################
# ##############################################################################
# ##                                                                          ##
# ##                          LOCAL DEBUG FUNCTIONS                           ##
# ##                                                                          ##
# ##############################################################################
# ##############################################################################
#
# import urllib.request as ur
# import time
#
# # basic debug function if site even loads json data
# def test_connection():
#     request_header = { "User-Agent" : "Mozilla/5.0 (Windows NT 6.1; Win64; x64)" }
#     request = ur.Request("https://instagram.com/nasa/?__a=1", headers=request_header)
#     data = ur.urlopen(request).read()
#     print(data)
#     assert len(data) == -1
#
# def test_getUserID():
#     time.sleep(2)
#     assert it.getUserID("nasa") != -1
#
# def test_getBiography():
#     time.sleep(2)
#     assert it.getBiography("nasa") != -1
#
# def test_getFollowerCount():
#     time.sleep(2)
#     assert it.getFollowerCount("nasa") != -1
#
# def test_getFollowingCount():
#     time.sleep(2)
#     assert it.getFollowingCount("nasa") != -1
#
# def test_getMediaCount():
#     time.sleep(2)
#     assert it.getMediaCount("nasa") != -1
#
# def test_getFullName():
#     time.sleep(2)
#     assert it.getFullName("nasa") != -1
#
# def test_getProfilePic():
#     time.sleep(2)
#     assert it.getProfilePic("nasa", True) != -1
#
# def test_getNewPost():
#     time.sleep(2)
#     assert it.getNewPost("nasa", True) != -1
#
# def test_getNewIGTV():
#     time.sleep(2)
#     assert it.getNewIGTV("nasa", True) != -1
#
# def test_getTagged():
#     time.sleep(2)
#     assert it.getTagged("nasa") == "https://instagram.com/nasa/tagged/"
#
# def test_isPostPrivate():
#     time.sleep(2)
#     assert it.isPostPrivate("https://www.instagram.com/p/B3APlTmHktH/") == False
#
# def test_isProfilePrivate():
#     time.sleep(2)
#     assert it.isProfilePrivate("nasa") != -1
#
# def test_isProfileBusiness():
#     time.sleep(2)
#     assert it.isProfileBusiness("nasa") != -1
#
# def test_isProfileVerified():
#     time.sleep(2)
#     assert it.isProfileVerified("nasa") != -1
#
# def test_getPostDetails():
#     time.sleep(2)
#     assert it.getPostDetails("https://www.instagram.com/p/B3APlTmHktH/") != -1
#
# def test_getMedia():
#     time.sleep(2)
#     assert it.getMedia("https://www.instagram.com/p/CKFNZXEJo3R/", True) != -1
