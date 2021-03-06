import sys, os
testPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, testPath + '/../app')

from main import app
client = app.test_client()

def test_index():
	response = client.get('/')
	assert response.status_code == 200

def test_404():
	response = client.get('/this_page_would_not_be_exist')
	assert response.status_code == 404