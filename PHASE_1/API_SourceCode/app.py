from flask import Flask, request
from flask_restplus import Resource, Api, reqparse, fields
import re
from scraper import scrape, update_db
import json
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
                "id":0,
                "disease":[
                    "influenza a/h5n1",
                    "influenza a/h7n9" 
                ],
                "syndrome":[
                ],
                "reported_events":[
                    {
                        "id": 0,
                        "type":"recovered",
                        "date":"2018-12-01Txx:xx:xx to 2018-12-10Txx:xx:xx",
                        "location":{
                            "geonames-id":1566083
                        },
                        "number-affected":1 
                    },
                    {
                        "id": 1,
                        "type":"hospitalised",
                        "date":"2018-12-01Txx:xx:xx to 2018-12-10Txx:xx:xx",
                        "location":{
                            "geonames-id":1566083 },
                        "number-affected":2
                    }
                ],
                "comment":None
            },
            {
                "id":1,
                "disease":[
                    "unknown"
                ],
                "syndrome":[
                    "Acute fever and rash"
                ],
                "reported_events":[
                    {
                        "id": 2,
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

location_model = api.model('Location', {
    'geonames-id': fields.Integer(example=1566083)
})

reported_event_model = api.model('Reported Event', {
    'id': fields.Integer(example=0),
    'type': fields.String(enum=['presence','death','infected','hospitalised','recovered'], example='infected'),
    'date': fields.String(example='2018-12-01Txx:xx:xx to 2018-12-10Txx:xx:xx'),
    'location': fields.Nested(location_model),
    'number-affected': fields.Integer(example=2)
})

report_model = api.model('Report', {
    'id': fields.Integer(example=0),
    'disease': fields.List(fields.String(example='unknown')),
    'syndrome': fields.List(fields.String(example='Acute fever and rash')),
    'reported_events': fields.List(fields.Nested(reported_event_model)),
    'comment': fields.String(example='')
})

article_model = api.model('Article', {
    'id': fields.Integer(example=0),
    'url': fields.String(example='http://www.who.int/lalala'),
    'date_of_publication': fields.String(example='2018-12-12Txx:xx:xx'),
    'headline': fields.String(example='Outbreaks in Southern Vietnam'),
    'main_text': fields.String(example='Three people infected by what is thought to be H5N1 or H7N9 in Ho Chi Minh city. First infection occurred on 1 Dec 2018, and latest is report on 10 December. Two in hospital, one has recovered. Furthermore, two people with fever and rash infected by an unknown disease.'),
    'reports': fields.List(fields.Nested(report_model))
})

search_result_model = api.model('Search Results', {
    'articles': fields.List(fields.Nested(article_model))
})

@api.param('article_id', 'ID of the requested article')
class Article(Resource):
    @api.response(200, 'Article retrieved', article_model)
    @api.response(400, 'Invalid article ID')
    @api.response(404, 'Article not found')

    # for testing
    # @api.response(600, 'Report', report_model)
    # @api.response(601, 'Reported Event', reported_event_model)
    # @api.response(602, 'Search result', search_result_model)

    # how to get id:

    def get(self, article_id):
        article_id = request.view_args['article_id']
        if not article_id.isdigit():
            return {'comment': 'Invalid article ID'}, 400
        desired_article = list(filter(lambda x: x['id'] == article_id, articles))
        print(desired_article)
        if len(desired_article) > 0:
            return desired_article[0], 200
        else:
            return {'comment': 'Article not found'}, 404

class Articles(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('start_date',
        type=str,
        required=True,
        help='Start date of articles in period of interest in the format "yyyy-mm-ddThh:mm:ss".\n Year is required, every other segment is optional, but missing characters must be replaced with "x"'
    )
    parser.add_argument('end_date',
        type=str,
        required=True,
        help='End date of articles in period of interest in the format "yyyy-mm-ddThh:mm:ss".\n Year is required, every other segment is optional, but missing characters must be replaced with "x".\n end_date must be identical to or chronologically after start_date.'
    )
    parser.add_argument('key_terms',
        type=str,
        required=False,
        help='Comma separated list of key terms to search for'
    )
    parser.add_argument('location',
        type=str,
        required=False,
        help='Name of location of interest'
    )
    
    @api.expect(parser)
    @api.response(200, 'Article retrieved', search_result_model)
    @api.response(400, 'Invalid parameters')
    @api.response(404, 'No results found')
    def get(self):
        data = Articles.parser.parse_args()
        date_regex = re.compile('^(\d{4})-(\d\d|xx)-(\d\d|xx)T(\d\d|xx):(\d\d|xx):(\d\d|xx)$')
        year_regex = re.compile('^(\d{4})')
        if not date_regex.match(data['start_date']) or not date_regex.match(data['end_date']) or data['start_date'] > data['end_date']:
            return {'comment': 'Invalid parameters'}, 400
        else: # start and end dates valid
            search_results = list(filter(lambda x: (x['date_of_publication'] <= data['end_date'] and x['date_of_publication'] >= data['start_date']), articles))
            '''
            if data['key_terms']: #TODO test if this actually works
                search_terms = data['key_terms'].split(','); # add synonyms???
                filtered_results = []
                for article in search_results:
                    for report in article['reports']:
                        diseases_string = ''
                        # put all diseases into one string, then check if keywords match
                        diseases_string = report['disease'].join(',')
                        for term in search_terms:
                            if term in diseases_string:
                                filtered_results += article
                                break
                search_results = filtered_results
            '''
            if data['location']:
                geonames_id
                pass
            if search_results:
                return {'articles': search_results}
            else:
                return {'comment': 'No results found'}, 404

api.add_resource(Article, '/article/<article_id>')
api.add_resource(Articles, '/articles')

if __name__ == '__main__':
    #while True:
    out = open("log", "w")
    
    res = scrape.scrape_news("http://www.cidrap.umn.edu/news-perspective", [])
    for r in res:
        json.dump(r, indent=4, sort_keys=True, fp=out)
        out.write("\n")
    out.close()
    
    update_db.add_result(res)
    app.run(debug=True)

