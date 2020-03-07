from flask import Flask, render_template, request, jsonify

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

import os

from dummy_data import test_articles


# init
app = Flask(__name__)
base_dir = os.path.abspath(os.path.dirname(__file__))


#db
app.config['SQLALCHEMY_DATABASE'] = 'sqlite:///' +os.path.join(base_dir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)


#models
class Article(db.Model):
    article_id = db.Column(db.integer, primary_key=True)
    title = db.Column()
    subtitle = db.Column()
    published = db.Column()
    amended = db.Column()
    thumbnail = db.Column()

    def __init__():
        




class Article_Segment(db.Model):
    article_segment_id = db.Column(db.integer, primary_key=True)


class Writer(db.Model):
    writer_id = db.Column(db.integer, primary_key=True)


class Category(db.Model):
    category_id = db.Column(db.integer, primary_key=True)



@app.route('/', methods=['GET'])
def home():
    featured = test_articles()[-4:]
    return render_template('home.html', featured=featured)


@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')


@app.route('/articles/<string:category>/', methods=['GET'])
def articles(category):
    articles = test_articles()
    if category != 'all':
        articles = (
            article 
            for article in articles
            if (category in article['categories'])
            )
    return render_template('articles.html', articles=articles)


@app.route('/article/<int:id>/', methods=['GET'])
def article(id):
    articles = test_articles()
    article = next(
        (
            article 
            for article in articles 
            if article['article_id'] == id
        ), 
        None
    )
    return render_template('article.html', article=article)


#run server
if __name__=='__main__':
    port = int(5000)
    app.run(host='0.0.0.0', port=port, debug=True)
