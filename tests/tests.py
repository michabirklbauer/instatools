#!/usr/bin/env python3

# INSTATOOLS - TESTS
# 2021 (c) Micha Johannes Birklbauer
# https://github.com/t0xic-m/
# micha.birklbauer@gmail.com

import InstaTools as it

def test_getUserID():
    assert it.getUserID("nasa") != -1

def test_getBiography():
    assert it.getBiography("nasa") != -1

def test_getFollowerCount():
    assert it.getFollowerCount("nasa") != -1

def test_getFollowingCount():
    assert it.getFollowingCount("nasa") != -1

def test_getMediaCount():
    assert it.getMediaCount("nasa") != -1

def test_getFullName():
    assert it.getFullName("nasa") != -1

def test_getProfilePic():
    assert it.getProfilePic("nasa", True) != -1

def test_getNewPost():
    assert it.getNewPost("nasa", True) != -1

def test_getNewIGTV():
    assert it.getNewIGTV("nasa", True) != -1

def test_getTagged():
    assert it.getTagged("nasa") == "https://www.instagram.com/nasa/tagged/"

def test_isPostPrivate():
    assert it.isPostPrivate("https://www.instagram.com/p/B3APlTmHktH/") == False

def test_isProfilePrivate():
    assert it.isProfilePrivate("nasa") != -1

def test_isProfileBusiness():
    assert it.isProfileBusiness("nasa") != -1

def test_isProfileVerified():
    assert it.isProfileVerified("nasa") != -1

def test_getPostDetails():
    assert it.getPostDetails("https://www.instagram.com/p/B3APlTmHktH/") != -1
