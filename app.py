#from flask import jsonify
#from requests import request
from flask import *

app = Flask(__name__)

@app.route('/hello/')
def welcome1():
    return "Hello World!--> Get Method Called"

@app.route('/hello/', methods=['POST'])
def welcome2():
    return "Hello World!--> Post Method Called"



@app.route('/logintest/', methods=['POST'])
def login1():
	uname = request.form['lid']
	passwd = request.form['pwd']
	if uname == "admin" and passwd == "admin":
			return "Hello "+uname+"  logged in"
	else:
		    return "Authentication Failed"
	



"""
@app.route('/login/', methods=['POST'])
def login():
	uname = request.form['lid']
	passwd = request.form['pwd']
	
	if uname == "admin" and passwd == "admin":
			return "Hello "+lid+" you are logged in"
	else:
		    return "Authentication Failed"

"""

@app.route('/hello/', methods=['PUT'])
def welcome3():
    return "Hello World!--> Put Method Called"

@app.route('/hello/', methods=['DELETE'])
def welcome4():
    return "Hello World!--> Delete Method Called"

@app.route('/person/')
def hello():
    return jsonify({'name':'Jimit',
                    'address':'India'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1005)