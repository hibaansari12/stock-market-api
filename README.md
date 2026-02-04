# Stock API

A Django REST Framework project to manage stock data for multiple companies.  
This project provides endpoints to fetch stock data, recent prices, summary statistics, and compare two companies.  
Swagger UI and ReDoc documentation are included for interactive exploration.

---

## Features

- List all companies and their stock symbols
- Retrieve all stock data for a company
- Get the most recent stock data for a company
- Generate summary statistics for a company's stock (average, max, min, latest close)
- Compare two companies’ recent stock data
- Interactive API documentation with **Swagger UI** and **ReDoc**

---

## Technologies Used

- Python 3.x  
- Django 5.x  
- Django REST Framework (DRF)  
- drf-yasg (Swagger / OpenAPI documentation)  
- SQLite (default, can be replaced with PostgreSQL/MySQL)

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/stock-api.git
cd stock-api
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows
.\.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate

#Install dependencies:
pip install -r requirements.txt

#Apply migrations:
python manage.py migrate

#Create a superuser (optional, for admin access):
python manage.py createsuperuser

#Run the development server:
python manage.py runserver

 API Structure
Base URL

## 📌 API Endpoints

| API Name              | Endpoint                               | Description                                      |
|----------------------|----------------------------------------|--------------------------------------------------|
| List Companies       | `/api/companies/`                      | Retrieve a list of all companies                 |
| Company Details      | `/api/companies/<symbol>/`             | Get details of a specific company by symbol      |
| List All Stocks      | `/api/stocks/`                         | Retrieve stock data for all companies            |
| Stock by Company     | `/api/stocks/<symbol>/`                | Get all stock records for a specific company     |
| Example (Apple)      | `/api/stocks/AAPL/`                    | Fetch stock data for Apple Inc (AAPL)            |
| Swagger UI           | `/swagger/`                            | Interactive API documentation (Swagger UI)       |
| ReDoc                | `/redoc/`                              | Read-only API documentation (ReDoc)              |
