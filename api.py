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

task_pos_args=reqparse.RequestParser()
task_pos_args.add_argument("task",type=str,help="Task is required",required=True)
task_pos_args.add_argument("summary",type=str,help="Summary is required",required=True)

task_update_args=reqparse.RequestParser()
task_update_args.add_argument("task",type=str)
task_update_args.add_argument("summary",type=str)

if __name__=='__main':
    app.run(debug=True)