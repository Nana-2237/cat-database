from flask import jsonify, request
from connector.main import get_connection
from app.schemas import CatSchema

cat_schema = CatSchema()
cats_schema = CatSchema(many=True)

def register_routes(app):
    @app.route('/cats', methods=['GET'])
    def get_cats():
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM rase_pisici")
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(cats_schema.dump(results)), 200

    @app.route('/cats', methods=['POST'])
    def create_cat():
        data = request.json
        errors = cat_schema.validate(data)
        if errors:
            return jsonify(errors), 400

        conn = get_connection()
        cursor = conn.cursor()
        query = "INSERT INTO rase_pisici (name, Breed, Age, Gender) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (data['name'], data['Breed'], data['Age'], data['Gender']))
        conn.commit()
        cursor.close()
        conn.close()

        return jsonify({"message": "Cat created successfully"}), 201
