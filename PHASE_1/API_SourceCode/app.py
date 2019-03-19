from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required

from security import authenticate, identity

app = Flask(__name__)

api = Api(app)

articles = [
    {
        "url":"www.who.int/lalala",
        "date_of_publication":"2018-12-12Txx:xx:xx",
        "headline":"Outbreaks in Southern Vietnam",
        "main_text":"Three people infected by what is thought to be H5N1 or H7N9 in Ho Chi Minh city.
        First infection occurred on 1 Dec 2018, and latest is report on 10 December. Two in hospital, one has recovered. Furthermore, two people with fever and rash infected by an unknown disease.",
        "reports":[
           {
               "disease":[
               "influenza a/h5n1",
               "influenza a/h7n9" ],
               "syndrome":[
               ],
               "reported_events":[
                   {
                       "type":"recovered",
                       "date":"2018-12-01Txx:xx:xx to 2018-12-10Txx:xx:xx",
                       "location":{
                        "geonames-id":1566083
                        },
                        "number-affected":1 },
                        {
                        "type":"hospitalised",
                        "date":"2018-12-01Txx:xx:xx to 2018-12-10Txx:xx:xx",
                        "location":{
                           "geonames-id":1566083 },
                        "number-affected":2
                        }
                ],
                "Comment":null
              },
              {
                 "disease":[
                 "unknown"
                 ],
                 "syndrome":[
                     "Acute fever and rash"
                 ],
                 "reported_events":[
                   {
                      "type":"infected",
                      "date":"2018-12-01Txx:xx:xx to 2018-12-10Txx:xx:xx",
                      "location":{
                      "geonames-id":1566083
                      },
                      "number-affected":2
                      }
                  ],
                  "comment":null
               }
       ]
    }
]

class Articles(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('start_date',
        type=str,
        required=True
    )
    parser.add_argument('end_date',
        type=str,
        required=True
    )
    parser.add_argument('key_terms',
        type=str,
        required=False
    )
    parser.add_argument('location',
        type=str,
        required=False
    )
    def get(self):
        data = Articles.parser.parse_args()
        articles_in_dates = list(filter(lambda x: (x['date_of_publication'] <= data['end_date'] and x['date_of_publication'] >= data['start_date'), articles))
        if data['key_terms']:
            pass
        if data['location']:
            pass
        return {'articles': articles_in_dates}

class Article(Resource):
    def get(self, article_id):
        
        return

api.add_resource(Articles, '/articles')
api.add_resource(Article, '/article/<article_id>')
