# app/models.py

from app import db

class Photo(db.Model):
    """
    Create a photo table
    """

    __tablename__ = 'photos'

    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(60), index=True, unique=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(
        db.DateTime, default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())

    def __init__(self, filename):
        """
        initialize with filename
        """
        self.filename = filename

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Photo.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<Photo: {}>".format(self.name)
