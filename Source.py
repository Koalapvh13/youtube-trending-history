class Source(object):
    """
    Class to get  the source txt file from youtube
    """
    @staticmethod
    def getVideoIdsFromRemoteTxt(country: str, date: str) -> list:
        """
        Static method to consult the remote TXT file (hosted on GitHub) and return a list with video's 
        ID from trending on determinate day.

        Parameters:
            country (str): the country from the video's trending
            date (str): specific day from the trend video list

        Return:
            videoIdsList (list[str]): list with the list of video's ID on the trending day
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
