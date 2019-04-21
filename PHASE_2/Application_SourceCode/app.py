from flask import Flask, render_template, request, session, jsonify
from flask_cors import CORS

app = Flask(__name__,
            static_folder = "./dist/static",
            template_folder = "./dist")

# Enable CORS
CORS(app)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")

@app.route('/login', methods = ['POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # check db for account, here just check for admin for example
        if username == 'admin' and password == 'password':
            #return render_template("index.html", login_name=username)
            return jsonify(message='success'), 200
        else:
            return jsonify(message='error'), 404
    return render_template("index.html")

@app.route('/register', methods = ['POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        account = {
            'name':name,
            'email':email,
            'username':username,
            'password':password
        }
        print(account)
        return jsonify(message='success'), 200
    return render_template("index.html")

app.run(debug=True)
