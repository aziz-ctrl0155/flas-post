from root import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=True)
    created_by = db.Column(db.Integer, default=-1)

    def __repr__(self):
        return self.title

    def __init__(self, title, description, created_by: int = None, id: int = None):
        self.id = id
        self.title = title
        self.description = description
        self.created_by = created_by
