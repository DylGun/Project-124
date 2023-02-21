from flask import Flask, jsonify, request

app=Flask(__name__)

List = [
    {
        'id': 1,
        'Name': u'Raju',
        'Contact': u'9987644456', 
        'done': False
    },
    {
        'id': 2,
        'Name': u'Rahul',
        'Contact': u'9876543222', 
        'done': False
    }
]

@app.route("/add-data", methods=["POST"])

def add_task():

    if not request.json:
        return jsonify({
            "status": "success",
            "message": "Task added successfully"
        })