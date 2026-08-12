# Assignment 3 — Flask API & MongoDB Atlas

## Overview

This assignment demonstrates Flask API development, reading backend data from a JSON file, handling frontend form submissions, and storing submitted data in MongoDB Atlas.

### Objectives

* Create a Flask `/api` endpoint.
* Read data from a backend JSON file.
* Return the data as a JSON response.
* Create a frontend form.
* Send form data to a Flask backend.
* Store submitted data in MongoDB Atlas.
* Handle successful and failed submissions.

---

# 1. Types of Databases

Databases can be broadly categorized into four commonly used types.

## 1.1 Relational Database

A **relational database** stores data in tables consisting of rows and columns. Relationships between tables are managed using keys.

### Examples

* MySQL
* PostgreSQL
* Oracle Database
* Microsoft SQL Server

Relational databases are commonly used for structured data and applications where relationships between data are important.

---

## 1.2 Document Database

A **document database** stores data as documents, commonly using JSON-like structures.

### Examples

* MongoDB
* CouchDB
* Firestore

Example:

```json
{
    "name": "Rahul",
    "email": "rahul@example.com",
    "grade": 85
}
```

MongoDB, which is used in this assignment, is a document-oriented NoSQL database.

---

## 1.3 Key-Value Database

A **key-value database** stores data as a collection of keys and their corresponding values.

### Examples

* Redis
* Amazon DynamoDB
* Riak

Example:

```text
"user_101" → "Rahul"
"user_102" → "Ankit"
```

Key-value databases are commonly used for caching, sessions, configuration data, and applications requiring fast lookups.

---

## 1.4 Graph Database

A **graph database** represents data using nodes and relationships between those nodes.

### Examples

* Neo4j
* Amazon Neptune
* ArangoDB

Example:

```text
Rahul ──FRIEND_OF──> Ankit
  │
  └──WORKS_AT──> Company A
```

Graph databases are useful when relationships between entities are the main focus, such as social networks, recommendation systems, and network analysis.

---

# 2. REST API

A **REST API (Representational State Transfer API)** allows different applications or services to communicate over HTTP. It commonly uses HTTP methods such as `GET`, `POST`, `PUT`, and `DELETE` to perform operations on resources.

In this assignment, the Flask `/api` route acts as an API endpoint. When a client sends a request to `/api`, the Flask application reads the backend data and returns it as a JSON response.

---

# 3. Task 1 — Flask API

## Objective

Create a Flask application with an `/api` route that reads data from a backend JSON file and returns the data as a JSON list.

## Project Flow

```text
dummy_data.json
       │
       ▼
   Flask App
       │
       ▼
    /api Route
       │
       ▼
   JSON Response
```

## Backend Data

The application stores the API data separately in:

```text
backend/
├── app.py
└── dummy_data.json
```

Example:

```json
[
    {
        "id": 1,
        "name": "Leanne Graham",
        "username": "Bret",
        "email": "Sincere@april.biz"
    }
]
```

Keeping the data in a separate JSON file prevents the API data from being hard-coded directly into the Flask application.

## Flask Code

```python
from flask import Flask, jsonify
import json

app = Flask(__name__)


@app.route("/api")
def api():
    with open("dummy_data.json", "r") as file:
        data = json.load(file)

    return jsonify(data)


if __name__ == "__main__":
    app.run(port=1000)
```

## Code Explanation

### Import Flask

```python
from flask import Flask, jsonify
```

* `Flask` is used to create the web application.
* `jsonify()` converts Python data into a JSON HTTP response.

### Import JSON

```python
import json
```

The `json` module is used to read and parse the JSON data file.

### Create Flask Application

```python
app = Flask(__name__)
```

This creates the Flask application instance.

### Create `/api` Route

```python
@app.route("/api")
def api():
```

The decorator connects the `/api` URL to the `api()` function.

### Read the Backend File

```python
with open("dummy_data.json", "r") as file:
    data = json.load(file)
```

The JSON file is opened in read mode and converted into Python data using `json.load()`.

### Return JSON

```python
return jsonify(data)
```

The loaded data is returned to the client as a JSON response.

---

# 4. Task 2 — Frontend Form and MongoDB Atlas

## Objective

Create a frontend form that submits data to a Flask backend and stores the submitted information in MongoDB Atlas.

## Application Flow

```text
User
 │
 ▼
Frontend Form
 │
 ▼
Frontend Flask Application
 │
 ▼
Backend Flask API
 │
 ▼
MongoDB Atlas
 │
 ├───────────────┐
 ▼               ▼
Success         Error
 │               │
 ▼               ▼
Success Page    Same Form Page
 │
 ▼
"Data submitted successfully"
```

