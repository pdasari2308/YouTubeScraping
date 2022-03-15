from googleapiclient.discovery import build

DEVELOPER_KEY = "AIzaSyBVQTVMsO5b8hTPN8I72y_3NBRsCxcizik"
# YOUTUBE_API_SERVICE_NAME = "youtube"
# YOUTUBE_API_VERSION = "v3"
commentsAll = []
repliesAll = []
def video_comments(video_id, token= None):
    # empty list for storing reply
    replies = []

    # creating youtube resource object
    youtube = build('youtube', 'v3',
                    developerKey=DEVELOPER_KEY)

    # retrieve youtube video results
    video_response = youtube.commentThreads().list(
        part='snippet,replies',
        videoId=video_id,
        pageToken=token
    ).execute()
    if 'nextPageToken' in video_response:
        token = video_response['nextPageToken']
    else:
        token = None
    # iterate video response
    while video_response:
        # extracting required info
        # from each result object
        for item in video_response['items']:

            # Extracting comments
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']

            # counting number of reply of comment
            replycount = item['snippet']['totalReplyCount']

            # if reply is there
            if replycount > 0:

                # iterate through all reply
                for reply in item['replies']['comments']:
                    # Extract reply
                    reply = reply['snippet']['textDisplay']

                    # Store reply is list
                    replies.append(reply)
                    repliesAll.append(reply)
            commentsAll.append(comment)
            # print comment with list of reply
            print(comment, replies, end='\n\n')
            # print(len(replies))
            # empty reply list
            replies = []

        # Again repeat
        # if 'nextPageToken' in video_response:
        #     video_response = youtube.commentThreads().list(
        #         part='snippet,replies',
        #         videoId=video_id
        #     ).execute()
        # else:
        #     break
        return token


videoID = "Fm8-ImJly1M"
token = video_comments(videoID)
print("-----------------------------NEXT-----------------------------------------------------------------------------")
# print(token)
while token != "last_page" and token is not None:
    if token is not None:
        token = video_comments(videoID, token=token)


