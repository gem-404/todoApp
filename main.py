"""
This python todo app, created in flask,
will demonstrate my knowledge in CRUD design pattern,
as all items added to my todo list, will
be stored(created), read, updated or deleted, from my
mysql database.
"""

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)


@app.route("/login")
def login():
    """
    Here will be my login router.
    It will store a flask session
    for the user that will log in.
    """
    # DO SOMETHING TO AUTHENTICATE USER AND GENERATE TOKEN
    return render_template("main.html", token="token")


@app.route("/logout")
def logout():
    """
    Here lies my logout router. It
    will clear the session created by
    the person who logged in.
    """
    # RETRIEVE TOKEN FROM LOCAL STORAGE
    _ = request.get_json()['token']

    # log the user out
    return jsonify({'status': 'success'})


if __name__ == '__main__':
    app.run(debug=True)
