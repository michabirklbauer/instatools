#!/usr/bin/env python3

# INSTATOOLS
# 2020 (c) Micha Johannes Birklbauer
# https://github.com/t0xic-m/
# micha.birklbauer@gmail.com

from getMedia import getMedia
import urllib.request as ur
import json

name = "InstaTools"
version = "1.1.0"

def getUserID(username):
    url = "https://www.instagram.com/" + str(username) + "/?__a=1"

    try:
        data = ur.urlopen(url).read()
    except Exception as e:
        print("ERROR reading page!")
        print(e)
        return -1
    try:
        json_data = json.loads(data)
    except Exception as e:
        print("ERROR loading json!")
        print(e)
        return -1

    try:
        return int(json_data["graphql"]["user"]["id"])
    except Exception as e:
        print("ERROR fetching id from json!")
        print(e)
        return -1

def getBiography(username):
    url = "https://www.instagram.com/" + str(username) + "/?__a=1"

    try:
        data = ur.urlopen(url).read()
    except Exception as e:
        print("ERROR reading page!")
        print(e)
        return -1
    try:
        json_data = json.loads(data)
    except Exception as e:
        print("ERROR loading json!")
        print(e)
        return -1

    try:
        return str(json_data["graphql"]["user"]["biography"])
    except Exception as e:
        print("ERROR fetching biography from json!")
        print(e)
        return -1

def getFollowerCount(username):
    url = "https://www.instagram.com/" + str(username) + "/?__a=1"

    try:
        data = ur.urlopen(url).read()
    except Exception as e:
        print("ERROR reading page!")
        print(e)
        return -1
    try:
        json_data = json.loads(data)
    except Exception as e:
        print("ERROR loading json!")
        print(e)
        return -1

    try:
        return int(json_data["graphql"]["user"]["edge_followed_by"]["count"])
    except Exception as e:
        print("ERROR fetching follower count from json!")
        print(e)
        return -1

def getFollowingCount(username):
    url = "https://www.instagram.com/" + str(username) + "/?__a=1"

    try:
        data = ur.urlopen(url).read()
    except Exception as e:
        print("ERROR reading page!")
        print(e)
        return -1
    try:
        json_data = json.loads(data)
    except Exception as e:
        print("ERROR loading json!")
        print(e)
        return -1

    try:
        return int(json_data["graphql"]["user"]["edge_follow"]["count"])
    except Exception as e:
        print("ERROR fetching following count from json!")
        print(e)
        return -1

def getMediaCount(username):
    url = "https://www.instagram.com/" + str(username) + "/?__a=1"

    try:
        data = ur.urlopen(url).read()
    except Exception as e:
        print("ERROR reading page!")
        print(e)
        return -1
    try:
        json_data = json.loads(data)
    except Exception as e:
        print("ERROR loading json!")
        print(e)
        return -1

    try:
        return int(json_data["graphql"]["user"]["edge_owner_to_timeline_media"]["count"])
    except Exception as e:
        print("ERROR fetching media count from json!")
        print(e)
        return -1

def getFullName(username):
    url = "https://www.instagram.com/" + str(username) + "/?__a=1"

    try:
        data = ur.urlopen(url).read()
    except Exception as e:
        print("ERROR reading page!")
        print(e)
        return -1
    try:
        json_data = json.loads(data)
    except Exception as e:
        print("ERROR loading json!")
        print(e)
        return -1

    try:
        return str(json_data["graphql"]["user"]["full_name"])
    except Exception as e:
        print("ERROR fetching full name from json!")
        print(e)
        return -1

def getProfilePic(username, download = False):
    url = "https://www.instagram.com/" + str(username) + "/?__a=1"

    try:
        data = ur.urlopen(url).read()
    except Exception as e:
        print("ERROR reading page!")
        print(e)
        return -1
    try:
        json_data = json.loads(data)
    except Exception as e:
        print("ERROR loading json!")
        print(e)
        return -1

    try:
        profile_pic_url = json_data["graphql"]["user"]["profile_pic_url_hd"]
    except Exception as e:
        print("ERROR fetching profile picture url from json!")
        print(e)
        return -1

    if download:
        try:
            save_path = "" + str(profile_pic_url).split("/")[-1].split("?")[0]
            ur.urlretrieve(str(profile_pic_url), save_path)
        except Exception as e:
            print("ERROR downloading profile picture!")
            print(e)

    return str(profile_pic_url)

def getNewPost(username, download = False):
    url = "https://www.instagram.com/" + str(username) + "/?__a=1"

    try:
        data = ur.urlopen(url).read()
    except Exception as e:
        print("ERROR reading page!")
        print(e)
        return -1
    try:
        json_data = json.loads(data)
    except Exception as e:
        print("ERROR loading json!")
        print(e)
        return -1

    try:
        shortcode = json_data["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"][0]["node"]["shortcode"]
    except Exception as e:
        print("ERROR extracting post shortcode from json!")
        print(e)
        return -1

    try:
        post_page = "https://instagram.com/p/" + str(shortcode)
        post_pics = getMedia(post_page, download = download)
        if post_pics != -1:
            post_details = [post_page] + post_pics
            return post_details
        else:
            print("ERROR in getMedia() - ERROR retrieving post media!")
            return -1
    except Exception as e:
        print("ERROR retrieving post media!")
        print(e)
        return -1

