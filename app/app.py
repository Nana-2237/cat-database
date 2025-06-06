# app.py
from flask import Flask, jsonify, request
from database import create_table, get_connection
from schemas import CatSchema

app = Flask(__name__)
cat_schema = CatSchema()
cats_schema = CatSchema(many=True)
def get_data():
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM rase_pisici")
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result

@app.route('/cats', methods=['POST'])
def create_cat():
    data = request.json
    errors = cat_schema.validate(data)
    if errors:
        return jsonify(errors), 400

    connection = get_connection()
    cursor = connection.cursor()
    query = "INSERT INTO rase_pisici (name, Breed, Age, Gender) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (data['name'], data['Breed'], data['Age'], data['Gender']))
    connection.commit()
    cursor.close()
    connection.close()

    return jsonify({"message": "Cat created successfully"}), 201

@app.route('/cats', methods=['GET'])
def get_cats():
    result = get_data()
    return jsonify(cats_schema.dump(result)), 200


create_table()
app.run(host="0.0.0.0", port=5000)
