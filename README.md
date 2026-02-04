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
```css
1. Clone the repository:

git clone https://github.com/yourusername/stock-api.git
cd stock-api
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows
.venv\Scripts\activate
# Linux / Mac
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run development server
python manage.py runserver
```
#API Structure
Base URL
```css
http://localhost:8000/api/v1/
```

## 📌 API Endpoints

```css

| App        | Base Path                         | Description                                      |
|------------|-----------------------------------|--------------------------------------------------|
| Companies  | `/companies/`                     | List all available companies                     |
| Companies  | `/companies/<symbol>/`            | Get company details by stock symbol              |
| Stocks     | `/stocks/`                        | Retrieve stock data for all companies            |
| Stocks     | `/stocks/<symbol>/`               | Get stock data for a specific company            |
| Stocks     | `/stocks/AAPL/`                   | Example: fetch Apple (AAPL) stock data           |
| Docs       | `/swagger/`                       | Interactive API documentation (Swagger UI)       |
| Docs       | `/redoc/`                         | Read-only API documentation (ReDoc)              |

---
