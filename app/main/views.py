from flask import render_template,url_for
from . import main
from ..requests import get_articles,get_news

# Views
@main.route('/')
def index():

    news_list = get_news()
    title = 'News'
    return render_template('index.html', title = title,  news = news_list)


@main.route('/articles/<id>')
def articles(id):

    
    articles = get_articles(id)
    return render_template('articles.html', articles = articles)

