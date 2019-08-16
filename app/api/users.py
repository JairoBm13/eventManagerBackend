''' Skills route '''

import csv
import logging
import os
import uuid

from boto3 import client, set_stream_logger
from flask import Blueprint, jsonify, request
from flask_cors import cross_origin
from app import models

from app import bcrypt, db
from app.api import bp


@bp.route('/signup', methods=['POST'])
@cross_origin(supports_credentials=True)
def register():
    data = request.get_json()
    user = models.User(email=data['email'], password=data['password'])
    db.session.add(user)
    db.session.commit()
    auth_token = user.encode_auth_token(user.id)
    return jsonify(user.serialize())


@bp.route('/login', methods=['POST'])
@cross_origin(supports_credentials=True)
def login():
    try:
        data = request.get_json()
        user = models.User.query.filter_by(email=data['email']).first()
        hashUser = bcrypt.check_password_hash(user.password, data.get('password'))
        if user and hashUser:
            return jsonify(user.serialize()), 200
        else:
            return jsonify({})
    except Exception as e:
        print(e)
        responseObject={
            'status': 'fail',
            'message': 'Try again'
        }
        return jsonify(responseObject), 500
