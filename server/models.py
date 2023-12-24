from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData()

db = SQLAlchemy(metadata=metadata)

class SerializerMixin:
    def serialize(self):
        schema = self.Schema()
        return schema.dump(self)

# Add models here
class Earthquake(db.Model, SerializerMixin):
  __tablename__ = "earthquakes"

  id = db.Column(db.Integer, primary_key= True)
  magnitude = db.Column(db.Float)
  location = db.Column(db.String)
  year = db.Column(db.Integer)

  class Schema(db.SQLAlchemyAutoSchema):
    class Meta:
      model = Earthquake

  def __repr__(self):
    return f'<Earthquake {self.id}, {self.magnitude}, {self.location}, {self.year}'
