''' Skills route '''

import csv
import uuid
import logging

from flask import Blueprint, jsonify, request
from flask_cors import cross_origin
from sqlalchemy import and_
from app.models import Event, User


from app import bcrypt, db
from app.api import bp


@bp.route('/<userid>/events', methods=['POST'])
@cross_origin(supports_credentials=True)
def create(userid):
   user = User.query.get(userid)
   data = request.get_json()
   event = Event()
   event.name = data.get('name')
   event.category = data.get('category')
   event.place = data.get('place')
   event.address = data.get('address')
   event.start_date = data.get('start_dadte')
   event.end_date = data.get('end_date')
   event.method = True if data.get('method') == 'true' else False
   event.owner = user
   db.session.add(event)
   db.session.commit()
   return jsonify(event.serialize())


@bp.route('/<userid>/events', methods=['GET'])
@cross_origin(supports_credentials=True)
def read(userid):
   user = User.query.get(userid)
   events = Event.query.join(User).filter(User.id == userid)
   events = list(map(lambda event: event.serialize(), events))
   return jsonify(events)


@bp.route('/<userid>/events/<eventid>', methods=['GET'])
@cross_origin(supports_credentials=True)
def get_detail(userid, eventid):
   user = User.query.get(userid)
   event = Event.query.join(User).filter(
       User.id == userid and Event.id == eventid).first()
   return jsonify(event.serialize())


@bp.route('/<userid>/events/<uid_to_delete>', methods=['DELETE'])
@cross_origin(supports_credentials=True)
def delete(userid, uid_to_delete):
   user = User.query.get(userid)
   event = Event.query.join(User).filter(and_(User.id == userid, Event.id == data.get('id'))).first()
   db.session.delete(event)
   db.session.commit()
   return jsonify(event.serialize())


@bp.route('/<userid>/events', methods=['PUT'])
@cross_origin(supports_credentials=True)
def modify(userid):
   user = User.query.get(userid)
   data = request.get_json()
   event = Event.query.join(User).filter(and_(User.id == userid, Event.id == data.get('id'))).first()
   if event:
      event.name = data.get('name')
      event.category = data.get('category')
      event.place = data.get('place')
      event.address = data.get('address')
      event.start_date = data.get('start_dadte')
      event.end_date = data.get('end_date')
      event.method = True if data.get('method') == 'true' else False
      db.session.commit()
      return jsonify(event.serialize())
   else:
      return jsonify({}), 404