# Simple Tweet Search App

Search for tweets by hashtags or tweets from user's feed.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Requirements

* Python 3.7.x
* PIP
* Twitter Account
* cURL(or any browser)

Register an app at https://developer.twitter.com/en/apps and get the consumer & access tokens.

## How to run locally
Download code to a local directory.

## Setup
### Additional requirements

Additional Requirements:
* Flask
* Flask-Cors
* oauth2

* Install requirements for app
```
pip install -r requirements.txt
```
### Create Twitter Application
* Create a new app here - https://dev.twitter.com/apps
* Application should be Read and Write capable
* Create OAUTH KEY and SECRET for yourself
 
 ```
Example:
Consumer key - 9zIJUgfYWN1DfE11CWZ605MUB 
API secret - key4gxdVRVjpawJXuHVyHRtGkpiK8JyKxRNr6We5W4I1KgQZA4noo
Access token - 27181586-QGaLhLXfSz3XMJm4wenDY1HmOGpa40U3Pph9WbAuL 
Access token secret - QF0VMHS9gnzVHHOwycY6h9NN7nv0cs2ix7ILljMcVpSnX
```
## Deployment
### Start Flask server
In terminal, under code directory, run app.py
```
python app.py
```

## Examples
### Searching Hashtags

Ex. Hashtag = python

* Web browser
```
http://localhost:5000/hashtag/python?limit=30
```

* Using Curl
```
curl -H "Accept: application/json" -X GET http://localhost:5000/users/twitter?limit=30
```

* Example Response
```
[{"fullname": "Deep_In_Depth", "href": "/Deep_In_Depth", "id": "861861525883158528", "date": "1154255029668388864", "hashtags": ["DeepLearning", "MachineLearning", "AI", "DataScience", "NeuralNetworks", "ReinforcementLearning", "NLP", "GPU", "TensorFlow", "Keras", "Pytorch", "Python", "HPC", "AutonomousCar", "Quant", "ArtificialIntelligence", "Automation"], "likes": 0, "repiles": 0, "retweets": 0, "text": "AI Accelerators are Revolutionizing Edge Computing! https://t.co/Q612kBoPPs #DeepLearning #MachineLearning #AI #DataScience #NeuralNetworks #ReinforcementLearning #NLP #GPU #TensorFlow #Keras #Pytorch #Python #HPC #AutonomousCar #Quant #ArtificialIntelligence #Automation"}]
```

### Search Tweets in User Feed
Ex. User = twitter
* Web browser
```
http://localhost:5000/users/twitter?limit=1
```
* Using Curl
```
curl -H "Accept: application/json" -X GET http://localhost:5000/users/twitter?limit=1
```

* Example Response
```
[{"fullname": "Twitter", "href": "/Twitter", "id": "783214", "date": "1154233785044602880", "hashtags": ["Tweetups"], "likes": 2, "repiles": 1, "retweets": 1, "text": "@AlaiaWilliams @pfont \ud83d\udc99 this. Let\u2019s make it happen. Wanna join one of our #Tweetups on Abbot Kinney?"}]
```

### Search Parameters
Address of local running server
```
http://localhost:5000
```

limit: integer, specifies the number of tweets to retrieve, default is 30.
item: hashtag or users (specific user's feed)
<text>: either a hashtag or user's name (Internal Server Error: if the name does not exist)
```
http://localhost:5000/item/<text>?limit=30
```


## Documentation
Twitter's API documentation: https://developer.twitter.com/en/docs


## Built With

* [Flask](http://www.dropwizard.io/1.0.2/docs/) - lightweight web application framework
* [Flask-Cors](https://flask-cors.readthedocs.io/en/latest/) - Flask extension




