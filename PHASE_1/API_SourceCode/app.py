from flask import Flask, request
from flask_restplus import Resource, Api, reqparse
import re
# from flask_jwt import JWT, jwt_required

# from security import authenticate, identity

app = Flask(__name__)
app.config.SWAGGER_UI_DOC_EXPANSION = 'list'

api = Api(app, title='CIDRAP', description='This API extracts disease report articles from the CIDRAP website. http://www.cidrap.umn.edu/')

articles = [
    {
        "id": "0", # this field was added
        "url":"www.who.int/lalala",
        "date_of_publication":"2018-12-12Txx:xx:xx",
        "headline":"Outbreaks in Southern Vietnam",
        "main_text":"Three people infected by what is thought to be H5N1 or H7N9 in Ho Chi Minh city. First infection occurred on 1 Dec 2018, and latest is report on 10 December. Two in hospital, one has recovered. Furthermore, two people with fever and rash infected by an unknown disease.",
        "reports":[
            {
                "disease":[
                    "influenza a/h5n1",
                    "influenza a/h7n9" 
                ],
                "syndrome":[
                ],
                "reported_events":[
                    {
                        "type":"recovered",
                        "date":"2018-12-01Txx:xx:xx to 2018-12-10Txx:xx:xx",
                        "location":{
                            "geonames-id":1566083
                        },
                        "number-affected":1 
                    },
                    {
                        "type":"hospitalised",
                        "date":"2018-12-01Txx:xx:xx to 2018-12-10Txx:xx:xx",
                        "location":{
                            "geonames-id":1566083 },
                        "number-affected":2
                    }
                ],
                "Comment":None
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
                "comment":None
            }
        ]
    }
]

'''
article_model = api.model('Article', 
    {
        "url":"www.who.int/lalala",
        "date_of_publication":"2018-12-12Txx:xx:xx",
        "headline":"Outbreaks in Southern Vietnam",
        "main_text":"Three people infected by what is thought to be H5N1 or H7N9 in Ho Chi Minh city. First infection occurred on 1 Dec 2018, and latest is report on 10 December. Two in hospital, one has recovered. Furthermore, two people with fever and rash infected by an unknown disease.",
        "reports":[
            {
                "disease":[
                    "influenza a/h5n1",
                    "influenza a/h7n9" 
                ],
                "syndrome":[
                ],
                "reported_events":[
                    {
                        "type":"recovered",
                        "date":"2018-12-01Txx:xx:xx to 2018-12-10Txx:xx:xx",
                        "location":{
                            "geonames-id":1566083
                        },
                        "number-affected":1 
                    },
                    {
                        "type":"hospitalised",
                        "date":"2018-12-01Txx:xx:xx to 2018-12-10Txx:xx:xx",
                        "location":{
                            "geonames-id":1566083 },
                        "number-affected":2
                    }
                ],
                "Comment":None
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
                "comment":None
            }
        ]
    })
'''

class Articles(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('start_date',
        type=str,
        required=True,
        help='Start date of articles in period of interest in the format "yyyy-mm-ddThh:mm:ss".\n Year is required, every other segment is optional and missing characters must be replaced with "x"'
    )
    parser.add_argument('end_date',
        type=str,
        required=True,
        help='End date of articles in period of interest in the format "yyyy-mm-ddThh:mm:ss".\n Year is required, every other segment is optional and missing characters must be replaced with "x"'
    )
    parser.add_argument('key_terms',
        type=str,
        required=False,
        help='Comma separated list of key terms to search for'
    )
    parser.add_argument('location',
        type=str,
        required=False,
        help='Names of locations of interest'
    )
    
    @api.expect(parser)
    @api.doc(responses = {
        200: 'Search successful', 
        400: 'Invalid parameters', 
        404: 'No results found'
    })
    def get(self):
        data = Articles.parser.parse_args()
        date_regex = re.compile('^(\d{4})-(\d\d|xx)-(\d\d|xx)T(\d\d|xx):(\d\d|xx):(\d\d|xx)$')
        if not (date_regex.match(data['start_date']) and date_regex.match(data['end_date'])) and data[start_date] <= data[end_date]:
            return 400
        else: # start and end dates valid
            search_results = list(filter(lambda x: (x['date_of_publication'] <= data['end_date'] and x['date_of_publication'] >= data['start_date']), articles))
            if data['key_terms']: #TODO 
                search_terms = data['key_terms'].split(',');
                pass
            if data['location']:
                pass
            if articles:
                return {'articles': search_results}
            else:
                return 404

@api.param('article_id', 'ID of the requested article')
class Article(Resource):
    @api.doc(responses = {
        200: 'Article retrieved', 
        400: 'Invalid article ID', 
        404: 'Article not found'
    })

    # how to get id:

    def get(self, article_id):
        article_id = request.view_args['article_id']
        if not article_id.isdigit():
            return 400
        desired_article = list(filter(lambda x: x['id'] == article_id, articles))
        print(desired_article)
        if len(desired_article) > 0:
            return desired_article[0], 200
        else:
            return 404

api.add_resource(Articles, '/articles')
api.add_resource(Article, '/article/<article_id>')

if __name__ == '__main__':
    app.run(debug=True)
