from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models import message

@app.route('/message/add', methods=['post'])
def add_message():
    print("request.form", request.form)
    message.Message.save(request.form)
    return redirect(f"/ride/details/{request.form['ride_id']}")