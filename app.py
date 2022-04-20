
from flask import Flask, render_template, jsonify
from flask_jwt import JWT, jwt_required
from users import authenticate, identity


app = Flask(__name__)
app.secret_key = 'mysecretkey'

jwt = JWT(app, authenticate, identity)

products_lst = [
    {'id': 1, 'name': 'prd1'}
]


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/products', methods=['POST'])
@jwt_required()
def products():
    return jsonify({'products': products_lst})


app.run(port=5757)
