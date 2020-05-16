from flask import Flask, render_template, jsonify, request
from youtube import youtube_main

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/youtube", methods=['POST'])
def youtubeComment():
    value = request.form['id']
    url = value[value.find('?v=')+3:]
    youtube_main(url)
    return render_template('word.html', url=url)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=80)