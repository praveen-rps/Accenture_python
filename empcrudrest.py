from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

empDb=[
	{ 'id':'1001',
       'name':'praveen',
	  'title':'Techincal Lead'
	},
	{ 'id':'1002',
       'name':'Kumar',
	  'title':'developer'
	}
]

@app.route('/test', methods=['GET'])
def test():
	return "flask server is running"


#Method to dispaly all the employee data 
@app.route('/employee/show',methods=['GET'])
def getAll():
	# write the database connectivity code to get all the data
	return jsonify({'emps':empDb})



#Method to insert an employee data into existing data
@app.route('/employee/add',methods=['POST'])
def addEmployee():
	dat = {
	'id': request.json['id'],
	'name':request.json['name'],
	'title':request.json['title']
	}
	empDb.append(dat)
	return jsonify(dat)


#Method to delete an employee data from the existing data
@app.route('/employee/delete/<empid>',methods=['DELETE'])
def deleteEmp(empid):
	em = [emp for emp in empDb if(emp['id']==empid) ]	
	if len(em) == 0:
		abort(404)

	empDb.remove(em[0])
	return jsonify({'response':'Success'})



#Method to search the employee based on empid
@app.route('/employee/search/<empid>', methods=['GET'])
def getEmpById(empid):
	temp = [emp for emp in empDb if(emp['id']==empid) ]
	return jsonify({'emps':temp})


#Method to update the employee based on empid
#id cannot be upated, ie primary key cannot be update.
@app.route('/employee/update/<empid>', methods=['PUT'])
def updateEmpById(empid):
	temp = [emp for emp in empDb if(emp['id']==empid) ]
	
	if 'name' in request.json: 
		temp[0]['name'] = request.json['name']

	if 'title' in request.json:
		temp[0]['title'] = request.json['title']

	return jsonify({'emps':temp[0]})




if __name__ == '__main__':
 app.run(port=5001)


