# Virtual Energy Trading Platform

## Overview
This project is a Virtual Energy Trading Platform built with FastAPI and SQLAlchemy. It allows users to trade energy by placing bids and managing their accounts.

## Features
- User management with roles (Customer, Staff, Admin)
- Energy bid creation and management
- RESTful API with versioning
- Database migrations with Alembic

## Requirements
- Python 3.11
- PostgreSQL

## Setup
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd virtual_energy_trading_platform
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure the database in `.env`:
   ```
   DATABASE_URL=postgresql://<username>:<password>@<host>:<port>/<database>
   ```

5. Run migrations:
   ```bash
   alembic upgrade head
   ```

6. Start the application:
   ```bash
   uvicorn main:app --reload
   ```

## Usage
- Access the API documentation at `http://127.0.0.1:8000/docs`.
- Use the endpoints to manage users and bids.

## Contributing
Feel free to submit issues and pull requests to improve the project.

## License
This project is licensed under the MIT License.
