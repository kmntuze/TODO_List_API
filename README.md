# TODO List API

## Project Overview

This is a simple TODO List API built with Python Django and Django REST Framework.

The API allows a user to create, view, list, update, partially update, and delete TODO items and focuses on basic CRUD functionality, validation, logging, unit tests, Docker support, and a Postman collection for testing.

## Technology Used

- Python
- Django
- Django REST Framework
- SQLite
- Docker
- Docker Compose
- Postman

## Project Structure

```text
TODO_List_API/
|-- manage.py
|-- requirements.txt
|-- Dockerfile
|-- docker-compose.yml
|-- README.md
|-- postman/
|   |-- TODO_LIST_API.postman_collection.json
|-- todo_api/
|   |-- settings.py
|   |-- urls.py
|   |-- asgi.py
|   |-- wsgi.py
|-- todos/
|   |-- models.py
|   |-- serializers.py
|   |-- views.py
|   |-- urls.py
|   |-- tests.py
|   |-- migrations/
```

## API Structure

The API is based on one main resource: `Todo`.

Each TODO item has these fields:

| Field | Type | Description |
| --- | --- | --- |
| `id` | Integer | The unique ID of the TODO item |
| `title` | String | The title of the TODO item |
| `description` | String | More details about the TODO item |
| `is_completed` | Boolean | Shows if the TODO item is completed or not |
| `created_at` | DateTime | The date and time the TODO item was created |
| `updated_at` | DateTime | The date and time the TODO item was last updated |

## API Endpoints

Local base URL:

```text
http://127.0.0.1:8000
```

Deployed base URL:

```text
https://todo-list-api-4gca.onrender.com
```

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | `/api/todos/` | List all TODO items |
| POST | `/api/todos/` | Create a new TODO item |
| GET | `/api/todos/<id>/` | View one TODO item |
| PUT | `/api/todos/<id>/` | Update a TODO item |
| PATCH | `/api/todos/<id>/` | Partially update a TODO item |
| DELETE | `/api/todos/<id>/` | Delete a TODO item |

## Example Create Request

```json
{
  "title": "Finish TODO API",
  "description": "Complete and test the Django REST API",
  "is_completed": false
}
```

## Example Response

```json
{
  "id": 1,
  "title": "Finish TODO API",
  "description": "Complete and test the Django REST API",
  "is_completed": false,
  "created_at": "2026-05-11T08:00:00Z",
  "updated_at": "2026-05-11T08:00:00Z"
}
```

## Validation

The `title` field is required.

If the title is missing or blank, the API returns a `400 Bad Request` response.

Example invalid request:

```json
{
  "title": "   ",
  "description": "This should fail",
  "is_completed": false
}
```

## How To Run The Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/kmntuze/TODO_List_API.git
cd TODO_List_API
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

On Windows:

```bash
.venv\Scripts\activate
```

On macOS or Linux:

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run migrations

```bash
python manage.py migrate
```

### 6. Start the server

```bash
python manage.py runserver
```

The API will run at:

```text
http://127.0.0.1:8000/api/todos/
```

## How To Run Tests

Run the tests with:

```bash
python manage.py test
```

The tests cover creating, listing, viewing, updating, partially updating, and deleting TODO items. They also cover validation for missing or blank titles and checking that a missing TODO item returns `404 Not Found`.

## How To Run With Docker

Build the Docker image:

```bash
docker build -t todo-list-api .
```

Run the container:

```bash
docker run -p 8000:8000 todo-list-api
```

The API will be available at:

```text
http://127.0.0.1:8000/api/todos/
```

## How To Run With Docker Compose

Start the project with Docker Compose:

```bash
docker compose up --build
```

Stop the project with:

```bash
docker compose down
```

## Postman Collection

A Postman collection is included to test the API.

The collection is located here:

```text
postman/TODO_LIST_API.postman_collection.json
```

### How To Use The Postman Collection

1. Open Postman.
2. Click `Import`.
3. Select the file `postman/TODO_LIST_API.postman_collection.json`.
4. Open the imported collection named `TODO List API`.
5. Check the collection variables.
6. For local testing, set `base_url` to:

```text
http://127.0.0.1:8000
```

7. For deployed testing, set `base_url` to:

```text
https://todo-list-api-4gca.onrender.com
```

8. Start the Django server if testing locally.
9. Run the requests in this order:
   - Create TODO
   - List TODOs
   - View TODO
   - Update TODO
   - Patch TODO
   - Delete TODO
   - Blank Title Validation
   - Missing TODO

The collection also has a `todo_id` variable. After creating a TODO item, update `todo_id` with the ID returned by the API if needed.

## Logging

The project includes logging for important API actions, such as creating, updating, partially updating, deleting, and looking for a TODO item that does not exist.

Logs are shown in the console while the server is running.

## Deployment

This project is deployed on Render.

Public API URL:

```text
https://todo-list-api-4gca.onrender.com/api/todos/
```

Root URL:

```text
https://todo-list-api-4gca.onrender.com/
```

The root URL redirects to the TODO API endpoint.

## The project includes:

- Public GitHub repository
- Working deployed API URL
- Postman collection
- Dockerfile
- Docker Compose file
- README file
- Unit tests