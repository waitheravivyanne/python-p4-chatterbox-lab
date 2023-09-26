from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_migrate import Migrate
from models import Message  
from database import db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

CORS(app)
migrate = Migrate(app, db)

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/messages', methods=['GET'])
def get_messages():
    messages = Message.query.all()
    message_list = []
    for message in messages:
        message_list.append({
            'id': message.id,
            'body': message.body,
            'username': message.username,
            'created_at': message.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            'updated_at': message.updated_at.strftime("%Y-%m-%d %H:%M:%S")
        })
    return jsonify(message_list)

@app.route('/messages/<int:id>', methods=['GET'])
def get_message_by_id(id):
    message = Message.query.get(id)
    if message:
        return jsonify({
            'id': message.id,
            'body': message.body,
            'username': message.username,
            'created_at': message.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            'updated_at': message.updated_at.strftime("%Y-%m-%d %H:%M:%S")
        })
    else:
        return jsonify({'error': 'Message not found'}), 404

if __name__ == '__main__':
    app.run(port=5555)
