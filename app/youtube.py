# Base code from https://medium.com/@jjeaby/youtube-data-api-%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%9C-commnet-text-%EA%B0%80%EC%A0%B8%EC%98%A4%EA%B8%B0-9fa6de6d7da6

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
if(key==None):
   raise Exception('youtube api key is null')

def getYoutube(_videoId, _pageToken=None):
   status_code = 0
   cnt = 0
   while (status_code!= 200 and cnt<5):
      if (_pageToken == None):
         page_info = requests.get(YOUTUBE_LINK.format(videoId = _videoId, key = key))
      else:
         page_info = requests.get(YOUTUBE_IN_LINK.format(videoId = _videoId, key = key, pageToken = _pageToken))
      status_code = page_info.status_code
      time.sleep(5)
      cnt += 1
   if status_code == 200:
      return page_info
   else:
      if (_pageToken == None):
         raise Exception('status code not 200')
      else:
         raise Exception('next page status code not 200')

def commentExtract(videoId, count = -1):
   page_info = getYoutube(videoId)
   page_info = page_info.json()
   comments = []
   cnt = 0
   for i in range(len(page_info['items'])):
      comments.append(page_info['items'][i]['snippet']['topLevelComment']['snippet']['textOriginal'])
      cnt += 1
      if cnt == count:
         return comments

   while 'nextPageToken' in page_info:
      page_info = getYoutube(videoId, page_info['nextPageToken'])
      page_info = page_info.json()
      page_info_len = len(page_info['items'])

      for i in range(page_info_len):
         comments.append(page_info['items'][i]['snippet']['topLevelComment']['snippet']['textOriginal'])
         cnt += 1
         if cnt == count:
            return comments

   return comments

if __name__ == "__main__":
   print(commentExtract('XoH9jzblxKQ'))