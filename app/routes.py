from flask import render_template
from app import app
from newsapi import NewsApiClient

@app.route('/')
@app.route('/home')
def home_page():
    #Getting api
    newsapi = NewsApiClient(api_key = app.config['NEWS_API_KEY'])

    #headlines
    top_headlines = newsapi.get_top_headlines(sources= 'cnn,bbc-news')
    #main articles
    all_articles = newsapi.get_everything(sources= 'cnn,bbc-news')


    #Fetch all articles of the top headlines
    top_articles = top_headlines['articles']

    #Fetch all articles
    a_articles = all_articles['articles']

    #make a list of contents to store the values on the list
    news = []
    desc = []
    img = []
    p_date = []
    url = []

    # fetch all the contents of the articles by using for loop
    for i in range(len(top_articles)):
        main_article = top_articles[i]
        #append all the contents in each of the lists
        news.append(main_article['title'])
        desc.append(main_article['description'])
        img.append(main_article['urlToImage'])
        p_date.append(main_article['publishedAt'])
        url.append(main_article['url'])

        #make a zip for finding the contents directly
        contents = zip(news,desc,img,p_date,url)

    news_all = []
    desc_all = []
    img_all = []
    p_date_all = []
    url_all = []

    for j in range(len(a_articles)):
        a_article = a_articles[j]
        #append all the contents in each of the lists
        news_all.append(a_article['title'])
        desc_all.append(a_article['description'])
        img_all.append(a_article['urlToImage'])
        p_date_all.append(a_article['publishedAt'])
        url_all.append(a_article['url'])

        all = zip(news_all,desc_all,img_all,p_date_all,url_all)


    return render_template('home.html', contents=contents,all=all)
