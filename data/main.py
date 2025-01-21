from odds import odds
from aws import s3
import time
import os

# Vars for API Request
ALL = 'true'
REGION = 'us'
SPORTS = ['americanfootball_ncaaf']
MARKETS = 'spreads,totals'
DAYS_FROM = '2'
DATE_FORMAT = 'unix'

# Specify your S3 bucket and the file name
S3_BUCKET_NAME = os.environ['S3_BUCKET_NAME']
STAGE = os.environ['STAGE']

print("This is the stage", STAGE)

# Instantiate objects
request_object = odds.oddsAPIClient()
s3_object = s3.awsHandler()

sports_data = request_object.make_request(endpoint='sports')

print("Uploading sports to s3")
s3_object.upload_json_to_s3(
    sports_data,
    S3_BUCKET_NAME,
    f'{STAGE}/sports/{int(time.time())}.json'
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
        endpoint=f'sports/{SPORT}/odds',
        params=odds_params
    )

    # Upload odds data to s3
    print("Uploading odds to s3")
    print(odds_data)
    s3_object.upload_json_to_s3(
        odds_data,
        S3_BUCKET_NAME,
        f'{STAGE}/odds/{SPORT}/{int(time.time())}.json'
    )

    # Gets passed into request for scores
    scores_params = {
        'regions': REGION,
        'daysFrom': DAYS_FROM,
        'dateFormat': DATE_FORMAT
    }

    # makes reuqest for scores
    scores_data = request_object.make_request(
        endpoint=f'sports/{SPORT}/scores',
        params=scores_params
    )

    # Upload scores2 data to s3
    print("Uploading scores to s3")
    s3_object.upload_json_to_s3(
        scores_data,
        S3_BUCKET_NAME,
        f'{STAGE}/scores/{SPORT}/{int(time.time())}.json'
    )
