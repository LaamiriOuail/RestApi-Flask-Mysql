from flask import *
import json
from car import Car
from db import DB
from flask_cors import CORS


db=DB()
app=Flask(__name__)
CORS(app)
@app.route('/getCars', methods=['GET'])
def get_students():
    data=db.getAllCars()
    return json.dumps(data)
    
@app.route('/getCarById/<int:car_id>', methods=['GET'])
def get_student_by_id(car_id:int):
    data = db.getCarById(car_id)
    if data==False:
        data=[]
    return jsonify(data)
@app.route('/addCar', methods=['POST', 'GET'])
def add_student():
    car = Car(request.form["id_car"],
                      request.form["model"],
                      request.form["hp"],
                      request.form["marque"]
                      )
    db.addCar(car)
    data=db.getLasElement()
    return json.dumps(data)
@app.route('/updateCar/<int:car_id>', methods=['PUT'])
def update_student(car_id:int):
    car = Car(request.form["id_car"],
                      request.form["model"],
                      request.form["hp"],
                      request.form["marque"]
                      )
    data=db.updateCar(car_id,car)
    if data==False:
        data=[]
    return json.dumps(data)
@app.route('/deleteCar/<int:car_id>', methods=['DELETE'])
def delete_student(car_id):
    data=db.deleteCarById(car_id)
    if data==False: 
        data=[]
    return json.dumps(data)

if __name__ == '__main__':
    app.run(port=8888)
