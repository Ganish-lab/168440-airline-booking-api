# 168440-airline-booking-api
# Airline Booking API Project

## Introduction
This project is a simplified Airline Booking API built using Django and Django Rest Framework (DRF). It enables users to manage flights and passengers with CRUD operations through a RESTful API.

---

## Features
- Manage flights: Create, retrieve, update, and delete flights.
- Manage passengers: Create, retrieve, update, and delete passengers.
- Filter passengers by flight.
- Pagination for list endpoints.

---

## Prerequisites
Ensure the following are installed on your system:
- Python (>=3.10)
- pip (Python package manager)
- Git

---

## Setup Instructions
### Clone the Repository
```bash
git clone https://github.com/Ganish-lab/168440-airline-booking-api.git
cd 168440-airline-booking-api
```

### Create and Activate a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Apply Database Migrations
```bash
python manage.py migrate
```

### Run the Development Server
```bash
python manage.py runserver
```
Access the server at `http://127.0.0.1:8000/`.

---

## Testing the API
### Using `test_api.http`
1. Open the `test_api.http` file in a compatible editor like Visual Studio Code.
2. Use the built-in HTTP client to execute API requests.

### Using cURL or Postman
Use the base URL `http://127.0.0.1:8000/admin/` Username:ADMN  Password:123 

---

## Project Structure
### Models
#### Flight
- `flight_number`: CharField (unique)
- `departure`: DateTimeField
- `arrival`: DateTimeField
- `origin`: CharField
- `destination`: CharField
- `capacity`: IntegerField

#### Passenger
- `first_name`: CharField
- `last_name`: CharField
- `email`: EmailField (unique)
- `phone_number`: CharField
- `flight`: ForeignKey to `Flight` (many-to-one relationship)

### Serializers
- **FlightSerializer**: Converts `Flight` model instances to JSON format.
- **PassengerSerializer**: Includes `flight` details when serializing `Passenger` model instances.

### Views/ViewSets
- **FlightViewSet**:
  - Handles CRUD operations for `Flight`.
  - URL: `/api/flights/`

- **PassengerViewSet**:
  - Handles CRUD operations for `Passenger`.
  - URL: `/api/passengers/`

### API Endpoints
| Method | Endpoint             | Description                     |
|--------|----------------------|---------------------------------|
| GET    | `/api/flights/`      | List all flights               |
| POST   | `/api/flights/`      | Create a new flight            |
| GET    | `/api/flights/{id}/` | Retrieve flight by ID          |
| PUT    | `/api/flights/{id}/` | Update flight by ID            |
| DELETE | `/api/flights/{id}/` | Delete flight by ID            |
| GET    | `/api/passengers/`   | List all passengers            |
| POST   | `/api/passengers/`   | Create a new passenger         |
| GET    | `/api/passengers/{id}/` | Retrieve passenger by ID      |
| PUT    | `/api/passengers/{id}/` | Update passenger by ID        |
| DELETE | `/api/passengers/{id}/` | Delete passenger by ID        |

---

## Design Decisions
1. **ViewSets**: DRF's ViewSets are used to reduce boilerplate code and provide CRUD functionality automatically.
2. **Relationships**: Each `Passenger` is linked to one `Flight` using a foreign key to represent real-world associations.
3. **Validation**: DRF's serializer validation ensures data integrity (e.g., unique emails for passengers).
4. **Scalability**: Pagination and filtering support improve API performance for large datasets.

---

## License
This project is licensed under the MIT License - see the `LICENSE` file for details.

---

## Contact
For queries, please contact:
- **Name**: Robins Ganira
- **Email**: robins.ganira@strathmore.edu
