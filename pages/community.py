from flask import jsonify, render_template, request, Response
from flask.ext.login import current_user, login_user

from functions import app
from models import User
from sqlalchemy import desc


@app.route('/community', methods=['GET'])
def community():

    login_user(User.query.get(1))

    # TODO: the instructions say to use raw SQL instead of an ORM
    # I was getting hung up on getting a direct connection to the database to be able to execute raw SQL
    recent_users = User.query.order_by(desc(User.signup_date)).limit(5).all()

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

