from flask import Flask, render_template, request, jsonify, session
import json

app = Flask(__name__,
            static_folder = "../../../vue-dashboard-master/dist/static",
            template_folder = "../../../vue-dashboard-master/dist")

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
        if username == 'admin' and password == 'password':
            return jsonify(message='success'), 200, {'Access-Control-Allow-Origin': '*'}
        else:
            return jsonify(message='error'), 404, {'Access-Control-Allow-Origin': '*'}
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
        return jsonify(message='success'), 200, {'Access-Control-Allow-Origin': '*'}
    return render_template("index.html")

app.run(debug=True)
