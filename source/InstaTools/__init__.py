#!/usr/bin/env python3

# INSTATOOLS
# 2021 (c) Micha Johannes Birklbauer
# https://github.com/t0xic-m/
# micha.birklbauer@gmail.com

import urllib.request as ur
import traceback as tb
import json

name = "InstaTools"
version = "1.1.1"

def getMedia(instagram_post_url, download = False):

    def get_image(json_data, download = download, prefix = ""):
        dimensions_h = int(json_data["dimensions"]["height"])
        dimensions_w = int(json_data["dimensions"]["width"])
        display_resources = json_data["display_resources"]
        image_src = ""
        image_display = ""
        for resource in display_resources:
            if int(resource["config_height"])==dimensions_h and int(resource["config_width"])==dimensions_w:
                image_src = str(resource["src"])
                break
        try:
            image_display = str(json_data["display_url"])
        except Exception as e:
            print("Error: Failed to extract image from display_url!")
            print(e)
            print("Full error traceback:")
            tb.print_exc()
            image_display = ""
        if image_display == image_src:
            image = image_display
        else:
            if image_src == "" and image_display != "":
                print("Warning: image_src and image_display not the same!")
                print("image_src is NULL")
                print("Getting display_url!")
                image = image_display
            elif image_src != "" and image_display == "":
                print("Warning: image_src and image_display not the same!")
                print("image_display is NULL")
                print("Getting display_resources!")
                image = image_src
            else:
                print("Warning: image_src and image_display not the same!")
                print("image_src: \n" + image_src)
                print("image_display: \n" + image_display)
                print("Default: Getting display_url!")
                image = image_display
        if image == "":
            print("Error: Failed to extract image!")
            return [1]
        image_link = image.replace("\\", "")
        try:
            file_name = prefix + "_" + str(image_link).split("/")[-1].split("?")[0]
            if download:
                ur.urlretrieve(str(image_link), file_name)
                print("Successfully extracted and downloaded image!")
            return [0, image_link]
        except Exception as e:
            error_msg = "Error: Failed to extract image from link: " + instagram_post_url
            print(error_msg)
            print(e)
            print("Full error traceback:")
            tb.print_exc()
            return [1, image_link]

    def get_video(json_data, download = download, prefix = ""):
        dimensions_h = int(json_data["dimensions"]["height"])
        dimensions_w = int(json_data["dimensions"]["width"])
        display_resources = json_data["display_resources"]
        image_src = ""
        image_display = ""
        result = []
        for resource in display_resources:
            if int(resource["config_height"])==dimensions_h and int(resource["config_width"])==dimensions_w:
                image_src = str(resource["src"])
                break
        try:
            image_display = str(json_data["display_url"])
        except Exception as e:
            print("Error: Failed to extract image from display_url!")
            print(e)
            print("Full error traceback:")
            tb.print_exc()
            image_display = ""
        if image_display == image_src:
            image = image_display
        else:
            if image_src == "" and image_display != "":
                print("Warning: image_src and image_display not the same!")
                print("image_src is NULL")
                print("Getting display_url!")
                image = image_display
            elif image_src != "" and image_display == "":
                print("Warning: image_src and image_display not the same!")
                print("image_display is NULL")
                print("Getting display_resources!")
                image = image_src
            else:
                print("Warning: image_src and image_display not the same!")
                print("image_src: \n" + image_src)
                print("image_display: \n" + image_display)
                print("Default: Getting display_url!")
                image = image_display
        if image == "":
            print("Error: Failed to extract image!")
            print("Trying to get video!")
        else:
            image_link = image.replace("\\", "")
            try:
                file_name = prefix + "_" + str(image_link).split("/")[-1].split("?")[0]
                if download:
                    ur.urlretrieve(str(image_link), file_name)
                    print("Successfully extracted and downloaded image!")
                result.append(image_link)
            except Exception as e:
                error_msg = "Error: Failed to extract image from link: " + instagram_post_url
                print(error_msg)
                print(e)
                print("Full error traceback:")
                tb.print_exc()
                print("Trying to get video!")
                result.append("no image")
        video = str(json_data["video_url"])
        video_link = video.replace("\\", "")
        try:
            file_name = prefix + "_" + str(video_link).split("/")[-1].split("?")[0]
            if download:
                ur.urlretrieve(str(video_link), file_name)
                print("Successfully extracted and downloaded video!")
            result.append(video_link)
            result.insert(0, 0)
            return result
        except Exception as e:
            error_msg = "Error: Failed to extract video from link: " + instagram_post_url
            print(error_msg)
            print(e)
            print("Full error traceback:")
            tb.print_exc()
            result.append(video_link)
            result.insert(0, 1)
            return result

    insta_url_api = str(instagram_post_url).rstrip("/") + "/?__a=1"
    request_header = { "User-Agent" : "Mozilla/5.0 (Windows NT 6.1; Win64; x64)" }
    request = ur.Request(insta_url_api, headers=request_header)
    data = ur.urlopen(request).read()

    try:
        json_data = json.loads(data)
    except Exception as e:
        print("Error: Failed to load json data!")
        print(e)
        print("Full error traceback:")
        tb.print_exc()
        return -1

    try:
        media_type = str(json_data["graphql"]["shortcode_media"]["__typename"])
    except Exception as e:
        print("ERROR extracting media type!")
        print(e)
        print("Full error traceback:")
        tb.print_exc()
        return -1

    try:
        if media_type == "GraphImage":
            r = get_image(json_data["graphql"]["shortcode_media"], download = download)
            if r[0] == 0:
                return r[1:]
            else:
                return -1
        elif media_type == "GraphVideo":
            prefix = str(json_data["graphql"]["shortcode_media"]["shortcode"])
            r = get_video(json_data["graphql"]["shortcode_media"], download = download, prefix = prefix)
            if r[0] == 0:
                return r[1:]
            else:
                return -1
        elif media_type == "GraphSidecar":
            sideshow_result = []
            prefix = str(json_data["graphql"]["shortcode_media"]["shortcode"])
            edges = json_data["graphql"]["shortcode_media"]["edge_sidecar_to_children"]["edges"]
            r = 0
            for edge in edges:
                if str(edge["node"]["__typename"]) == "GraphImage":
                    r_ = get_image(edge["node"], download = download, prefix = prefix)
                elif str(edge["node"]["__typename"]) == "GraphVideo":
                    r_ = get_video(edge["node"], download = download, prefix = prefix)
                else:
                    print("Error: Unrecognized typename!")
                    return -1
                if r_[0] == 0:
                    sideshow_result.append(r_[1:])
                else:
                    r = 1
            if r == 0:
                return sideshow_result
            else:
                print("ERROR retrieving media from slideshow!")
                return -1
        else:
            print("Error: Unrecognized typename!")
            return -1
    except Exception as e:
        print("ERROR extracting media!")
        print(e)
        print("Full error traceback:")
        tb.print_exc()
        return -1

