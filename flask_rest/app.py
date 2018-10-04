from flask import Flask, request
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)

items = []


class Item(Resource):
    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None)
        return { 'item': item }, 200 if item else 404

    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None):
            return { 'message': 'Item with name \'{}\' already exists.'.format(name)}, 400

        new_item = request.get_json()
        item = { 'name': name, 'price': new_item['price'] }
        items.append(item)
        return item, 201

    def put(self, name):
        data = request.get_json()
        item = next(filter(lambda x: x['name'] == name, items), None)

        if item: # update
            item.update(data)
        else: # create
            item = { 'name': name, 'price': data['price'] }
            items.append(item)

        return item

    def delete(self, name):
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        return { 'message': 'Item successfully removed.'}


class ItemList(Resource):
    def get(self):
        return { 'items': items }


api.add_resource(ItemList, '/items')
api.add_resource(Item, '/items/<string:name>')

app.run(port=5050, debug=True)
