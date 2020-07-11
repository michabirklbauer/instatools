#!/usr/bin/env python3

# INSTATOOLS - getMedia
# 2020 (c) Micha Johannes Birklbauer
# https://github.com/t0xic-m/
# micha.birklbauer@gmail.com

import urllib.request as ur
import json

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
            error_msg = "Error: Failed to extract image from link: " + insta_url
            print(error_msg)
            print(e)
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
                error_msg = "Error: Failed to extract image from link: " + insta_url
                print(error_msg)
                print(e)
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
            error_msg = "Error: Failed to extract video from link: " + insta_url
            print(error_msg)
            print(e)
            result.append(video_link)
            result.insert(0, 1)
            return result

    insta_url_api = str(instagram_post_url).rstrip("/") + "/?__a=1"
    data = ur.urlopen(insta_url_api).read()

    try:
        json_data = json.loads(data)
    except Exception as e:
        print("Error: Failed to load json data!")
        print(e)
        return -1

    try:
        media_type = str(json_data["graphql"]["shortcode_media"]["__typename"])
    except Exception as e:
        print("ERROR extracting media type!")
        print(e)
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
        return -1
