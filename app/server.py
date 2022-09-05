from flask import Flask, request
from indexer import indexer

server = Flask(__name__)

@server.route("/")
def app():
    video_url = request.args.get('video_url')
    response = indexer(video_url)
    return response

if __name__ == '__main__':
    server.run(host='0.0.0.0')