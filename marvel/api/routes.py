from flask import Blueprint, request, jsonify
from marvel.helpers import token_required
from marvel.models import db, Marvel, marvel_schema, marvels_schema

api = Blueprint('api', __name__, url_prefix = '/api')

@api.route('/getdata')
def getdata():
    return { 'some': 'value'}

#Create
@api.route('/marvels', methods = ['POST'])
@token_required
def create_marvel(our_user):

    name = request.json['name']
    description = request.json['description']
    comics_appeared_in = request.json['comics_appeared_in']
    super_power = request.json['super_power']
    date_created = request.json['date_created']
    user_token = our_user.token

    print(f"User Token: {our_user.token}")

    marvel = Marvel(name, description, comics_appeared_in, super_power, date_created, user_token)

    db.session.add(marvel)
    db.session.commit()
    response = marvel_schema.dump(marvel)

    return jsonify(response)


@api.route('/marvels/<id>', methods = ['GET'])
@token_required
def get_marvel(our_user, id):
    if id:
        marvel = Marvel.query.get(id)
        response = marvel_schema.dump(marvel)
        return jsonify(response)
    else:
        return jsonify({'message': 'ID is missing'}), 401
    

@api.route('/marvels', methods = ['GET'])
@token_required
def get_marvels(our_user):
    token=our_user.token
    marvels = Marvel.query.filter_by(user_token = token).all()
    response = marvels_schema.dump(marvels)
    return jsonify(response)



@api.route('/marvels/<id>', methods = ['PUT'])
@token_required
def update_marvel(our_user, id):
    marvel = Marvel.query.get(id)

    marvel.name = request.json['name']
    marvel.description = request.json['description']
    marvel.comics_appeared_in = request.json['comics_appeared_in']
    marvel.super_power = request.json['super_power']
    marvel.date_created = request.json['date_created']
    marvel.user_token = our_user.token

    db.session.commit()

    response = marvel_schema.dump(marvel)

    return jsonify(response)

@api.route('/marvels/<id>', methods = ['DELETE'])
@token_required
def delete_marvel(our_user, id):
    marvel = Marvel.query.get(id)
    db.session.delete(marvel)
    db.session.commit()
    response = marvel_schema.dump(marvel)
    return jsonify(response)