def getNewIGTV(username, download = False):
    url = "https://www.instagram.com/" + str(username) + "/?__a=1"

    try:
        data = ur.urlopen(url).read()
    except Exception as e:
        print("ERROR reading page!")
        print(e)
        return -1
    try:
        json_data = json.loads(data)
    except Exception as e:
        print("ERROR loading json!")
        print(e)
        return -1

    try:
        count = json_data["graphql"]["user"]["edge_felix_video_timeline"]["count"]
        shortcode = json_data["graphql"]["user"]["edge_felix_video_timeline"]["edges"][0]["node"]["shortcode"]
    except Exception as e:
        print("ERROR fetching data from json!")
        print(e)
        return -1

    igtv_page = "https://instagram.com/p/" + str(shortcode)
    igtv_nr = "Number of IGTV posts: " + str(count)
    try:
        post_igtv = getMedia(igtv_page, download = download)
        if post_igtv != -1:
            post_details = [igtv_nr] + [igtv_page] + post_igtv
            return post_details
        else:
            print("ERROR in getMedia() - ERROR retrieving IGTV media!")
            return -1
    except Exception as e:
        print("ERROR retrieving IGTV media!")
        print(e)
        return -1

def getTagged(username):
    tagged_page = "https://instagram.com/" + username + "/tagged/"
    return tagged_page

def isPostPrivate(instagram_post_url):
    url = str(instagram_post_url)
    shortcode = str(url.split("instagram.com/p/")[1]).split("/")[0]
    return len(shortcode) > 12

def isProfilePrivate(username):
    url = "https://www.instagram.com/" + str(username) + "/?__a=1"

    try:
        data = ur.urlopen(url).read()
    except Exception as e:
        print("ERROR reading page!")
        print(e)
        return -1
    try:
        json_data = json.loads(data)
    except Exception as e:
        print("ERROR loading json!")
        print(e)
        return -1

    try:
        return bool(json_data["graphql"]["user"]["is_private"])
    except Exception as e:
        print("ERROR fetching private status from json!")
        print(e)
        return -1

def isProfileBusiness(username):
    url = "https://www.instagram.com/" + str(username) + "/?__a=1"

    try:
        data = ur.urlopen(url).read()
    except Exception as e:
        print("ERROR reading page!")
        print(e)
        return -1
    try:
        json_data = json.loads(data)
    except Exception as e:
        print("ERROR loading json!")
        print(e)
        return -1

    try:
        return bool(json_data["graphql"]["user"]["is_business_account"])
    except Exception as e:
        print("ERROR fetching business status from json!")
        print(e)
        return -1

def isProfileVerified(username):
    url = "https://www.instagram.com/" + str(username) + "/?__a=1"

    try:
        data = ur.urlopen(url).read()
    except Exception as e:
        print("ERROR reading page!")
        print(e)
        return -1
    try:
        json_data = json.loads(data)
    except Exception as e:
        print("ERROR loading json!")
        print(e)
        return -1

    try:
        return bool(json_data["graphql"]["user"]["is_verified"])
    except Exception as e:
        print("ERROR fetching verified status from json!")
        print(e)
        return -1

def getPostDetails(instagram_post_url):

    shortcode = instagram_post_url.split("/p/")[1].split("/")[0]
    url = "https://instagram.com/p/" + shortcode + "/?__a=1"

    try:
        post_data = ur.urlopen(url).read()
        post_json = json.loads(post_data)
        return [url, post_data, post_json]
    except Exception as e:
        print("ERROR fetching post!")
        print(e)
        return -1

def getStories(username, download = False):

    raise NotImplementedError()
    # basically this doesn't work at the moment
    url = "https://storiesig.com/stories/" + str(username)

    try:
        page = ur.urlopen(url).read().decode("utf-8")
    except Exception as e:
        print("ERROR fetching stories!")
        print(e)
        return -1

    lines = page.splitlines()

    data = ""

    media_links = []

    for line in lines:
        if "__NEXT_DATA__" in line:
            data = line.replace("__NEXT_DATA__ = ", "").lstrip().rstrip()

    if data == "":
        print("ERROR fetching json!")
        return -1
    else:
        try:
            json_data = json.loads(data)
            stories = json_data["props"]["pageProps"]["stories"]["items"]
        except Exception as e:
            print("ERROR loading json!")
            print(e)
            return -1
        if len(stories) == 0:
            print("No stories for username ", username)
            return media_links
        else:
            for story in stories:
                try:
                    original_width = story["original_width"]
                    original_height = story["original_height"]
                    media_type = int(story["media_type"])
                    for entry in story["image_versions2"]["candidates"]:
                        if entry["width"] == original_width and entry["height"] == original_height:
                            media_links.append(str(entry["url"]))
                            if download:
                                s_path = "" + str(entry["url"]).split("/")[-1].split("?")[0]
                                ur.urlretrieve(str(entry["url"]), s_path)
                    max_height = 0
                    max_counter = 0
                    i = 0
                    if media_type == 2:
                        for entry in story["video_versions"]:
                            if int(entry["height"]) >= max_height:
                                max_height = int(entry["height"])
                                max_counter = i
                            i = i + 1
                        media_links.append(str(story["video_versions"][max_counter]["url"]))
                        if download:
                            s_path = "" + str(story["video_versions"][max_counter]["url"]).split("/")[-1].split("?")[0]
                            ur.urlretrieve(str(story["video_versions"][max_counter]["url"]), s_path)
                    return media_links
                except Exception as e:
                    print("ERROR retrieving stories!")
                    print(e)
                    return -1
