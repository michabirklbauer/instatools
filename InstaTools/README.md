# InstaTools by Micha Birklbauer

A small python package to access and deal with Instagram data!

## Quick Start

Installation:

```bash
pip install Release/InstaTools-1.1.0.tar.gz
```

Import and Usage:

```python
import InstaTools as it
it.getUserID("micha_birklbauer")
8460770171
````

## Functions

- #### name
  - description: Returns the package name.
  - parameters: none
  - returns: package name (type: string)
- #### version
  - description: Returns package version.
  - parameters: none
  - returns: package version (type: string)
- #### getUserID(username)
  - description: Retrieves user ID given a username.
  - parameters: ```username``` (a valid and existing instagram username, type: string)
  - returns: ```user_id``` (the corresponding user ID \[or -1 in case of error\], type: integer)
- #### getBiography(username)
  - description: Retrieves biography given a username.
  - parameters: ```username``` (a valid and existing instagram username, type: string)
  - returns: ```biography``` (the corresponding biography \[or -1 in case of error\], type: string)
- #### getFollwerCount(username)
  - description: Retrieves follower count given a username.
  - parameters: ```username``` (a valid and existing instagram username, type: string)
  - returns: ```follower_count``` (the corresponding follower count \[or -1 in case of error\], type: integer)
- #### getFollwingCount(username)
  - description: Retrieves following count given a username.
  - parameters: ```username``` (a valid and existing instagram username, type: string)
  - returns: ```following_count``` (the corresponding following count \[or -1 in case of error\], type: integer)
- #### getMediaCount(username)
  - description: Retrieves media count given a username.
  - parameters: ```username``` (a valid and existing instagram username, type: string)
  - returns: ```media_count``` (the corresponding media count \[or -1 in case of error\], type: integer)
- #### getFullName(username)
  - description: Retrieves full name given a username.
  - parameters: ```username``` (a valid and existing instagram username, type: string)
  - returns: ```full_name``` (the corresponding full name \[or -1 in case of error\], type: string)
- #### getProfilePic(username, download = False)
  - description: Retrieves profile picture URL given a username.
  - parameters: ```username``` (a valid and existing instagram username, type: string)
  - parameters: ```download``` (whether or not profile picture should be downloaded, type: boolean, default: False)
  - returns: ```profile_pic_url``` (direct link to the corresponding profile picture \[or -1 in case of error\], type: string)
- #### getNewPost(username, download = False)
  - description: Retrieves most recent post given a username.
  - parameters: ```username``` (a valid and existing instagram username, type: string)
  - parameters: ```download``` (whether or not newest post should be downloaded, type: boolean, default: False)
  - returns: ```[post_page, post_pictures]``` (link to the page of the most recent post, link(s) to the picture(s) \[or -1 in case of error\], type: list of strings)
- #### getNewIGTV(username, download = False)
  - description: Retrieves most recent IGTV post given a username.
  - parameters: ```username``` (a valid and existing instagram username, type: string)
  - parameters: ```download``` (whether or not newest IGTV post should be downloaded, type: boolean, default: False)
  - returns: ```[igtv_nr, igtv_page, post_igtv]``` (Number IGTV posts, link to the page of the most recent post, the IGTV media \[or -1 in case of error\], type: list of strings)
- #### getTagged(username)
  - description: Retrieves the URL to the user's tagged posts.
  - parameters: ```username``` (a valid and existing instagram username, type: string)
  - returns: ```tagged_page``` (link to user's tagged page, type: string)
- #### isPostPrivate(instagram_post_url)
  - description: Retrieves private status given an URL to an instagram post.
  - parameters: ```instagram_post_url``` (a valid link to an existing instagram post, type: string)
  - returns: True/False (private status \[or -1 in case of error\], type: boolean)
- #### isProfilePrivate(username)
  - description: Retrieves private status of an instagram profile given a username.
  - parameters: ```username``` (a valid and existing instagram username, type: string)
  - returns: True/False (private status \[or -1 in case of error\], type: boolean)
- #### isProfileBusiness(username)
  - description: Retrieves business status of an instagram profile given a username.
  - parameters: ```username``` (a valid and existing instagram username, type: string)
  - returns: True/False (business status \[or -1 in case of error\], type: boolean)
- #### isProfileVerified(username)
  - description: Retrieves verified status of an instagram profile given a username.
  - parameters: ```username``` (a valid and existing instagram username, type: string)
  - returns: True/False (verified status \[or -1 in case of error\], type: boolean)
- #### getPostDetails(instagram_post_url)
  - description: Retrieves post details via the instagram API.
  - parameters: ```instagram_post_url``` (a valid link to an existing instagram post, type: string)
  - returns: ```[url, post_data, post_json]``` (a list containing the URL to the retrieved page, type: string; the json data in string format, type: string; the json data as a json object, type: json; \[or -1 in case of error\])
- #### getMedia(instagram_post_url, download = False)
  - description: Retrieves download links to media given an instagram post URL.
  - parameters: ```instagram_post_url``` (a valid link to an existing instagram post, type: string)
  - parameters: ```download``` (if media should be downloaded or not, type: boolean, default: False)
  - returns: ```media_links``` (a list of media links \[or -1 in case of error\], type: list of strings)
  - Note: For downloading several posts I recommend to use [Instagram Downloader](https://github.com/t0xic-m/instagram_downloader).

## License

[MIT License](https://github.com/t0xic-m/instatools/blob/master/LICENSE.md)

## Contact

- Website: [Web](https://t0xic-m.github.io/web)
- Website: [GitHub](https://t0xic-m.github.io)
- Mail: [Contact](mailto:micha.birklbauer@gmail.com)
