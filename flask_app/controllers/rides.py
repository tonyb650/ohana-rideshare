from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models import ride, message

#GET routes
@app.route('/ride/dashboard')
def dashboard_page():
    open_rides = ride.Ride.get_open_rides()
    filled_rides = ride.Ride.get_filled_rides()
    return render_template('dashboard.html',unbooked_rides=open_rides,filled_rides=filled_rides)

@app.route('/ride/edit/<int:ride_id>')
def ride_edit_page(ride_id):
    ride_obj = ride.Ride.get_one_by_id(ride_id)
    return render_template('ride_edit.html',ride=ride_obj)

@app.route('/ride/details/<int:ride_id>')
def ride_detail_page(ride_id):
    ride_obj = ride.Ride.get_one_by_id(ride_id)
    message_list = message.Message.get_by_ride_id(ride_id)
    return render_template('ride_detail.html',ride=ride_obj,messages=message_list)

@app.route('/ride/add')
def ride_add_page():
    return render_template('ride_request.html')

@app.route('/ride/delete/<int:ride_id>')
def ride_delete(ride_id):
    # Should set up a method to check if correct user on GET routes
    if not ride.Ride.get_one_by_id(ride_id).rider_id == session['user_id']:
        print("user not logged in")
        return redirect('/login')
    else:
        ride.Ride.delete(ride_id)
        return redirect('/ride/dashboard')

@app.route('/ride/assign/<int:ride_id>')
def ride_assign_driver(ride_id):
    # Should set up a method to check if correct user on GET routes
    data = {
        'ride_id' : ride_id,
        'driver_id' : session['user_id']
    }
    results = ride.Ride.assign_driver(data)
    return redirect('/ride/dashboard')

@app.route('/ride/cancel/<int:ride_id>')
def ride_unassign_driver(ride_id):
    # Should set up a method to check if correct user on GET routes
    data = {
        'ride_id' : ride_id
    }
    results = ride.Ride.unassign_driver(data)
    return redirect('/ride/dashboard')


#POST routes
@app.route('/ride/create', methods=['post'])
def create_ride():
    if ride.Ride.ride_is_valid(request.form):
        ride_id = ride.Ride.save(request.form)
        # clear session variables for ride if it does save    
        session.pop('destination', None)
        session.pop('origin', None)
        session.pop('details', None)
        session.pop('date', None)
        return redirect('/ride/dashboard') # redirect to dashboard
    else: #failed validations
        # Create session variables for ride if it doesn't save
        session['destination'] = request.form['destination']
        session['origin'] = request.form['origin']
        session['details'] = request.form['details']
        session['date'] = request.form['date']
        return redirect('/ride/add') #redirect to same page
    
@app.route('/ride/update', methods=['post'])
def update_ride():
    if ride.Ride.ride_is_valid(request.form):
        ride.Ride.update(request.form)
        # clear session variables for ride if it does save    
        session.pop('destination', None)
        session.pop('origin', None)
        session.pop('details', None)
        session.pop('date', None)
        return redirect('/ride/dashboard') # redirect to dashboard
    else: #failed validations
        # Create session variables for ride if it doesn't save
        session['destination'] = request.form['destination']
        session['origin'] = request.form['origin']
        session['details'] = request.form['details']
        session['date'] = request.form['date']
        return redirect(f"/ride/edit/{request.form['id']}") #redirect to same page