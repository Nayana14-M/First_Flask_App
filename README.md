Book API - Flask Project

This is a simple RESTful API built using Flask, Flask-SQLAlchemy, and optionally Flask-Migrate. It allows you to perform CRUD operations on a collection of books stored in a SQLite database.

Project Structure

1 book_api/

2 ├── app.py # Main application with routes and API logic

3 ├── models.py # SQLAlchemy models

4 └── books.db # SQLite database (auto-created)

Setup Instructions

1. Clone the Repository or Download the Files

   cd book_api

2. Install Dependencies

   pip install flask flask-sqlalchemy flask-migrate

3. Run the Application (Without Migrations)

If you're not using Flask-Migrate:

python app.py

This will:

Create books.db if it doesn't exist

Create the Book table using db.create_all()

Start the Flask server at http://localhost:5000 / specified port in the code (ex:5005)

4. (Optional) Using Flask-Migrate for Schema Migrations

If you want to use Flask-Migrate:

# Set environment variable

 export FLASK_APP=app.py # On Windows: set FLASK_APP=app.py

# Initialize migrations

flask db init

# Generate migration script

 flask db migrate -m "Initial migration"


# Apply migration

 flask db upgrade


# API Endpoints

Add a Book - POST /books
{

       "title": "Clean Code",

       "author": "Robert C. Martin",

      "year": 2008

}

1.Get All Books - GET /books

2.Get Book by ID - GET /books/<id>

3.Update Book by ID - PUT /books/<id>

{

      "title": "Updated Title",
      "author": "Updated Author",
      "year": 2020

}

4.Delete Book by ID - DELETE /books/<id>

# Technologies Used
Python 3
Flask
Flask-SQLAlchemy
Flask-Migrate (optional)
SQLite
