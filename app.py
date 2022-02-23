from flask import Flask, render_template, request
import json
import os

from cores.music import music_core

app = Flask(__name__)

@app.route("/music/")
@app.route("/music/<tool>/")
def music(tool=None):
    action = request.args.get("action") # show_artist, show_album, show_all?
    artist = request.args.get("artist")
    album = request.args.get("album")

    if action == "show_artist":
        if artist:
            if os.path.isfile("./static/storage/music/" + artist + "/infos.json"):
                return render_template("index.html", category="music", tool=tool, url={
                    "action": action
                }, other = {
                    "data_static": json.loads(open("./static/storage/music/category_infos.json", "r", encoding="utf8").read()),
                    "data_passthrough": json.loads(open("./static/storage/music/" + artist + "/infos.json", "r", encoding="utf8").read())
                })
    elif action == "show_album":
        if artist and album:
            if os.path.isfile("./static/storage/music/" + artist + "/infos.json"):
                return render_template("index.html", category="music", tool=tool, url={
                    "action": action,
                    "album": album
                }, other = {
                    "data_static": json.loads(open("./static/storage/music/category_infos.json", "r", encoding="utf8").read()),
                    "data_passthrough": json.loads(open("./static/storage/music/" + artist + "/infos.json", "r", encoding="utf8").read())
                })
    else: # or action == "show_all"
        return render_template("index.html", category="music", tool=tool, url={}, other = {
            "data_static": json.loads(open("./static/storage/music/category_infos.json", "r", encoding="utf8").read()),
        })

@app.route("/process/<name>")
def run_process(name=None, args=None):
    if name == "refresh_artist_list":
        music_core.refresh_artist_list()

    #return "<script>document.location.href=\"" + str(request.args.get("page")) + "\"</script>"
    return ""