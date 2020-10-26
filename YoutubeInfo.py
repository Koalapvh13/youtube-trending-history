class YoutubeInfo(object):
    """
    Class to get info about a specific Youtube Video
    """

    @staticmethod
    def getVideoInfo(url_link: str):
        """
        docstring
        """
        import urllib.request
        import json
        import urllib

        params = {"format": "json",
                  "url": "https://www.youtube.com/watch?v="+url_link}
        url = "https://www.youtube.com/oembed"
        query_string = urllib.parse.urlencode(params)
        url = url + "?" + query_string

        info = ""
        try:
            with urllib.request.urlopen(url) as response:
                response_text = response.read()
                data = json.loads(response_text.decode())
                info = {
                    "title": data["title"],
                    "video_url":  "https://www.youtube.com/watch?v="+url_link,
                    "channel": data["author_name"],
                    "channel_url": data["author_url"],
                    "thumbnail": "https://i.ytimg.com/vi/BrnDlRmW5hs/hqdefault.jpg"
                }
        except urllib.error.HTTPError as exception:
            print(exception.getcode())
        finally:
            return info


if __name__ == "__main__":
   # YoutubeInfo.info('BrnDlRmW5hs')
    print(YoutubeInfo.getVideoInfo(
        'BrnDlRmW5hs'))
