import datetime
import jwt
from app import app, db, bcrypt


class User(db.Model):
    """ User Model for storing user related details """

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def __init__(self, email, password, admin=False):
        self.email = email
        self.password = bcrypt.generate_password_hash(
            password, app.config.get('BCRYPT_LOG_ROUNDS')
        ).decode()

    @staticmethod
    def decode_auth_token(auth_token):
        """
        Decodes the auth token
        :param auth_token:
        :return: integer|string
        """
        try:
            payload = jwt.decode(auth_token, app.config.get('SECRET_KEY'))
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'

    def encode_auth_token(self, user_id):
        """
        Generates the Auth Token
        :return: string
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=900),
                'iat': datetime.datetime.utcnow(),
                'sub': user_id
            }
            return jwt.encode(
                payload,
                app.config.get('SECRET_KEY'),
                algorithm='HS256'
            )
        except Exception as e:
            return e

    def serialize(self):
        return dict(id=self.id, email=self.email)


''' Un evento esta compuesto de nombre,  una  categoría  (las  cuatro  posibles 
categorías  son:  Conferencia,  Seminario,  Congreso  o  Curso
),  un  lugar,  una  dirección, una  fecha  de 
inicio y una fecha de fin, y si el evento es presencial o virtual '''


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    event_owner = db.Column(db.Integer, db.ForeignKey('user.id'))
    owner = db.relationship('User', backref='owner_event',
                            foreign_keys=[event_owner])
    name = db.Column(db.String(255),  nullable=False)
    category = db.Column(db.String(255),  nullable=False)
    place = db.Column(db.String(255),  nullable=False)
    address = db.Column(db.String(255),  nullable=False)
    start_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    end_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    method = db.Column(db.Boolean, default=False)

    def __str__(self):
        return self.name

    def serialize(self):
        return dict(
            id=self.id,
            name=self.name,
            owner=self.owner.id,
            category=self.category,
            place=self.category,
            address=self.address,
            start_date=self.start_date,
            end_date=self.end_date,
            method=self.method)
