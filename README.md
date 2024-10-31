# Hotel Management API Gateway

This API Gateway serves as an intermediary for various microservices in a hotel management system. It routes requests to the appropriate services for managing guests, bills, bookings, room pricing, and room availability.

## Features

- Manage guests (CRUD operations)
- Handle billing (CRUD operations)
- Manage room bookings (CRUD operations)
- Fetch room pricing based on type and season
- Check and update room availability
- Retrieve datasets for guests, bookings, bills, and room pricing

### Endpoints

#### Guests

- **Get all guests**
    - **URL**: `/guests`
    - **Method**: `GET`
    - **Description**: Returns a list of all guests.
    - **Response**:
        - `200 OK`: List of guests.

- **Search guest by last name**
    - **URL**: `/guests/search`
    - **Method**: `GET`
    - **Description**: Returns guest details by last name.
    - **Query Parameter**: 
        - `last_name`: Last name of the guest.
    - **Response**:
        - `200 OK`: Guest details.
  
- **Add guest**
    - **URL**: `/guests`
    - **Method**: `POST`
    - **Description**: Adds a new guest.
    - **Request Body**:
        ```json
        {}
        ```
    - **Response**:
        - `201 Created`: Guest added successfully.

- **Update guest information**
    - **URL**: `/guests/<id>`
    - **Method**: `PUT`
    - **Description**: Updates guest information by ID.
    - **Request Body**:
        ```json
        {}
        ```
    - **Response**:
        - `200 OK`: Guest information updated.

- **Get guest by ID**
    - **URL**: `/guests/<id>`
    - **Method**: `GET`
    - **Description**: Returns guest details by ID.
    - **Response**:
        - `200 OK`: Guest details.

- **Delete guest by ID**
    - **URL**: `/guests/<id>`
    - **Method**: `DELETE`
    - **Description**: Deletes a guest by ID.
    - **Response**:
        - `204 No Content`: Guest deleted successfully.

#### Bills

- **Get all bills**
    - **URL**: `/bills`
    - **Method**: `GET`
    - **Description**: Returns a list of all bills.
    - **Response**:
        - `200 OK`: List of bills.

- **Create new bill**
    - **URL**: `/bills`
    - **Method**: `POST`
    - **Description**: Creates a new bill.
    - **Request Body**:
        ```json
        {}
        ```
    - **Response**:
        - `201 Created`: Bill created successfully.

- **Get specific bill by guest ID**
    - **URL**: `/bills/guest/<guest_id>`
    - **Method**: `GET`
    - **Description**: Returns bill details by guest ID.
    - **Response**:
        - `200 OK`: Bill details.

- **Get specific bill by bill ID**
    - **URL**: `/bills/<bill_id>`
    - **Method**: `GET`
    - **Description**: Returns bill details by bill ID.
    - **Response**:
        - `200 OK`: Bill details.

- **Update bill by bill ID**
    - **URL**: `/bills/<bill_id>`
    - **Method**: `PUT`
    - **Description**: Updates bill details by ID.
    - **Request Body**:
        ```json
        {}
        ```
    - **Response**:
        - `200 OK`: Bill updated.

- **Delete bill by bill ID**
    - **URL**: `/bills/<bill_id>`
    - **Method**: `DELETE`
    - **Description**: Deletes a bill by ID.
    - **Response**:
        - `204 No Content`: Bill deleted successfully.

#### Bookings

- **Create room booking**
    - **URL**: `/book/room`
    - **Method**: `POST`
    - **Description**: Creates a new room booking.
    - **Request Body**:
        ```json
        {}
        ```
    - **Response**:
        - `201 Created`: Room booked successfully.

- **See all bookings**
    - **URL**: `/bookings`
    - **Method**: `GET`
    - **Description**: Returns a list of all room bookings.
    - **Response**:
        - `200 OK`: List of bookings.

- **Delete a booking by ID**
    - **URL**: `/book/room/<booking_id>`
    - **Method**: `DELETE`
    - **Description**: Deletes a room booking by ID.
    - **Response**:
        - `204 No Content`: Booking deleted successfully.

#### Room Pricing

- **Get room price by room type and season**
    - **URL**: `/rooms/<room_type>/<season>`
    - **Method**: `GET`
    - **Description**: Returns room price based on type and season.
    - **Response**:
        - `200 OK`: Room price details.

- **Change room price by type and season**
    - **URL**: `/rooms/<room_type>/<season>`
    - **Method**: `PUT`
    - **Description**: Updates room price by type and season.
    - **Request Body**:
        ```json
        {}
        ```
    - **Response**:
        - `200 OK`: Room price updated.

#### Rooms

- **Update room availability**
    - **URL**: `/room/availability`
    - **Method**: `PUT`
    - **Description**: Updates the availability of a room.
    - **Request Body**:
        ```json
        {}
        ```
    - **Response**:
        - `200 OK`: Room availability updated.

- **Check room availability by room number**
    - **URL**: `/room/availability`
    - **Method**: `GET`
    - **Description**: Checks room availability by room number.
    - **Query Parameter**: 
        - `room_number`: Number of the room.
    - **Response**:
        - `200 OK`: Room availability status.

- **List of all rooms**
    - **URL**: `/rooms`
    - **Method**: `GET`
    - **Description**: Returns a list of all rooms.
    - **Response**:
        - `200 OK`: List of rooms.

- **Get room type by room ID**
    - **URL**: `/room/type/<room_number>`
    - **Method**: `GET`
    - **Description**: Returns room type by room ID.
    - **Response**:
        - `200 OK`: Room type details.

- **Update cleaning status by room ID**
    - **URL**: `/room/cleaning`
    - **Method**: `PUT`
    - **Description**: Updates cleaning status of a room.
    - **Request Body**:
        ```json
        {}
        ```
    - **Response**:
        - `200 OK`: Cleaning status updated.

#### Data Retrieval

- **Get all booking data**
    - **URL**: `/dataset/bookings`
    - **Method**: `GET`
    - **Description**: Returns all booking data.
    - **Response**:
        - `200 OK`: Booking data.

- **Get all data from guests**
    - **URL**: `/dataset/guests`
    - **Method**: `GET`
    - **Description**: Returns all guest data.
    - **Response**:
        - `200 OK`: Guest data.

- **Get all data from room pricing**
    - **URL**: `/dataset/room-pricing`
    - **Method**: `GET`
    - **Description**: Returns all room pricing data.
    - **Response**:
        - `200 OK`: Room pricing data.

- **Get all data from rooms**
    - **URL**: `/dataset/rooms`
    - **Method**: `GET`
    - **Description**: Returns all room data.
    - **Response**:
        - `200 OK`: Room data.

- **Get all data from bills (WIP)**
    -**URL**: `/dataset/bills`
    -**Method**: `GET`
    - **Description**: Returns all bills data
    - **Response**:
        - `200 OK`: Bills data.