def getUserID(username):
    url = "https://www.instagram.com/" + str(username) + "/?__a=1"

    try:
        request_header = { "User-Agent" : "Mozilla/5.0 (Windows NT 6.1; Win64; x64)" }
        request = ur.Request(url, headers=request_header)
        data = ur.urlopen(request).read()
    except Exception as e:
        print("ERROR reading page!")
        print(e)
        print("Full error traceback:")
        tb.print_exc()
        return -1
    try:
        json_data = json.loads(data)
    except Exception as e:
        print("ERROR loading json!")
        print(e)
        print("Full error traceback:")
        tb.print_exc()
        return -1

    try:
        return int(json_data["graphql"]["user"]["id"])
    except Exception as e:
        print("ERROR fetching id from json!")
        print(e)
        print("Full error traceback:")
        tb.print_exc()
        return -1

def getBiography(username):
    url = "https://www.instagram.com/" + str(username) + "/?__a=1"

    try:
        request_header = { "User-Agent" : "Mozilla/5.0 (Windows NT 6.1; Win64; x64)" }
        request = ur.Request(url, headers=request_header)
        data = ur.urlopen(request).read()
    except Exception as e:
        print("ERROR reading page!")
        print(e)
        print("Full error traceback:")
        tb.print_exc()
        return -1
    try:
        json_data = json.loads(data)
    except Exception as e:
        print("ERROR loading json!")
        print(e)
        print("Full error traceback:")
        tb.print_exc()
        return -1

    try:
        return str(json_data["graphql"]["user"]["biography"])
    except Exception as e:
        print("ERROR fetching biography from json!")
        print(e)
        print("Full error traceback:")
        tb.print_exc()
        return -1

def getFollowerCount(username):
    url = "https://www.instagram.com/" + str(username) + "/?__a=1"

    try:
        request_header = { "User-Agent" : "Mozilla/5.0 (Windows NT 6.1; Win64; x64)" }
        request = ur.Request(url, headers=request_header)
        data = ur.urlopen(request).read()
    except Exception as e:
        print("ERROR reading page!")
        print(e)
        print("Full error traceback:")
        tb.print_exc()
        return -1
    try:
        json_data = json.loads(data)
    except Exception as e:
        print("ERROR loading json!")
        print(e)
        print("Full error traceback:")
        tb.print_exc()
        return -1

    try:
        return int(json_data["graphql"]["user"]["edge_followed_by"]["count"])
    except Exception as e:
        print("ERROR fetching follower count from json!")
        print(e)
        print("Full error traceback:")
        tb.print_exc()
        return -1

