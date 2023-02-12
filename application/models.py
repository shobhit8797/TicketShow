from application import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

user_role = db.Table('user_role',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer, db.ForeignKey('role.id'))
)

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    description = db.Column(db.String(64), index=True, unique=True)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    name = db.Column(db.String(128))
    password_hash = db.Column(db.String(128))
    # address_id = db.Column(db.Integer, db.ForeignKey("address.id"), unique=True)
    role = db.relationship('Role', secondary=user_role, backref=db.backref('users', lazy='dynamic'))
    is_active = db.Column(db.Boolean, default=True)

    def get(id):
        return User.query.filter_by(id = id).first()



# venue_show = db.Table('venue_show',
#     db.Column('venue_id', db.Integer, db.ForeignKey('venue.id')),
#     db.Column('show_id', db.Integer, db.ForeignKey('show.id'))
# )

# class Address(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     street = db.Column(db.String(100), nullable=False)
#     city = db.Column(db.String(100), nullable=False)
#     state = db.Column(db.String(100), nullable=False)
#     zipcode = db.Column(db.String(100), nullable=False)
#     user_id = db.Column(db.Integer, db.ForeignKey("user.id"), unique=True)

# # Venue Table
# class Venue(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64), index=True, unique=True)
#     capacity = db.Column(db.Integer, nullable = False)
#     address_id = db.Column(db.Integer, db.ForeignKey("address.id"), unique=True)
#     place = db.Column(db.String(64), unique=True)


#     show = db.relationship('Show', secondary=venue_show, backref=db.backref('venues', lazy='dynamic'))
    

# class Show(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64), index=True, unique=True)
#     rating = db.Column(db.Integer, nullable = True, default=0)
#     price = db.Column(db.Integer, nullable = False)

#     venue = db.relationship('Venue', secondary=venue_show, backref=db.backref('shows', lazy='dynamic'))
