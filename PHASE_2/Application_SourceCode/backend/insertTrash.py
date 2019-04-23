import db_operations as db

res = db.add_user({ 'username': 'Bob12', 'password': 'Bob', 'email': 'bob@gmail.com', 'name': 'Bob' })
res = db.add_user({ 'username': 'Bob12', 'password': 'Bob', 'email': '22bob@gmail.com', 'name': 'Bob' })
res = db.add_user({ 'username': 'Bob13', 'password': 'Bob', 'email': 'bob@gmail.com', 'name': 'Bob' })
