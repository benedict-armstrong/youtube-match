#GET https://www.googleapis.com/youtube/v3/subscriptions

# Query youtube api get subscriptions
# coding: utf-8
# https://developers.google.com/youtube/v3/docs/subscriptions/list

import math
import os

from get_auth import get_authenticated_service

def retrieve_youtube_subscriptions():
    # In order to retrieve the YouTube subscriptions for the current user,
    # the user needs to authenticate and authorize access to their YouTube
    # subscriptions.
    youtube_authorization = get_authenticated_service()

    try:
        # init
        next_page_token = ''
        subs_iteration = 0
        while True:
            # retrieve the YouTube subscriptions for the authorized user
            subscriptions_response = youtube_subscriptions(youtube_authorization, next_page_token)
            subs_iteration += 1
            total_results = subscriptions_response['pageInfo']['totalResults']
            results_per_page = subscriptions_response['pageInfo']['resultsPerPage']
            total_iterations = math.ceil(total_results / results_per_page)
            print('Subscriptions iteration: {} of {} ({}%)'.format(subs_iteration,
                                                                   total_iterations,
                                                                   round(subs_iteration / total_iterations * 100),
                                                                   0))
            # get the token for the next page if there is one
            next_page_token = get_next_page(subscriptions_response)
            # extract the required subscription information
            channels = parse_youtube_subscriptions(subscriptions_response)
            # add the channels relieved to the main channel list
            all_channels.extend(channels)
            if not next_page_token:
                break
        return all_channels

    except HttpError as err:
        print("An HTTP error {} occurred:\n{}".format(err.resp.status, err.content))


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


if __name__ == "__main__":
    # init
    all_channels = []

    print('Perform youtube subscriptions')
    # retrieve subscriptions
    all_channels = retrieve_youtube_subscriptions()
    print('Subscriptions complete')
    print('Subscriptions found: {}'.format(len(all_channels)))

    print("Channels:\n", "\n".join(all_channels), "\n")