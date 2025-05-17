# API Testing with Pytest - JSONPlaceholder

This project demonstrates how to test REST API endpoints using `requests` and `pytest` in Python.

## Features
- GET requests to `/posts` and `/users` endpoints
- Validates status codes and JSON structure
- Automated testing with `pytest`

## Getting Started

```bash
git clone https://github.com/kullaniciadi/api-testing-jsonplaceholder.git
cd api-testing-jsonplaceholder
python -m venv venv
source venv/Scripts/activate  # Windows
pip install -r requirements.txt
pytest
