##put and delete - HTTP verbs
## working with API's -- json

from flask import Flask,jsonify,request

app = Flask(__name__)

##initial data in my to-do list
items=[
  {"id":1,"name":"Buy milk","discription":"Buy 2 litres of milk"},
  {"id":2,"name":"Buy bread","discription":"Buy 1 loaf of bread"},
  {"id":3,"name":"Buy eggs","discription":"Buy a dozen eggs"}
] 

@app.route("/")
def home():
  return "Welcome to the To-Do List API!"

@app.route("/items", methods=['GET'])
def get_items():
  return jsonify(items)

##get: retrieve a specific item by id
@app.route("/items/<int:item_id>", methods=['GET'])
def get_item(item_id):
  item=next((item for item in items if item["id"]==item_id),None)
  if item is None:
    return jsonify({"error":"Item not found"})
  return jsonify(item)

##Post: add a new item to the list
@app.route("/items", methods=['POST'])
def create_item():
  if not request.json or 'name' in request.json:
    return jsonify({"error":"Bad request"})
  new_item={
    "id": items[-1]["id"] +1 if items else 1,
    "name": request.json['name'],
    "discription": request.json('discription')
  }
  items.append(new_item)
  return jsonify(new_item) 

##Put: update an existing item
@app.route("/items/<int:item_id>", methods=['PUT'])
def update_item(item_id):
  item=next((item for item in items if item["id"]==item_id),None)
  if item is None:
    return jsonify({"error":"Item not found"})
  
  if not request.json:
    return jsonify({"error":"Bad request"})
  
  item['name']=request.json.get('name',item['name'])
  item['discription']=request.json.get('discription',item['discription'])
  
  return jsonify(item)

##Delete: remove an item from the list
@app.route("/items/<int:item_id>", methods=['DELETE'])
def delete_item(item_id):
  global items
  items=[item for item in items if item["id"]!=item_id]
  return jsonify({"result":"Item deleted successfully"}) 

if __name__=='__main__':
  app.run(debug=True)