## Main Components

### Frontend

The frontend provides a form where the user enters the required information. The submitted form data is sent to the Flask application.

### Backend

The backend receives the submitted data, processes it, and communicates with MongoDB Atlas.

### MongoDB Atlas

MongoDB Atlas stores the submitted information as a document in a MongoDB collection.

---

# 5. MongoDB Atlas Setup

MongoDB Atlas is the cloud-based platform used to host the MongoDB database for this assignment.

### Setup Steps

1. Create an account on MongoDB Atlas.
2. Create a MongoDB cluster.
3. Create the required database and collection.
4. Configure the database access credentials.
5. Get the MongoDB connection URL/connection string.
6. Create a `.env` file in the backend project.
7. Store the MongoDB connection URL inside the `.env` file.

Example:

```text
MONGODB_URI=mongodb+srv://username:password@cluster.mongodb.net/database_name
```

### Important Security Note

**Do not upload the `.env` file to GitHub.**

Add `.env` to `.gitignore`:

```text
.env
```

The MongoDB credentials and connection URL should remain private.

The application can then read the connection URL from the environment variable instead of hard-coding credentials in the Python source code.

---

# 6. MongoDB Atlas

MongoDB is a **document-oriented NoSQL database**.

Instead of storing data in traditional rows and columns, MongoDB stores data as documents.

Example document:

```json
{
    "name": "Rahul",
    "email": "rahul@example.com",
    "message": "Hello"
}
```

In this assignment, the Flask backend sends the submitted form data to MongoDB Atlas, where it is stored as a document.

---

# 7. Form Submission

The frontend collects user information and sends it to the backend.

```text
HTML Form
    ↓
POST Request
    ↓
Flask Backend
    ↓
MongoDB Atlas
```

The backend receives the form data and creates a MongoDB document from it.

---

# 8. Success Handling

After successful insertion into MongoDB Atlas, the user should be redirected to a separate page.

The page must display the required message:

> **Data submitted successfully**

The successful submission should use an actual redirect to the success page.

---

# 9. Error Handling

If an error occurs during submission, the user should **not be redirected**.

Instead, the error should be displayed on the original form page.

```text
Submission
    │
    ▼
Backend
    │
    ├── Success ──→ Redirect → Success Page
    │
    └── Error ───→ Same Form Page + Error Message
```

This allows the user to see the error and correct the form without being redirected away from the original page.

---

# 10. Technologies Used

* **Python** — Programming language
* **Flask** — Web framework
* **REST API** — Communication between applications
* **JSON** — Backend data format
* **HTML/CSS** — Frontend interface
* **MongoDB** — Document-oriented database
* **MongoDB Atlas** — Cloud-hosted MongoDB service
* **python-dotenv** — Environment variable management

---

# 11. Project Structure

```text
Assignment-3/
│
├── Task 1/
│   └── backend/
│       ├── app.py
│       └── dummy_data.json
│
├── Task 2/
│   ├── backend/
│   │   ├── app.py
│   │   ├── requirements.txt
│   │   └── .env
│   │
│   └── frontend/
│       ├── app.py
│       ├── requirements.txt
│       └── templates/
│           ├── index.html
│           └── submit.html
│
├── screenshots/
│   ├── 01-flask-api.png
│   ├── 02-form.png
│   ├── 03-mongodb.png
│   ├── 04-success.png
│   └── 05-error.png
│
├── Assignment-3.docx
└── README.md
```

> **Note:** The `.env` file is shown in the project structure for development purposes only. It should be excluded from Git using `.gitignore` and must not be committed to the repository.

---

# 12. Screenshots

## Flask API Response

![Flask API](screenshots/01-flask-api.png)

## Frontend Form

![Frontend Form](screenshots/02-form.png)

## MongoDB Atlas

![MongoDB Atlas](screenshots/03-mongodb.png)

## Successful Submission

![Success Page](screenshots/04-success.png)

## Error Handling

![Error Handling](screenshots/05-error.png)

---

# 13. What I Learned

Through this assignment, I practiced:

* Creating Flask applications
* Creating REST API endpoints
* Reading JSON files using Python
* Returning JSON responses
* Building frontend forms
* Sending data between frontend and backend
* Connecting Flask applications with MongoDB
* Setting up MongoDB Atlas
* Using environment variables for database credentials
* Handling successful requests
* Handling application errors
* Understanding different database models


