from app import db

class Photo(db.Model):
    """
    Create a photo table
    """

    __tablename__ = 'photos'

    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(60), index=True, unique=True)
