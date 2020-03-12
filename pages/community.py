from flask import jsonify, render_template, request, Response
from flask.ext.login import current_user, login_user

from functions import app
from models import User, db


RECENT_USER_COUNT = 5
RECENT_USER_QUERY = 'SELECT * FROM user ORDER BY signup_date DESC LIMIT {};'.format(RECENT_USER_COUNT)

@app.route('/community', methods=['GET'])
def community():

    login_user(User.query.get(1))

    connection = db.session.connection()
    recent_users = connection.execute(RECENT_USER_QUERY)

    args = {
            'recent_users': [
                {
                    'display_name': user.display_name,
                    'tier': user.tier,
                    'point_balance': user.point_balance,
                }
                for user in recent_users
            ]
    }
    return render_template("community.html", **args)

