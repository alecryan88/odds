from odds import odds
from aws import s3
import time

# from datetime import datetime

# Vars for API Request
ALL = 'true'
REGION = 'us'
SPORTS = ['americanfootball_ncaaf']
MARKETS = 'spreads,totals'
DAYS_FROM = '2'
DATE_FORMAT = 'unix'

# Specify your S3 bucket and the file name
BUCKET_NAME = 'odds-api-data'

# Instantiate objects
request_object = odds.oddsAPIClient()
s3_object = s3.awsHandler()

sports_data = request_object.make_request(endpoint='sports')

print("Uploading sports to s3")
s3_object.upload_json_to_s3(
    sports_data,
    BUCKET_NAME,
    f'sports/{int(time.time())}.json'
    )

for SPORT in SPORTS:
    # Gets passed into request for odds
    odds_params = {
        'regions': REGION,
        'markets': MARKETS,
        'daysFrom': DAYS_FROM,
        'dateFormat': DATE_FORMAT
    }

    # retrieve odds data
    odds_data = request_object.make_request(
        endpoint='sports/{SPORT}/odds',
        params=odds_params
    )

    # Upload odds data to s3
    print("Uploading odds to s3")
    s3_object.upload_json_to_s3(
        odds_data,
        BUCKET_NAME,
        f'odds/{SPORT}/{int(time.time())}.json'
    )

    # Gets passed into request for scores
    scores_params = {
        'regions': REGION,
        'daysFrom': DAYS_FROM,
        'dateFormat': DATE_FORMAT
    }

    # makes reuqest for scores
    scores_data = request_object.make_request(
        endpoint='sports/{SPORT}/scores',
        params=scores_params
    )

    # Upload scores2 data to s3
    print("Uploading scores to s3")
    s3_object.upload_json_to_s3(
        scores_data,
        BUCKET_NAME,
        f'scores/{SPORT}/{int(time.time())}.json'
    )
