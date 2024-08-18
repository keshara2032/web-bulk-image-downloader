import requests
import os
# Used to securely store your API key
from configparser import ConfigParser
import time  # Import time module to introduce a delay between requests
from googleapiclient.discovery import build

from utils import *


config = ConfigParser()
config.read('credentials.ini')
api_key = config['API_KEY']['google_api_key']
cx = config['API_KEY']['cx_key']

service = build("customsearch", "v1", developerKey=api_key)

# Example usage:
search_query = 'iv access'
folder_path = './dataset/iv_access'

if(not os.path.exists(folder_path)):
    os.makedirs(folder_path)

page_size = 5
start_index = 1

while True:
    res = service.cse().list(
        q=search_query,
        cx=cx,
        searchType='image',
        num=page_size,
        imgType='photo',
        safe='off',
        start=start_index
    ).execute()

    download_images_from_results(res, folder_path)

    if 'queries' in res and 'nextPage' in res['queries'] and len(res['queries']['nextPage']) > 0:
        # Continue to the next page
        start_index = res['queries']['nextPage'][0]['startIndex']
        time.sleep(1)  # Introduce a delay to avoid making requests too quickly
    else:
        # No more pages, break out of the loop
        break