def getFollowingCount(username):
    url = "https://www.instagram.com/" + str(username) + "/?__a=1"

    try:
        request_header = { "User-Agent" : "Mozilla/5.0 (Windows NT 6.1; Win64; x64)" }
        request = ur.Request(url, headers=request_header)
        data = ur.urlopen(request).read()
    except Exception as e:
        print("ERROR reading page!")
        print(e)
        print("Full error traceback:")
        tb.print_exc()
        return -1
    try:
        json_data = json.loads(data)
    except Exception as e:
        print("ERROR loading json!")
        print(e)
        print("Full error traceback:")
        tb.print_exc()
        return -1

    try:
        return int(json_data["graphql"]["user"]["edge_follow"]["count"])
    except Exception as e:
        print("ERROR fetching following count from json!")
        print(e)
        print("Full error traceback:")
        tb.print_exc()
        return -1

def getMediaCount(username):
    url = "https://www.instagram.com/" + str(username) + "/?__a=1"

    try:
        request_header = { "User-Agent" : "Mozilla/5.0 (Windows NT 6.1; Win64; x64)" }
        request = ur.Request(url, headers=request_header)
        data = ur.urlopen(request).read()
    except Exception as e:
        print("ERROR reading page!")
        print(e)
        print("Full error traceback:")
        tb.print_exc()
        return -1
    try:
        json_data = json.loads(data)
    except Exception as e:
        print("ERROR loading json!")
        print(e)
        print("Full error traceback:")
        tb.print_exc()
        return -1

    try:
        return int(json_data["graphql"]["user"]["edge_owner_to_timeline_media"]["count"])
    except Exception as e:
        print("ERROR fetching media count from json!")
        print(e)
        print("Full error traceback:")
        tb.print_exc()
        return -1

def getFullName(username):
    url = "https://www.instagram.com/" + str(username) + "/?__a=1"

    try:
        request_header = { "User-Agent" : "Mozilla/5.0 (Windows NT 6.1; Win64; x64)" }
        request = ur.Request(url, headers=request_header)
        data = ur.urlopen(request).read()
    except Exception as e:
        print("ERROR reading page!")
        print(e)
        print("Full error traceback:")
        tb.print_exc()
        return -1
    try:
        json_data = json.loads(data)
    except Exception as e:
        print("ERROR loading json!")
        print(e)
        print("Full error traceback:")
        tb.print_exc()
        return -1

    try:
        return str(json_data["graphql"]["user"]["full_name"])
    except Exception as e:
        print("ERROR fetching full name from json!")
        print(e)
        print("Full error traceback:")
        tb.print_exc()
        return -1

def getProfilePic(username, download = False):
    url = "https://www.instagram.com/" + str(username) + "/?__a=1"

    try:
        request_header = { "User-Agent" : "Mozilla/5.0 (Windows NT 6.1; Win64; x64)" }
        request = ur.Request(url, headers=request_header)
        data = ur.urlopen(request).read()
    except Exception as e:
        print("ERROR reading page!")
        print(e)
        print("Full error traceback:")
        tb.print_exc()
        return -1
    try:
        json_data = json.loads(data)
    except Exception as e:
        print("ERROR loading json!")
        print(e)
        print("Full error traceback:")
        tb.print_exc()
        return -1

    try:
        profile_pic_url = json_data["graphql"]["user"]["profile_pic_url_hd"]
    except Exception as e:
        print("ERROR fetching profile picture url from json!")
        print(e)
        print("Full error traceback:")
        tb.print_exc()
        return -1

    if download:
        try:
            save_path = "" + str(profile_pic_url).split("/")[-1].split("?")[0]
            ur.urlretrieve(str(profile_pic_url), save_path)
        except Exception as e:
            print("ERROR downloading profile picture!")
            print(e)
            print("Full error traceback:")
            tb.print_exc()

    return str(profile_pic_url)

def getNewPost(username, download = False):
    url = "https://www.instagram.com/" + str(username) + "/?__a=1"

    try:
        request_header = { "User-Agent" : "Mozilla/5.0 (Windows NT 6.1; Win64; x64)" }
        request = ur.Request(url, headers=request_header)
        data = ur.urlopen(request).read()
    except Exception as e:
        print("ERROR reading page!")
        print(e)
        print("Full error traceback:")
        tb.print_exc()
        return -1
    try:
        json_data = json.loads(data)
    except Exception as e:
        print("ERROR loading json!")
        print(e)
        print("Full error traceback:")
        tb.print_exc()
        return -1

    try:
        shortcode = json_data["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"][0]["node"]["shortcode"]
    except Exception as e:
        print("ERROR extracting post shortcode from json!")
        print(e)
        print("Full error traceback:")
        tb.print_exc()
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
        print("Full error traceback:")
        tb.print_exc()
        return -1

