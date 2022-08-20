from flask import Flask, jsonify, request

from blog.commands import CreateArticleCommand
from blog.queries import GetArticleByIDQuery, ListArticlesQuery

app = Flask(__name__)

@app.route("/create-article/", methods=["POST"])
def create_article():
    cmd = CreateArticleCommand(
        **request.json
    )
    return jsonify(cmd.execute().dict())