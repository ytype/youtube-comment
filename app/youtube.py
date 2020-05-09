# code from https://medium.com/@jjeaby/youtube-data-api-%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%9C-commnet-text-%EA%B0%80%EC%A0%B8%EC%98%A4%EA%B8%B0-9fa6de6d7da6

import lxml
import requests
import time
import sys

from dotenv import load_dotenv
import os

YOUTUBE_IN_LINK = 'https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&maxResults=100&order=relevance&pageToken={pageToken}&videoId={videoId}&key={key}'
YOUTUBE_LINK = 'https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&maxResults=100&order=relevance&videoId={videoId}&key={key}'

load_dotenv(verbose=True)
key = os.getenv("YOTUBE_API_KEY")
   
def commentExtract(videoId, count = -1):
   print ("Comments downloading")
   page_info = requests.get(YOUTUBE_LINK.format(videoId = videoId, key = key))
   while page_info.status_code != 200:
      if page_info.status_code != 429:
         print ("Comments disabled")
         sys.exit()

      time.sleep(20)
      page_info = requests.get(YOUTUBE_LINK.format(videoId = videoId, key = key))

   page_info = page_info.json()

   comments = []
   co = 0;
   for i in range(len(page_info['items'])):
      comments.append(page_info['items'][i]['snippet']['topLevelComment']['snippet']['textOriginal'])
      co += 1
      if co == count:
         print ()
         return comments

   # INFINTE SCROLLING
   while 'nextPageToken' in page_info:
      temp = page_info
      page_info = requests.get(YOUTUBE_IN_LINK.format(videoId = videoId, key = key, pageToken = page_info['nextPageToken']))

      while page_info.status_code != 200:
         time.sleep(20)
         page_info = requests.get(YOUTUBE_IN_LINK.format(videoId = videoId, key = key, pageToken = temp['nextPageToken']))
      page_info = page_info.json()

      for i in range(len(page_info['items'])):
         comments.append(page_info['items'][i]['snippet']['topLevelComment']['snippet']['textOriginal'])
         co += 1
         if co == count:

            print ()
            return comments

   print ()
   return comments