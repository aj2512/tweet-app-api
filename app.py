from flask import Flask, request, jsonify, Response
from flask_cors import CORS, cross_origin
import oauth2
import json
import urllib.parse
app = Flask(__name__)
CORS(app)

#Twitter Keys & Tokens
# CONSUMER_KEY = "Your KEY HERE"
# CONSUMER_SECRET = "YOUR SECRECT HERE"
# ACCESS_KEY = "Your KEY HERE"
# ACCESS_SECRET = "YOUR SECRECT HERE"

#Twitter Resource URL 
URL_SearcTweet = "https://api.twitter.com/1.1/search/tweets.json"
URL_SearcUsers = "https://api.twitter.com/1.1/statuses/user_timeline.json"

#authenticating
def oauth_req(url, http_method="GET", post_body="", http_headers=None):
    consumer = oauth2.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
    access_token = oauth2.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)
    client = oauth2.Client(consumer, access_token)
    resp, content = client.request( url )
    print(resp)
    return content

#check
@app.route('/healthcheck', methods=['GET'])
def healthcheck():
    data = {
         "status": "Ok"
    }
    return jsonify(data)

#Search for tweets by hashtag
@app.route('/hashtag/<hashtag>', methods=['GET'])
def test(hashtag):
    limit = request.args.get('limit', default = 30, type = int)
    query = (URL_SearcTweet + '?q=' + urllib.parse.quote("#" + hashtag + " -filter:retweets -filter:repiles") + "&lang=en&result_type=recent&count=" + str(limit) + "&tweet_mode=extended&include_entities=true").encode('utf-8')
    data = oauth_req(query)
    raw_data = json.loads(data)
    final_data = []
    for content in raw_data['statuses']:
        fullname=content['user']['name']
        href="/"+content['user']['screen_name']
        user_id=content['user']['id_str']
        create_date = content['id_str']
        hashtag_arr = []
        for hashtag_item in content['entities']['hashtags']:
            hashtag_arr.append(hashtag_item["text"])
        likes = content['favorite_count']
        repiles = content['retweet_count']
        retweets = content['retweet_count']
        text = content['full_text']
        data_dict = {
            "fullname": fullname,
            "href": href,
            "id": user_id,
            "date": create_date,
            "hashtags": hashtag_arr,
            "likes": likes,
            "repiles": repiles,
            "retweets": retweets,
            "text": text
        }
        final_data.append(data_dict)
    #print(final_data)
    return Response(json.dumps(final_data), mimetype='application/json')
    
#Search for tweets from user feed
@app.route('/users/<person>', methods=['GET'])
def tweets(person):
    limit = request.args.get('limit', default = 30, type = int)
    query = (URL_SearcUsers + '?screen_name=' + urllib.parse.quote(person) + "&lang=en&&result_type=recents&count=" + str(limit) + "&tweet_mode=extended&include_entities=true").encode('utf-8')
    #print(query)
    data = oauth_req(query)
    raw_data = json.loads(data)
    final_data = []
    for content in raw_data:
        fullname=content['user']['name']
        href="/"+content['user']['screen_name']
        user_id=content['user']['id_str']
        create_date = content['id_str']
        hashtag_arr = []
        for hashtag_item in content['entities']['hashtags']:
            hashtag_arr.append(hashtag_item["text"])
        likes = content['favorite_count']
        repiles = content['retweet_count']
        retweets = content['retweet_count']
        text = content['full_text']
        data_dict = {
            "fullname": fullname,
            "href": href,
            "id": user_id,
            "date": create_date,
            "hashtags": hashtag_arr,
            "likes": likes,
            "repiles": repiles,
            "retweets": retweets,
            "text": text
        }
        final_data.append(data_dict)
    #print(final_data)
    return Response(json.dumps(final_data), mimetype='application/json')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)