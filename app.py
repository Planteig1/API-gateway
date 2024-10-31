from flask import Flask, jsonify, request
import requests


app = Flask(__name__)

# Guests
    # * Get all - DONE
@app.route('/guests', methods=["GET"])
def get_guests():
    api = "http://guests-service:5000/guests"
    data = requests.get(api)

    if data.status_code == 404:
        return jsonify(data.json()), 400
    return jsonify(data.json()), 200

    # * Get by last name - DONE
@app.route('/guests/search', methods=["GET"])
def search_guest_by_last_name():
    last_name = request.args.get('last_name')
    api = "http://guests-service:5000/guests/search"
    data = requests.get(api, params={"last_name":last_name})

    if data.status_code == 404:
        return jsonify(data.json()), 400
    return jsonify(data.json()), 200

    # * Add guest - DONE
@app.route('/guests', methods=["POST"])
def create_guest():
    request_body = request.json
    api = "http://guests-service:5000/guests"
    data = requests.post(api, json=request_body)

    if data.status_code == 400:
        return jsonify(data.json()), 400
    return jsonify(data.json()), 200

    # * Change guest information - DONE
@app.route('/guests/<int:id>', methods=["PUT"])
def change_guest_information(id):
    request_body = request.json
    api = f"http://guests-service:5000/guests/{id}"
    data = requests.put(api, json=request_body)

    if data.status_code == 404:
        return jsonify(data.json()), 400
    return jsonify(data.json()), 200


    # * Get guest by id - DONE
@app.route('/guests/<int:id>', methods=["GET"])
def get_guest_id(id):
    api = f"http://guests-service:5000/guests/{id}"
    data = requests.get(api)

    if data.status_code == 404:
        return jsonify(data.json()), 400
    return jsonify(data.json()), 200

    # * Delete guest by id - DONE
@app.route('/guests/<int:id>', methods=["DELETE"])
def delete_guest_id(id):
    api = f"http://guests-service:5000/guests/{id}"
    data = requests.delete(api)

    if data.status_code == 404:
        return jsonify(data.json()), 400
    return jsonify(data.json()), 200


################
#Bills
    # * Get all bills - CHECK
@app.route('/bills', methods=["GET"])
def get_bills():
    api = "http://bill-service:5000/bills"
    data = requests.get(api)
    return jsonify(data), 200

    # * Create new bill - CHECK
@app.route('/bills', methods=["POST"])
def add_bill():
    request_body = request.json
    api = "http://bill-service:5000/bills"
    data = requests.post(api, json=request_body)
    if data.status_code == 200:
        return data.text, 200
    else:
        return data.text, 400

    # * Get specific bill by guest id - CHECK
@app.route('/bills/guest/<int:guest_id>', methods=["GET"])
def get_bill_by_guest_id(guest_id): 
    api = f"http://bill-service:5000/bills/guest/{guest_id}"
    data = requests.get(api)
    if data.status_code == 404:
        return jsonify(data.text), 400
    return data.json

    # * Get specific bill by bill id - CHECK
@app.route('/bills/<int:bill_id>', methods=["GET"])
def get_bill_by_bill_id(bill_id):
    api = f"http://bill-service:5000/bills/{bill_id}"
    data = requests.get(api)
    if data.status_code == 404:
        return jsonify(data.text), 400
    return data.json


    # * Update bill by bill id - CHECK
@app.route('/bills/<int:bill_id>', methods=["PUT"])
def update_bill(bill_id):
    request_body = request.json
    api = f"http://bill-service:5000/bills/{bill_id}"
    data = requests.put(api,json=request_body)
    if data.status_code == 404:
        return jsonify(data.text), 400
    return data.text, 200

    
    # * Delete bill by bill id - CHECK
@app.route('/bills/<int:bill_id>', methods=["DELETE"])
def delete_bill(bill_id):
    api = f"http://bill-service:5000/bills/{bill_id}"
    data = requests.put(api)
    if data.status_code == 404:
        return jsonify(data.json), 400
    return jsonify(data.json), 200




####################
    #Booking
    # * Create room booking - DONE
@app.route('/book/room', methods=["POST"])
def book_room():
    api = "http://booking-service:5000/book/room"
    new_booking = request.json
    data = requests.post(api, json=new_booking)
    
    if data.status_code == 200:
        return data.text, 200
    else:
        return data.text, 400

    # * See all bookings -  DONE
