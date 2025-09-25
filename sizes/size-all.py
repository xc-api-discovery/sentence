from flask import Flask, json

sizes = [{"id": 1,"name": "small"},{"id": 2,"name": "big"},{"id": 3,"name": "skinny"}]

api = Flask(__name__)

@api.route('/api/sizes', methods=['GET'])
def get_sizes():
  return json.dumps(sizes)

@api.route('/api/sizes', methods=['POST'])
def post_sizes():
  return json.dumps({"success": True}), 201

@api.route('/api/sizes', methods=['DELETE'])
def delete_sizes():
  return json.dumps({"success": True}), 202

if __name__ == '__main__':
    api.run()