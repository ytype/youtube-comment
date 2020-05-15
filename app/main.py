from flask import Flask
from flask import jsonify
from youtube import commentExtract

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World from Flask"

@app.route("/youtube/<videoId>", methods=['GET'])
def youtubeComment(videoId):
    return jsonify(commentExtract(videoId))

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=80)