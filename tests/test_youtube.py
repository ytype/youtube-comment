import sys
import os
testPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, testPath + '/../app')

import pytest
from dotenv import load_dotenv
from youtube import commentExtract
from youtube import preTexts

load_dotenv(verbose=True)

def test_data():
    videoId = os.getenv("VIDEO_ID")
    assert len(commentExtract(videoId))>10

def test_text_processing():
    text = ["안녕하세요 12 abc !!@# #\n"]
    result = preTexts(text)
    print(result)
    assert result == ["안녕하세요"]
