from flask import Flask, json

animals = [{"id": 1,"name": "dog"},{"id": 2,"name": "cat"},{"id": 3,"name": "horse"}]

api = Flask(__name__)

@api.route('/api/animals', methods=['GET'])
def get_animals():
  return json.dumps(animals)

@api.route('/api/animals', methods=['POST'])
def post_animals():
  return json.dumps({"success": True}), 201

@api.route('/api/animals', methods=['DELETE'])
def delete_animals():
  return json.dumps({"success": True}), 202

if __name__ == '__main__':
    api.run()