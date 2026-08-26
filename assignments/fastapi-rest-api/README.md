# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a small REST API with Python and FastAPI. You will create endpoints, validate request data with Pydantic models, and return clear HTTP responses.

## 📝 Tasks

### 🛠️ Build API Routes

#### Description
Create a FastAPI application that manages a collection of books. Store the books in memory and add routes for reading the collection, reading one book, and adding a new book.

#### Requirements
Completed program should:

- Create a `FastAPI` application in `main.py`
- Implement `GET /books` to return all books
- Implement `GET /books/{book_id}` to return one book by ID
- Implement `POST /books` to add a book and return the created book
- Use appropriate HTTP status codes and include a unique ID for each book


### 🛠️ Validate Requests and Responses

#### Description
Use Pydantic models to define the data accepted by the API and the shape of its responses. Validate required fields so incomplete or invalid books are rejected automatically.

#### Requirements
Completed program should:

- Define a request model with required `title` and `author` fields
- Define a response model that includes the book ID, title, author, and publication year
- Validate that the publication year is a reasonable four-digit year
- Return JSON responses with consistent field names and types


### 🛠️ Handle Errors and Test the API

#### Description
Make the API predictable for clients by handling missing books and testing successful and unsuccessful requests with FastAPI's interactive documentation or a test client.

#### Requirements
Completed program should:

- Return a `404 Not Found` response when a requested book does not exist
- Return a `422 Unprocessable Entity` response for invalid request data
- Add at least three tests covering a successful request and two error cases
- Include instructions for running the API with Uvicorn

