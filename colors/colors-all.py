from flask import Flask, json

colors = [{"id": 1,"name": "blue"},{"id": 2,"name": "red"},{"id": 3,"name": "white"}]

api = Flask(__name__)

@api.route('/api/colors', methods=['GET'])
def get_colors():
  return json.dumps(colors)

@api.route('/api/colors', methods=['POST'])
def post_colors():
  return json.dumps({"success": True}), 201

@api.route('/api/colors', methods=['DELETE'])
def delete_colors():
  return json.dumps({"success": True}), 202

if __name__ == '__main__':
    api.run()