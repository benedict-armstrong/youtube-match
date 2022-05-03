import math
from typing import List

from requests import HTTPError

from util.youtube import get_next_page, parse_youtube_subscriptions, youtube_subscriptions


def fetch_channels(youtube_authorization, ) -> List[str]:
    try:
        all_channels = []
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

    except HTTPError as err:
        print("An HTTP error {} occurred:\n{}".format(err.resp.status, err.content))