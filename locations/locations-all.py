from flask import Flask, json

locations = [{"id": 1,"name": "city"},{"id": 2,"name": "mountain"},{"id": 3,"name": "beach"}]

api = Flask(__name__)

@api.route('/api/locations', methods=['GET'])
def get_locations():
  return json.dumps(locations)

@api.route('/api/locations', methods=['POST'])
def post_locations():
  return json.dumps({"success": True}), 201

@api.route('/api/locations', methods=['DELETE'])
def delete_locations():
  return json.dumps({"success": True}), 202

if __name__ == '__main__':
    api.run()