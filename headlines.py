import feedparser
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

RSS_FEEDS = {'tn': 'https://tn.com.ar/rss.xml',
             # 'espn': 'http://www.espn.com/espn/rss/news',
             'clarin': 'https://www.clarin.com/rss/lo-ultimo/',
             'telam': 'https://www.telam.com.ar/rss2/ultimasnoticias.xml'}


@app.route('/')
def get_news():

    query = request.args.get('publication')
    if not query or query.lower() not in RSS_FEEDS:
        publication = 'tn'
    else:
        publication = query.lower()

    feed = feedparser.parse(RSS_FEEDS[publication])

    return render_template('home.html', articles=feed['entries'])

if __name__ == '__main__':
    app.run(port=5000, debug=True)
