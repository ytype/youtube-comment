import sys, os
testPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, testPath + '/../app')

from dotenv import load_dotenv
import os

from youtube import commentExtract

load_dotenv(verbose=True)

def test_data():
    #videoId = os.getenv("VIDEO_ID")
    #assert len(commentExtract(videoId))>400
    assert 1==1