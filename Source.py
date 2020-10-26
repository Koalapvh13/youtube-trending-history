class Source(object):
    """
    Class to get  the source txt file from youtube
    """
    @staticmethod
    def getVideoIdsFromRemoteTxt(country: str, date: str) -> list:
        """
        Static method to get data from remote Txt file
        """
        BASE_URL = "https://raw.githubusercontent.com/ophobe/trending-youtube/master/"
        videoIdsList = []
        txt_url = BASE_URL + "{}/{}.txt".format(country, date)
        from urllib.request import urlopen
        videoIds = urlopen(txt_url)
        for video in videoIds:
            clearId = video.decode('utf-8').replace('\n', '')
            videoIdsList.append(clearId)
        return videoIdsList


if __name__ == "__main__":
    l = Source.getVideoIdsFromRemoteTxt('BR', '01-01-2020')
    print(l)
