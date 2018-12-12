# InstaTools

A small python package to access and deal with Instagram data!

Sidenote: Yes, this is the follow-up to [InstaPython](https://github.com/t0xic-m/instapython)

# TL;DR

Head over to [InstaTools](https://t0xic-m.github.io/instatools)!

## Quick Start

Installation:

```bash
pip install Release/InstaTools-1.0.0.tar.gz
```

Import and Usage:

```python
import InstaTools
instagram = InstaTools.Instagram()
instagram.getUserID("katie_kosova")
262972296
````

## Classes and Functions

- ### Main Functions:

  These methods are available outside of specific classes:

  - #### name
    - description: Returns the package name
    - parameters: none (also no braces!)
    - returns: package_name (type: string)
  - #### gui()
    - description: Initiates a tkinter GUI with part of the functions provided by this package
    - parameters: none
    - returns: NULL

- ### Instagram

  Basic utility functions:

  - #### getUserID(user_name)
    - description: Retrieves user ID given a username
    - parameters: ```user_name``` (a valid and existing instagram username, type: string)
    - returns: ```user_id``` (the corresponding user ID \[or 1 in case of error\], type: integer)
  - #### getBiography(user_name)
    - description: Retrieves biography given a username
    - parameters: ```user_name``` (a valid and existing instagram username, type: string)
    - returns: ```biography``` (the corresponding biography \[or 1 in case of error\], type: string\[/integer\])
  - #### getFollwerCount(user_name)
    - description: Retrieves follower count given a username
    - parameters: ```user_name``` (a valid and existing instagram username, type: string)
    - returns: ```followers_count``` (the corresponding follower count \[or "1" in case of error\], type: integer\[/string\])
  - #### getFollwingCount(user_name)
    - description: Retrieves following count given a username
    - parameters: ```user_name``` (a valid and existing instagram username, type: string)
    - returns: ```following_count``` (the corresponding following count \[or "1" in case of error\], type: integer\[/string\])
  - #### getMediaCount(user_name)
    - description: Retrieves media count given a username
    - parameters: ```user_name``` (a valid and existing instagram username, type: string)
    - retunrs: ```media_count``` (the corresponding media count \[or "1" in case of error\], type: integer\[/string\])
  - #### getFullName(user_name)
    - description: Retrieves full name given a username
    - parameters: ```user_name``` (a valid and existing instagram username, type: string)
      - retunrs: ```full_name``` (the corresponding full name \[or 1 in case of error\], type: string\[/integer\])
  - #### getProfilePic(user_name, download = False)
    - description: Retrieves profile picture URL given a username
    - parameters: ```user_id``` (a valid and existing instagram username, type: string)
    - parameters: ```download``` (wether or not profile picture should be downloaded, type: boolean, default: False)
    - returns: ```profile_pic_url``` (direct link to the corresponding profile picture \[or 1 in case of error\], type: string\[/integer\])
  - #### getNewPost(user_name, download = False)
    - description: Retrieves most recent post given a username
    - parameters: ```user_name``` (a valid and existing instagram username, type: string)
    - parameters: ```download``` (wether or not newest post should be downloaded, type: boolean, default: False)
    - returns: ```[post_page, post_pic(s)]``` (links to 1) the page of the most recent post and 2) the picture(s), type: list of strings)
  - #### getNewIGTV(user_name, download = False)
    - description: Retrieves most recent IGTV post given a username
    - parameters: ```user_name``` (a valid and existing instagram username, type: string)
    - parameters: ```download``` (wether or not newest IGTV post should be downloaded, type: boolean, default: False)
    - returns: ```[igtv_nr, post_page, post_pic(s)]``` (1) Number IGTV posts, links to 2) the page of the most recent post and 3) the picture(s), type: list of strings)
  - #### getTagged(user_name)
    - description: Retrieves the URL to the user's tagged posts
    - parameters: ```user_name``` (a valid and existing instagram username, type: string)
    - returns: ```tagged_page``` (link to user's tagged page, type: string)
  - #### isPrivate(instagram_post_url)
    - description: Retrieves private status given an URL to an instagram post
    - parameters: ```instagram_post_url``` (a valid link to an existing instagram post, type: string)
    - returns: True/False (status, type: boolean)
  - #### isProfilePrivate(user_name)
    - description: Retrieves private status of an instagram profile given a username
    - parameters: ```user_name``` (a valid and existing instagram user ID, type: string)
    - returns: True/False (private status \[or 1 in case of error\], type: boolean\[/integer\])
  - #### isProfileBusiness(user_name)
    - description: Retrieves business status of an instagram profile given a username
    - parameters: ```user_name``` (a valid and existing instagram user ID, type: string)
    - returns: True/False (business status \[or 1 in case of error\], type: boolean\[/integer\])
  - #### isProfileVerified(user_name)
    - description: Retrieves verified status of an instagram profile given a username
    - parameters: ```user_name``` (a valid and existing instagram user ID, type: string)
    - returns: True/False (verified status \[or 1 in case of error\], type: boolean\[/integer\])
  - #### getPostDetails(instagram_post_url)
    - description: Retrieves post details via the Instagram API
    - parameters: ```instagram_post_url``` (a valid link to an existing instagram post, type: string)
    - returns: ```[url, post_data, post_json]``` (a list containing 1) URL to the retrieved page, type: string; 2) the json data in string format, type: string; 3) the json data as a json object, type: json)
  - #### getMedia(instagram_post_url, download)
    - description: Retrieves download links to media given an instagram post URL
    - parameters: ```instagram_post_url``` (a valid link to an existing instagram post, type: string)
    - parameters: ```download``` (if media should be downloaded or not, type: boolean, default: False)
    - returns: ```media_links = []``` (a list of media links, type: list of strings)
  - #### getMediaSafe(instagram_post_url, download)
    - description: Retrieves download links to media given an instagram post URL but in a more safe way than the traditional method (slower)
    - parameters: ```instagram_post_url``` (a valid link to an existing instagram post, type: string)
    - parameters: ```download``` (if media should be downloaded or not, type: boolean, default: False)
    - returns: ```media_links = []``` (a list of media links, type: list of strings)
  - #### getStories(user_name, download)
    - description: Retrieves download links to stories given a username
    - parameters: ```user_name``` (a valid and existing instagram username, type: string)
    - parameters: ```download``` (if media should be downloaded or not, type: boolean, default: False)
    - returns: ```media_links = []``` (a list of media links, type: list of strings)

- ### InstaLoad

  Download media functions:

  - #### instaload(instagram_post_url)
    - description: Downloads media from an instagram post
    - parameters: ```instagram_post_url``` (a valid link to an existing instagram post, type: string)
    - returns: NULL (Media is downloaded to working directory)
  - #### isPrivate(instagram_post_url)
    - description: Retrieves private status given an URL to an instagram post
    - parameters: ```instagram_post_url``` (a valid link to an existing instagram post, type: string)
    - returns: True/False (status, type: boolean)
  - #### multiload(file_name)
    - description: Download multiple posts via a file containing links (see [Example](https://raw.githubusercontent.com/t0xic-m/instagram_downloader/master/links.txt))
    - parameters: ```file_name``` (filename or path to file that contains the links, type: string)
    - returns: NULL

- ### InstaBot

  Watchdog functions:

  - #### Constructor Options - InstaBot(path_to_config_file, channel, api_token):
    - ```path_to_config_file``` (path were configuration data should be stored, type: string)
    - ```channel``` (a telegram channel name or ID, type: string)
    - ```api_token``` (telegram bot api token, type: string)

  - #### instaBot(user_ids, rtime, stime, daily = False, debugging_mode = True)
    - description: A bot that watches instagram profiles and sends notifications to a telegram channel
    - parameters: ```user_names``` (a list of valid and existing usernames, type: list of strings)
    - parameters: ```rtime``` (time in seconds that specifies how long the bot should run, if set to 0 it will run forever, type: integer, default: 3480)
    - parameters: ```stime``` (time in hours that specifies when story alerts should be sent, type: integer, default: 21)
    - parameters: ```daily``` (if stories should be sent daily or every 12 hours, type: boolean, default: False - Stories are sent every 12 hours)
    - parameters: ```debugging_mode``` (if control and status messages should be sent to the telegram channel, type: boolean, default: True)
    - returns: NULL

- ### InstaView

  Main Repository:
  - [Instagram_Data_Download_Viewer](https://github.com/t0xic-m/instagram_data_download_viewer)

  Viewer functions:

  - #### createRMD(path)
    - description: Creates an R Markdown file from several json files and tries knitting it to PDF
    - parameters: ```path``` (path to the json-files-directory, type: string, default: current directory)
    - returns: NULL (creates RMD in specified directory)  

## License

[MIT License](https://github.com/t0xic-m/instatools/blob/master/LICENSE.md)

## Contact

- Website: [Web](https://t0xic-m.github.io/web)
- Website: [GitHub](https://t0xic-m.github.io)
- Mail: [Contact](mailto:micha.birklbauer@gmail.com)
