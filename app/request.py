from app import app
import urllib.request,json
from .models import newsarticles
Newsarticles = newsarticles.Newsarticles


api_key = app.config['NEWS_API_KEY']

#Getting the base url
base_url = app.config['NEWS_API_BASE_URL']

def get_news():
    get_news_url = base_url.format(api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_results(news_results_list)

    return news_results

def process_results(news_list):
    news_results = []
    for news_item in news_list:
        title = news_item.get('title')
        desc = news_item.get('description')
        img = news_item.get('urlToImage')
        time = news_item.get('publishedAt')
        url = news_item.get('url')

        news_object = Newsarticles(title,desc,img,time,url)
        news_results.append(news_object)

    return news_results

