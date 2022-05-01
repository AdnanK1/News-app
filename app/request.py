from app import app
from newsapi import NewsApiClient

def get_head_news():
    #Getting api key
    newsapi = NewsApiClient(api_key = app.config['NEWS_API_KEY'])
    
    #headlines
    top_headlines = newsapi.get_top_headlines(sources= 'cnn,bbc-news')
    

    #Fetch all articles of the top headlines
    top_articles = top_headlines['articles']

    

    #make a list of contents to store the values on the list
    news = []
    desc = []
    img = []
    p_date = []
    url = []

    #fetch all the contents of the articles by using for loop
    for i in range(len(top_articles)):
        head_article = top_articles[i]

        news.append(head_article['title'])
        desc.append(head_article['description'])
        img.append(head_article['urlToImage'])
        p_date.append(head_article['publishedAt'])
        url.append(head_article['url'])

        #make a zip for finding the contents directly
        head = zip(news,desc,img,p_date,url)
        return head

def get_main_news():
    #Getting api key
    newsapi = NewsApiClient(api_key = app.config['NEWS_API_KEY'])

    #main articles
    all_articles = newsapi.get_everything(sources= 'cnn,bbc-news')

    #Fetch all articles
    a_articles = all_articles['articles']
    #make a list of contents to store the values on the list
    news_all = []
    desc_all = []
    img_all = []
    p_date_all = []
    url_all = []

    #fetch all the contents of the articles by using for loop
    for j in range(len(a_articles)):
        a_article = a_articles[j]
        #append all the contents in each of the lists
        news_all.append(a_article['title'])
        desc_all.append(a_article['description'])
        img_all.append(a_article['urlToImage'])
        p_date_all.append(a_article['publishedAt'])
        url_all.append(a_article['url'])

        main = zip(news_all,desc_all,img_all,p_date_all,url_all)
        return main
