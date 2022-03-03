import csv
import sys
sys.path.append('/Users/abhinavreddy/PycharmProjects/youtubeScraping')
from youtube_videos import youtube_search, video_comments
from intoCSV import processTOCSV


# test = youtube_search("cognitive")

# video_dict = {'youID': [], 'title': [], 'pub_date': [], 'accountName': [], 'description': [], 'link': []}

# just_json = test[1]
# print(len(just_json))


# for video in just_json:
#     print(video['snippet']['title'])

# token = test[0]
# youtube_search("cognitive", token=token)

#  (when, who, account details, description, comment section, link)


video_dict = {
    'youID': [],
    'title': [],
    'accountName': [],
    'pub_date': [],
    'description': [],
    'link': [],
    'comments': []
}
writedata = []

def grab_videos(keyword, token=None):
    writeEachDict = {}
    res = youtube_search(keyword, token=token)
    token = res[0]
    videos = res[1]
    # print(token)
    for vid in videos:
        # for csv
        writeEachDict['youID'] = (vid['id']['videoId'])
        writeEachDict['title'] = (vid['snippet']['title'])
        # when
        writeEachDict['pub_date'] = (vid['snippet']['publishedAt'])
        # who
        writeEachDict['accountName'] = (vid['snippet']['channelTitle'])
        # description
        writeEachDict['description'] = (vid['snippet']['description'])
        # link
        writeEachDict['link'] = ("https://www.youtube.com/watch?v="  + vid['id']['videoId'])
        writedata.append(writeEachDict)


        video_dict['youID'].append(vid['id']['videoId'])
        video_dict['title'].append(vid['snippet']['title'])
        # when
        video_dict['pub_date'].append(vid['snippet']['publishedAt'])
        # who
        video_dict['accountName'].append(vid['snippet']['channelTitle'])
        # description
        video_dict['description'].append(vid['snippet']['description'])
        # link
        video_dict['link'].append("https://www.youtube.com/watch?v=" + vid['id']['videoId'])
        # comments (need to trim as the data is huge)
        # video_dict['comments'].append(video_comments(vid['id']['videoId']))

        # print(vid['snippet']['channelTitle'])
        # exit()



    print("added " + str(len(videos)) + " videos to a total of " + str(len(video_dict['youID'])))
    return token
# (toddler | kid) (Physical | Cognitive | Emotional | Social and Language | Sensory and Motor skills) (Development)
search_word = "child Physical Development"

token = grab_videos(search_word)
while token != "last_page":
    # print(token)
    token = grab_videos(search_word, token=token)

processTOCSV(video_dict)

# print(video_dict)
# fields = ['youID', 'title', 'accountName', 'pub_date', 'description', 'link']

# with open("YouTube_Data.csv", 'w') as csvfile:
#     # creating a csv dict writer object
#     writer = csv.DictWriter(csvfile, fieldnames=fields)
#
#     # writing headers (field names)
#     writer.writeheader()
#
#     # writing data rows
#     writer.writerows(writedata)