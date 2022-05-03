# Call youtube.subscriptions.list method
# to list the channels subscribed to.
def youtube_subscriptions(youtube, next_page_token):
    subscriptions_response = youtube.subscriptions().list(
        part='snippet',
        mine=True,
        maxResults=50,
        order='alphabetical',
        pageToken=next_page_token).execute()
    return subscriptions_response


def get_next_page(subscriptions_response):
    # check if the subscription response contains a reference to the
    # next page or not
    if 'nextPageToken' in subscriptions_response:
        next_page_token = subscriptions_response['nextPageToken']
    else:
        next_page_token = ''
    return next_page_token


def parse_youtube_subscriptions(subscriptions_response):
    channels = []

    # Add each result to the appropriate list
    for subscriptions_result in subscriptions_response.get("items", []):
        if subscriptions_result["snippet"]["resourceId"]["kind"] == "youtube#channel":
            channels.append("{} ({})".format(subscriptions_result["snippet"]["title"],
                                             subscriptions_result["snippet"]["resourceId"]["channelId"]))

    return channels