import urllib.request,json
from .models import News,Article


# Getting api key
api_key = None

# Getting the news base url
news_base_url = None
article_base_url = None

def configure_request(app):
    global api_key, news_base_url , article_base_url
    api_key = app.config['NEWS_API_KEY']
    news_base_url = app.config['NEWS_API_BASE_URL']
    article_base_url = app.config['ARTICLE_BASE_URL']



def get_news():
    '''
    Function that gets the json response to our url request
    '''
    
    get_news_url = news_base_url.format(api_key)
    
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None
    
        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
            news_results = process_newsResults(news_results_list)


    return news_results

def get_articles(id):
    get_articles_url = article_base_url.format(id, api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        articles_data = url.read()
        articles_response = json.loads(articles_data)

    articles_result = None
    if articles_response['articles']:
        articles_list = articles_response['articles']
        articles_result = process_articleResults(articles_list)

    return articles_result


def process_newsResults(news_list):

    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        country = news_item.get('country')
        url = news_item.get('url')
        category = news_item.get('category')

        news_object = News(id,name, description,country, url, category)
        news_results.append(news_object)

    return news_results


def process_articleResults(article_list):

    article_results = []
    for article in article_list:
        author = article.get('author')
        title = article.get('title')
        description = article.get('description')
        url = article.get('url')
        urlToImage = article.get('urlToImage')
        content = article.get('content')

       


        article_object = Article(author, title, description, url, urlToImage, content)
        article_results.append(article_object)

    return article_results 