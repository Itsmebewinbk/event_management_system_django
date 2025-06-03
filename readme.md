#  Mini Event Management System API

A simple Event Management System built with Django and Django REST Framework

---

## Features

* Create and list upcoming events
* Register attendees with overbooking and duplicate protection
* View attendees of a specific event
* Pagination for attendee list 
* Swagger documentation for API
* Signals for attendee count tracking
* Logging support


## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd event_management_system
```

### 2. Create and Activate a Virtual Environment for linux

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Create `.env` File

Create a file named `.env` in the root directory:

```ini
check env_sample.sh
```

> Note: Use `SIGNAL_ENABLE=False` during testing to disable signal triggers for attendee count.

### 5. Create Logs Directory

```bash
mkdir logs
```

> Log files will be saved to `logs/error.log`

### 6. Apply Migrations

```bash
python manage.py migrate
```

### 7. Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 8. Run the Development Server

```bash
python manage.py runserver
```

Visit the following URLs:

* API Base: [http://127.0.0.1:8000/events/](http://127.0.0.1:8000/events/)
* Swagger Docs: [http://127.0.0.1:8000/api/docs/](http://127.0.0.1:8000/api/docs/)
* Admin Panel: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## Running Tests

### With Django's test runner:

```bash
python manage.py test
```



## 🌐 API Documentation

* Auto-generated Swagger UI: [http://127.0.0.1:8000/api/docs/](http://127.0.0.1:8000/api/docs/)


## 📂 Logs

Logs are saved in `logs/` with level DEBUG for development. Customize in `settings.py` as needed.



## Completed Aspects

* [x] Event Creation and Listing
* [x] Attendee Registration with validation
* [x] Attendee Listing with pagination
* [x] Clean architecture and separation of concerns
* [x] Basic unit tests (Django TestCase)
* [x] Swagger documentation
* [x] Logging and `.env` configuration
