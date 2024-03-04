from flask import Flask
from flask_restful import Resource,Api,reqparse,abort,fields,marshal_with

app=Flask(__name__)
api=Api(app)
app.config['MONGODB_SETTINGS']={
    'db':'todomodel',
    'host':'localhost',
    'port':27017
}
db=MongoEngine()
db.init_app(app)

class Todomodel(db.Document):
    _id=db.IntField()
    task=db.StringField(required=True)
    summary=db.StringField(required=True)
task_pos_args=reqparse.RequestParser()
task_pos_args.add_argument("task",type=str,help="Task is required",required=True)
task_pos_args.add_argument("summary",type=str,help="Summary is required",required=True)

task_update_args=reqparse.RequestParser()
task_update_args.add_argument("task",type=str)
task_update_args.add_argument("summary",type=str)

ressource_fields={
    '_id':fields.Integer,
    'task':fields.String,
    'summary':fields.String
}

class ToDo(Resource):
    @marshal_with(ressource_fields)
    def get(self,todo_id):
        task=Todomodel.Objects.get(_id=todo_id)
        if not task:
            abort(404,message="could not find task with that id")
        return task
    @marshal_with(ressource_fields)
    def post(self,todo_id):
        args=task_pos_args.parse_args()
        todo=Todomodel(_id=todo_id,task=args['task'],summary=args['summary']).save()
        id_=todo._id
        return {"id":str(id_)},201

if __name__=='__main':
    app.run(debug=True)