@app.route('/bookings', methods=["GET"])
def get_all_bookings():
    api = "http://booking-service:5000/bookings"
    data = requests.get(api)
    return data.json()

    # * Delete a booking by id - DONE
@app.route('/book/room/<int:booking_id>', methods=["DELETE"])
def delete_booking(booking_id):
    api = f"http://booking-service:5000/book/room/{booking_id}"
    data = requests.delete(api)

    if data.status_code == 200:
        return data.text, 200
    else:
        return data.text, 400
    
##############

#Room pricing
    # * Get room price by room type & season - DONE
@app.route('/rooms/<room_type>/<season>', methods=["GET"])
def get_room_price(room_type,season):
    api = f"http://room-pricing-service:5000/rooms/{room_type}/{season}"
    data = requests.get(api)

    if data.status_code == 400:
        return data.text, 400
    else:
        return jsonify(data.json()), 200

    # * Change room price by type and season - DONE
@app.route("/rooms/<room_type>/<season>", methods=["PUT"])
def update_room_price(room_type, season):
    request_body = request.json
    api = f"http://room-pricing-service:5000/rooms/{room_type}/{season}"
    data = requests.put(api,json=request_body)

    if data.status_code == 200:
        return jsonify(data.json()), 200
    return jsonify(data.json()), 400



####################

#Rooms
    # * Update room availability by room id - DONE
@app.route('/room/availability',methods=["PUT"])
def update_room_availability():
    api = "http://room-service:5000/room/availability"
    request_body = request.json
    data = requests.put(api,json=request_body)
    if data.status_code == 200:
        return data.text, 200
    else:
        return data.text, 400


    # * Check room availability by room id - DONE
@app.route('/room/availability', methods=["GET"])
def check_availability():
    room_number = request.args.get("room_number")
    api = "http://room-service:5000/room/availability"
    data = requests.get(api, params={"room_number": room_number})
    if data.status_code == 400:
        return data.text, 400
    elif data.status_code != 200:
        return data.text, 400
    return jsonify(data.json()), 200

    # * List of all rooms - DONE
@app.route('/rooms', methods=["GET"])
def get_all_rooms():
    api = "http://room-service:5000/rooms"
    data = requests.get(api)
    if data.status_code == 400:
        return data.text, 400
    return jsonify(data.json()), 200
    
    # * Get room type by room id - DONE
@app.route('/room/type/<int:room_number>', methods=["GET"])
def get_room_type(room_number):
    api = f"http://room-service:5000/room/type/{room_number}"
    data = requests.get(api)
    if data.status_code == 400:
        return data.text, 400
    return data.text, 200


    # * Update cleaning status by room id - DONE
@app.route('/room/cleaning', methods=["PUT"])
def update_cleaning():
    api = "http://room-service:5000/room/cleaning"
    request_body = request.json
    data = requests.put(api,json=request_body)
    if data.status_code == 400:
        return data.text, 400
    return data.text, 200
    
#Data retriveal 

    # * Get all booking data - DONE
@app.route('/dataset/bookings', methods=["GET"])
def get_all_bookings_data():
    api = "http://data-retriveal-service:5000/dataset/bookings"
    data = requests.get(api)
    if data.status_code == 400:
        return data.text, 400
    return data.text, 200
    # * Get all data from Guests - DONE
@app.route('/dataset/guests', methods=["GET"])
def get_all_guests_data():
    api = "http://data-retriveal-service:5000/dataset/guests"
    data = requests.get(api)
    if data.status_code == 400:
        return data.text, 400
    return data.text, 200

    # * Get all data from Bills

    # * Get all data from room-pricing - DONE
@app.route('/dataset/room-pricing', methods=["GET"])
def get_room_pricing():
    api = "http://data-retriveal-service:5000/dataset/room-pricing"
    data = requests.get(api)
    if data.status_code == 400:
        return data.text, 400
    return data.text, 200

    # * Get all data from rooms - DONE
@app.route('/dataset/rooms', methods=["GET"])
def get_rooms_data():
    api = "http://data-retriveal-service:5000/dataset/rooms"
    data = requests.get(api)
    if data.status_code == 400:
        return data.text, 400
    return data.text, 200




app.run(debug=True, host="0.0.0.0")