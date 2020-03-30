from flaskrecap import app,db
from datetime import datetime

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    task = db.Column(db.String(100), nullable = False)
    assignee = db.Column(db.String(100), nullable=False)
    assigner = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable = False)
    date_created = db.Column(db.DateTime,nullable=False, default = datetime.utcnow)

    def __init__(self,task,assignee,assigner,description):
        self.task = task
        self.assignee = assignee
        self.assigner = assigner
        self.description = description

    def __repr__(self):
        return f"{self.assigner} has assigned {self.assignee} \n the following task ({self.task}). \n Here's a description {self.description}"