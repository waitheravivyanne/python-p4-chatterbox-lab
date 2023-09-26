from app import db, app
from models import Message
from faker import Faker
from random import choice as rc

fake = Faker()

usernames = [fake.first_name() for i in range(4)]
if "Duane" not in usernames:
    usernames.append("Duane")

def make_messages():
    Message.query.delete()
    
    messages = []

    for i in range(20):
        while True:
            username = rc(usernames)
            if username not in [message.username for message in messages]:
                break

        message = Message(
            body=fake.sentence(),
            username=rc(usernames),
        )
        messages.append(message)

    db.session.add_all(messages)
    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        make_messages()