def getNewIGTV(username, download = False):
    url = "https://www.instagram.com/" + str(username) + "/?__a=1"

    try:
        request_header = { "User-Agent" : "Mozilla/5.0 (Windows NT 6.1; Win64; x64)" }
        request = ur.Request(url, headers=request_header)
        data = ur.urlopen(request).read()
    except Exception as e:
        print("ERROR reading page!")
        print(e)
        print("Full error traceback:")
        tb.print_exc()
        return -1
    try:
        json_data = json.loads(data)
    except Exception as e:
        print("ERROR loading json!")
        print(e)
        print("Full error traceback:")
        tb.print_exc()
        return -1

    try:
        count = json_data["graphql"]["user"]["edge_felix_video_timeline"]["count"]
        shortcode = json_data["graphql"]["user"]["edge_felix_video_timeline"]["edges"][0]["node"]["shortcode"]
    except Exception as e:
        print("ERROR fetching data from json!")
        print(e)
        print("Full error traceback:")
        tb.print_exc()
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
        print("Full error traceback:")
        tb.print_exc()
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
        request_header = { "User-Agent" : "Mozilla/5.0 (Windows NT 6.1; Win64; x64)" }
        request = ur.Request(url, headers=request_header)
        data = ur.urlopen(request).read()
    except Exception as e:
        print("ERROR reading page!")
        print(e)
        print("Full error traceback:")
        tb.print_exc()
        return -1
    try:
        json_data = json.loads(data)
    except Exception as e:
        print("ERROR loading json!")
        print(e)
        print("Full error traceback:")
        tb.print_exc()
        return -1

    try:
        return bool(json_data["graphql"]["user"]["is_private"])
    except Exception as e:
        print("ERROR fetching private status from json!")
        print(e)
        print("Full error traceback:")
        tb.print_exc()
        return -1

def isProfileBusiness(username):
    url = "https://www.instagram.com/" + str(username) + "/?__a=1"

    try:
        request_header = { "User-Agent" : "Mozilla/5.0 (Windows NT 6.1; Win64; x64)" }
        request = ur.Request(url, headers=request_header)
        data = ur.urlopen(request).read()
    except Exception as e:
        print("ERROR reading page!")
        print(e)
        print("Full error traceback:")
        tb.print_exc()
        return -1
    try:
        json_data = json.loads(data)
    except Exception as e:
        print("ERROR loading json!")
        print(e)
        print("Full error traceback:")
        tb.print_exc()
        return -1

    try:
        return bool(json_data["graphql"]["user"]["is_business_account"])
    except Exception as e:
        print("ERROR fetching business status from json!")
        print(e)
        print("Full error traceback:")
        tb.print_exc()
        return -1

def isProfileVerified(username):
    url = "https://www.instagram.com/" + str(username) + "/?__a=1"

    try:
        request_header = { "User-Agent" : "Mozilla/5.0 (Windows NT 6.1; Win64; x64)" }
        request = ur.Request(url, headers=request_header)
        data = ur.urlopen(request).read()
    except Exception as e:
        print("ERROR reading page!")
        print(e)
        print("Full error traceback:")
        tb.print_exc()
        return -1
    try:
        json_data = json.loads(data)
    except Exception as e:
        print("ERROR loading json!")
        print(e)
        print("Full error traceback:")
        tb.print_exc()
        return -1

    try:
        return bool(json_data["graphql"]["user"]["is_verified"])
    except Exception as e:
        print("ERROR fetching verified status from json!")
        print(e)
        print("Full error traceback:")
        tb.print_exc()
        return -1

def getPostDetails(instagram_post_url):

    shortcode = instagram_post_url.split("/p/")[1].split("/")[0]
    url = "https://instagram.com/p/" + shortcode + "/?__a=1"

    try:
        request_header = { "User-Agent" : "Mozilla/5.0 (Windows NT 6.1; Win64; x64)" }
        request = ur.Request(url, headers=request_header)
        post_data = ur.urlopen(request).read()
        post_json = json.loads(post_data)
        return [url, post_data, post_json]
    except Exception as e:
        print("ERROR fetching post!")
        print(e)
        print("Full error traceback:")
        tb.print_exc()
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
