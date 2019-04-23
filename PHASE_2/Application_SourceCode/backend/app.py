from flask import Flask, render_template, request, jsonify, session
import json
import db_operations as db
import secretSession as cookieSession

app = Flask(__name__,
            static_folder = "../frontend/dist/static",
            template_folder = "../frontend/dist")

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")

@app.route('/auth/login', methods = ['POST'])
def login():
    if request.method == 'POST':
        body = json.loads(request.data.decode("utf-8"))
        username = body['username']
        password = body['password']
        # check db for account, here just check for admin for example
        # login_obj = { 'username': username, 'password': password }
        # print(login_obj)
        user_id = db.check_login(username, password)
        print("login with " + str(user_id))
        if user_id < 0:
            return jsonify(message='error', status=404), 404#, {'Access-Control-Allow-Origin': '*'}
        else:
            cookie = cookieSession.encodeFlaskCookie({'userId': user_id})
            return jsonify(message='success', status=200, cookie=cookie), 200#, {'Access-Control-Allow-Origin': '*'}
    return render_template("index.html")

@app.route('/auth/signup', methods = ['POST'])
def register():
    if request.method == 'POST':
        body = json.loads(request.data.decode("utf-8"))
        name = body['name']
        email = body['email']
        username = body['username']
        password = body['password']
        account = {
            'name':name,
            'email':email,
            'username':username,
            'password':password
        }
        print(account)
        if db.add_user(account) > 0:
            return jsonify(message='success'), 200#, {'Access-Control-Allow-Origin': '*'}
        else:
            return jsonify(message='error: username or email is taken'), 404#, {'Access-Control-Allow-Origin': '*'}
    return render_template("index.html")

@app.route('/saveArticle', methods = ['POST'])
def save_article():
    if request.method == 'POST':
        body = json.loads(request.data.decode("utf-8"))
        sess = body['user_id']
        url = body['url']
        text = body['text']
        headline = body['headline']
        user_id = cookieSession.decodeFlaskCookie(sess[len('session='):])['userId']
        article = {
            'user_id': user_id, 
            'url': url,
            'headline': headline,
            'text': text
        }
        print(article)
        if db.save_article(article) > 0:
            return jsonify(message='success'), 200#, {'Access-Control-Allow-Origin': '*'}
        else:
            return jsonify(message='error'), 404#, {'Access-Control-Allow-Origin': '*'}

@app.route('/getSavedArticles', methods = ['GET'])
def get_saved_articles():
    if request.method == 'GET':
        sess = request.args['session']
        user_id = cookieSession.decodeFlaskCookie(sess)['userId']
        articles = db.get_articles({'user_id': user_id})
        return jsonify(articles=articles), 200


app.run(debug=True)
